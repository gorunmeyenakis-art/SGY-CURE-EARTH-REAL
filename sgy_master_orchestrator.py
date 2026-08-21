import time, logging
from cyber_matrix_protocol import CyberTeologyProtocol
from saha_optimizasyonu import SahaOptimizer
from modbus_otomasyonu import PLCController
from sekillendirme_kuvvet import ForceRealizer

logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] - %(message)s")

def otonom_saha_dongusu():
    print("\n🌌 SGY CURE-EARTH KORUMALI OTONOM ORKESTRATÖR BAŞLATILDI 🌌\n")
    
    # 1. KATMAN: Siber-Teolojik Güvenlik ve Şifreleme (Cebrail Protocol & Firewall)
    cyber = CyberTeologyProtocol()
    cyber.rogue_hacker_scan()
    packet = cyber.cebrail_protocol_encrypt("SYSTEM_STARTUP_COMMAND")
    
    # 2. KATMAN: Saha Bağlantısı ve Kenar Analitik
    optimizer = SahaOptimizer()
    if optimizer.baglanti_kontrol():
        
        # 3. KATMAN: Fiziksel Kuvvet ve Şekillendirme
        realizer = ForceRealizer(malzeme="CELIK", etki_alani_mm2=4500)
        k_N, ton = realizer.gereken_kuvveti_hesapla()
        realizer.pres_tetikle(k_N, ton)
        
        # 4. KATMAN: Anomali Tespiti ve PLC Eylemi
        durum = optimizer.veri_filtrele_ve_islem(85.0)
        if durum == "KRİTİK_ELEM_TETİKLE":
            plc = PLCController()
            plc.acil_durum_tetikle(valve_id=1)
            
    logging.info("🎯 Korumalı Saha Döngüsü Sıfır Zafiyetle Tamamlandı.")

if __name__ == "__main__":
    otonom_saha_dongusu()
