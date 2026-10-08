package uz.qalqon.antiradar.service

import android.app.*
import android.content.Context
import android.content.Intent
import android.location.Location
import android.os.Build
import android.os.IBinder
import android.os.Looper
import android.speech.tts.TextToSpeech
import androidx.core.app.NotificationCompat
import com.google.android.gms.location.*
import java.util.*

/**
 * Antiradar Qalqon - Background Foreground Location & Alert Service
 * Ekrani o'chiq bo'lsa ham yoki boshqa ilovalar (Yandex/Google Maps)
 * ishlayotganda fonda radarlarni aniqlaydi va ovozli ogohlantiradi.
 */
class RadarForegroundService : Service(), TextToSpeech.OnInitListener {

    private lateinit var fusedLocationClient: FusedLocationProviderClient
    private lateinit var locationCallback: LocationCallback
    private var tts: TextToSpeech? = null
    private var isTtsReady = false

    companion object {
        const val CHANNEL_ID = "RadarServiceChannel"
        const val NOTIFICATION_ID = 1001
    }

    override fun onCreate() {
        super.onCreate()
        tts = TextToSpeech(this, this)
        createNotificationChannel()

        fusedLocationClient = LocationServices.getFusedLocationProviderClient(this)

        locationCallback = object : LocationCallback() {
            override fun onLocationResult(locationResult: LocationResult) {
                for (location in locationResult.locations) {
                    processDriverLocation(location)
                }
            }
        }

        startLocationUpdates()
    }

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        val notification = buildForegroundNotification("Antiradar faol: Yo'l himoyasi yoqilgan")
        startForeground(NOTIFICATION_ID, notification)
        return START_STICKY
    }

    private fun startLocationUpdates() {
        val locationRequest = LocationRequest.Builder(
            Priority.PRIORITY_HIGH_ACCURACY, 1000 // Har 1 soniyada
        ).apply {
            setMinUpdateIntervalMillis(500)
            setMinUpdateDistanceMeters(1.0f)
        }.build()

        try {
            fusedLocationClient.requestLocationUpdates(
                locationRequest,
                locationCallback,
                Looper.getMainLooper()
            )
        } catch (e: SecurityException) {
            e.printStackTrace()
        }
    }

    /**
     * GPS koordinata va tezlikni tekshirish
     */
    private fun processDriverLocation(location: Location) {
        val speedKmH = (location.speed * 3.6f).toInt() // m/s -> km/h
        val heading = location.bearing // 0..360 daraja

        // Bu yerda RadarEngine orqali eng yaqin kamera hisoblanadi:
        // Masalan: Agar 500m masofada 70 km/h radar bo'lsa va haydovchi 82 km/h ketsa:
        if (speedKmH > 70) {
            // Tezlik oshgani haqida ogohlantirish
            speakAlert("Diqqat! Kamera 70! Tezlikni tushiring!")
        }
    }

    private fun speakAlert(message: String) {
        if (isTtsReady && tts != null) {
            tts?.speak(message, TextToSpeech.QUEUE_FLUSH, null, "radar_alert")
        }
    }

    override fun onInit(status: Int) {
        if (status == TextToSpeech.SUCCESS) {
            tts?.language = Locale("uz") // O'zbek tili yoki Locale.getDefault()
            isTtsReady = true
        }
    }

    private fun createNotificationChannel() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val serviceChannel = NotificationChannel(
                CHANNEL_ID,
                "Antiradar Radar Service",
                NotificationManager.IMPORTANCE_LOW
            )
            val manager = getSystemService(NotificationManager::class.java)
            manager?.createNotificationChannel(serviceChannel)
        }
    }

    private fun buildForegroundNotification(contentText: String): Notification {
        return NotificationCompat.Builder(this, CHANNEL_ID)
            .setContentTitle("Qalqon Antiradar (ContraCam)")
            .setContentText(contentText)
            .setSmallIcon(android.R.drawable.ic_menu_compass)
            .setOngoing(true)
            .build()
    }

    override fun onDestroy() {
        super.onDestroy()
        fusedLocationClient.removeLocationUpdates(locationCallback)
        tts?.stop()
        tts?.shutdown()
    }

    override fun onBind(intent: Intent?): IBinder? = null
}
