import time, logging
from saha_optimizasyonu import SahaOptimizer
from modbus_otomasyonu import PLCController
from sekillendirme_kuvvet import ForceRealizer

logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] - %(message)s")

def otonom_saha_dongusu():
    print("\n🌐 SGY CURE-EARTH OTONOM SAHA ORKESTRATÖRÜ BAŞLATILDI 🌐\n")
    
    # 1. Saha Bağlantısı ve Analitik
    optimizer = SahaOptimizer()
    if optimizer.baglanti_kontrol():
        # 2. Şekillendirme ve Kuvvet Hesabı
        realizer = ForceRealizer(malzeme="CELIK", etki_alani_mm2=4500)
        k_N, ton = realizer.gereken_kuvveti_hesapla()
        realizer.pres_tetikle(k_N, ton)
        
        # 3. Anomali ve Eylem Takibi
        durum = optimizer.veri_filtrele_ve_islem(85.0) # Test anomalisi
        if durum == "KRİTİK_ELEM_TETİKLE":
            plc = PLCController()
            plc.acil_durum_tetikle(valve_id=1)
            
    logging.info("🎯 Otonom Saha Döngüsü Kusursuz Tamamlandı.")

if __name__ == "__main__":
    otonom_saha_dongusu()
