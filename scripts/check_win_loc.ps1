Add-Type -AssemblyName System.Device
$watcher = New-Object System.Device.Location.GeoCoordinateWatcher([System.Device.Location.GeoPositionAccuracy]::High)
$watcher.Start()

$count = 0
while ($watcher.Status -ne [System.Device.Location.GeoPositionStatus]::Ready -and $count -lt 15) {
    Start-Sleep -Milliseconds 500
    $count++
}

Write-Output "Watcher Status: $($watcher.Status)"
Write-Output "Watcher Permission: $($watcher.Permission)"
if (-not $watcher.Position.Location.IsUnknown) {
    Write-Output "LAT: $($watcher.Position.Location.Latitude)"
    Write-Output "LNG: $($watcher.Position.Location.Longitude)"
    Write-Output "ALT: $($watcher.Position.Location.Altitude)"
    Write-Output "ACCURACY: $($watcher.Position.Location.HorizontalAccuracy)"
} else {
    Write-Output "Location is Unknown in Windows Location Services"
}
$watcher.Stop()
