/**
 * Antiradar Qalqon - Audio & Voice Alert Engine
 * Web Audio API (Chime/Beeps) + SpeechSynthesis (O'zbekcha / Ruscha ovoz)
 */

export class AudioAlertEngine {
  private audioCtx: AudioContext | null = null;
  private isMuted: boolean = false;
  private lastSpokenText: string = '';
  private lastSpokenTime: number = 0;
  private speechCooldownMs: number = 8000; // Har 8 soniyada takrorlash
  private lastBeepTime: number = 0;

  constructor() {
    // AudioContext user gesture orqali initsializatsiya qilinadi
  }

  private initAudio() {
    if (!this.audioCtx) {
      const AudioContextClass = window.AudioContext || (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext;
      this.audioCtx = new AudioContextClass();
    }
    if (this.audioCtx.state === 'suspended') {
      this.audioCtx.resume();
    }
  }

  public setMuted(muted: boolean) {
    this.isMuted = muted;
  }

  public getMuted(): boolean {
    return this.isMuted;
  }

  /**
   * Radarga yaqinlashganda yumshoq ogohlantirish signali (Ding-dong)
   */
  public playApproachChime() {
    if (this.isMuted) return;
    this.initAudio();
    if (!this.audioCtx) return;

    const now = this.audioCtx.currentTime;
    const osc = this.audioCtx.createOscillator();
    const gain = this.audioCtx.createGain();

    osc.type = 'sine';
    osc.frequency.setValueAtTime(880, now); // A5
    osc.frequency.exponentialRampToValueAtTime(1320, now + 0.15); // E6

    gain.gain.setValueAtTime(0.3, now);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.35);

    osc.connect(gain);
    gain.connect(this.audioCtx.destination);

    osc.start(now);
    osc.stop(now + 0.35);
  }

  /**
   * Tezlik oshib ketganda xavf signali (Qattiq va tez bi-bi-bip)
   */
  public playOverSpeedWarning() {
    if (this.isMuted) return;
    const currentTime = Date.now();
    if (currentTime - this.lastBeepTime < 1200) return; // 1.2 soniya oraliq
    this.lastBeepTime = currentTime;

    this.initAudio();
    if (!this.audioCtx) return;

    const now = this.audioCtx.currentTime;
    
    // Ikki marta tez zarba beruvchi signal
    [0, 0.12].forEach((offset) => {
      if (!this.audioCtx) return;
      const osc = this.audioCtx.createOscillator();
      const gain = this.audioCtx.createGain();

      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(1600, now + offset);
      osc.frequency.exponentialRampToValueAtTime(1100, now + offset + 0.08);

      gain.gain.setValueAtTime(0.4, now + offset);
      gain.gain.exponentialRampToValueAtTime(0.01, now + offset + 0.08);

      osc.connect(gain);
      gain.connect(this.audioCtx.destination);

      osc.start(now + offset);
      osc.stop(now + offset + 0.09);
    });
  }

  /**
   * O'zbekcha / Ruscha ovozli xabar o'qish (TTS)
   */
  public speak(text: string, force: boolean = false) {
    if (this.isMuted || !('speechSynthesis' in window)) return;

    const now = Date.now();
    // Agar xuddi shu xabar yaqinda aytilgan bo'lsa va majburiy bo'lmasa qaytaramiz
    if (!force && this.lastSpokenText === text && now - this.lastSpokenTime < this.speechCooldownMs) {
      return;
    }

    this.lastSpokenText = text;
    this.lastSpokenTime = now;

    window.speechSynthesis.cancel(); // avvalgi gapni to'xtatish

    const utterance = new SpeechSynthesisUtterance(text);
    utterance.rate = 1.05; // Bir oz tezroq, haydovchi tez tushunishi uchun
    utterance.pitch = 1.0;
    utterance.volume = 1.0;

    // Mavjud ovozlardan O'zbek yoki Rus ovozini qidirish
    const voices = window.speechSynthesis.getVoices();
    const uzVoice = voices.find(v => v.lang.startsWith('uz'));
    const ruVoice = voices.find(v => v.lang.startsWith('ru'));

    if (uzVoice) {
      utterance.voice = uzVoice;
      utterance.lang = 'uz-UZ';
    } else if (ruVoice) {
      utterance.voice = ruVoice;
      utterance.lang = 'ru-RU';
    }

    window.speechSynthesis.speak(utterance);
  }
}
