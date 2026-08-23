import numpy as np
import time, logging, random
from cyber_matrix_protocol import CyberTevhidProtocol

logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] - %(message)s")

class PredictiveMaintenanceEngine:
    """SGY CURE-EARTH Yapay Zeka Tabanlı Kestirimci Bakım Motoru"""
    def __init__(self):
        self.cyber = CyberTevhidProtocol()
        # İdeal saha parametre eşik değerleri
        self.IDEAL_PRESS_BAR = 200.0
        self.IDEAL_TEMP_C = 45.0
        self.IDEAL_VIBRATION_MM_S = 1.2

    def sensor_trend_analiz(self):
        """Son 10 veri noktasının mikro sapmalarını ve Kestirimci Arıza Skorunu (0-100) hesaplar"""
        # Senaryo gereği zaman serisi verileri simüle ediliyor
        basinc_serisi = np.random.normal(self.IDEAL_PRESS_BAR, 5.0, 10)
        sicaklik_serisi = np.random.normal(self.IDEAL_TEMP_C, 2.5, 10)
        titresim_serisi = np.random.normal(self.IDEAL_VIBRATION_MM_S, 0.4, 10)

        # İstatistiksel sapma ve anomali analizi
        basinc_std = np.std(basinc_serisi)
        vibr_max = np.max(titresim_serisi)
        temp_mean = np.mean(sicaklik_serisi)

        # Rulman ve Valf Sağlık İndeksi (RHI / VHI) Hesabı
        ariza_skoru = (basinc_std * 4.0) + (vibr_max * 15.0) + (max(0, temp_mean - 50.0) * 2.0)
        ariza_skoru = min(100.0, round(ariza_skoru, 2))

        logging.info(f"🧠 EDGE AI ANALİZİ -> Titreşim Tepe: {vibr_max:.2f} mm/s | Isı Ort: {temp_mean:.1f}°C")
        logging.info(f"🔮 KESTİRİMCİ ARIZA SKORU: %{ariza_skoru}")

        # Erken Uyarı ve Bakım Kararı
        if ariza_skoru > 65.0:
            msg = f"⚠️ [UYARI] Hidrolik Valf/Rulman Aşınması Tespiti! Bakım Kalan Süre: ~48 Saat (Skor: %{ariza_skoru})"
            logging.warning(msg)
            return "BAKIM_ELEM_PLANLA", ariza_skoru
        else:
            logging.info("✅ Donanım Sağlığı Mükemmel Seviyede (RULMAN & VALF OK)")
            return "SİSTEM_STABLE", ariza_skoru

if __name__ == "__main__":
    print("\n🧠 SGY CURE-EARTH KESTİRİMCİ BAKIM MOTORU ÇALIŞTIRILDI 🧠\n")
    pdm = PredictiveMaintenanceEngine()
    karar, skor = pdm.sensor_trend_analiz()
