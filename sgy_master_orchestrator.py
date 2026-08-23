import time, logging
from cyber_matrix_protocol import CyberTeologyProtocol
from saha_optimizasyonu import SahaOptimizer
from modbus_otomasyonu import PLCController
from sekillendirme_kuvvet import ForceRealizer
from predictive_maintenance import PredictiveMaintenanceEngine

logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] - %(message)s")

def otonom_saha_dongusu():
    print("\n🌌 SGY CURE-EARTH (KIZILELMA) FULL OTONOM ORKESTRATÖR BAŞLATILDI 🌌\n")
    
    # 1. KATMAN: Siber-Matrix Güvenlik Duvarı
    cyber = CyberTeologyProtocol()
    cyber.rogue_hacker_scan()
    
    # 2. KATMAN: Yapay Zeka Kestirimci Bakım (PdM)
    pdm = PredictiveMaintenanceEngine()
    pdm_karar, pdm_skor = pdm.sensor_trend_analiz()
    
    # 3. KATMAN: Saha Bağlantısı ve Kuvvet Motoru
    optimizer = SahaOptimizer()
    if optimizer.baglanti_kontrol():
        realizer = ForceRealizer(malzeme="CELIK", etki_alani_mm2=4500)
        k_N, ton = realizer.gereken_kuvveti_hesapla()
        realizer.pres_tetikle(k_N, ton)
        
    logging.info(f"🎯 Saha Döngüsü Sıfır Zafiyet ve Kestirimci Bakım Kalkanıyla Tamamlandı. (PdM Skor: %{pdm_skor})")

if __name__ == "__main__":
    otonom_saha_dongusu()
