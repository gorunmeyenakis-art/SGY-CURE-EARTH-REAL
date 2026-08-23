import time, logging
from cyber_matrix_protocol import CyberTevhidProtocol
from saha_optimizasyonu import SahaOptimizer
from sekillendirme_kuvvet import ForceRealizer
from predictive_maintenance import PredictiveMaintenanceEngine
from t3_gemstone_logger import T3GemstoneHardwareAccelerator
from aeron_warp_engine import AeronWarpSimulationEngine
from telegram_alarm_bot import TelegramAlarmDispatcher

logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] - %(message)s")

def otonom_saha_dongusu():
    print("\n🌌 SGY CURE-EARTH (KIZILELMA) FULL OTONOM ORKESTRATÖR BAŞLATILDI 🌌\n")
    
    # 1. Siber Güvenlik Duvarı
    cyber = CyberTevhidProtocol()
    cyber.rogue_hacker_scan()
    
    # 2. Donanım & NPU
    gemstone = T3GemstoneHardwareAccelerator()
    aeron_warp = AeronWarpSimulationEngine()
    bot = TelegramAlarmDispatcher()
    
    # 3. Kestirimci Bakım (PdM)
    pdm = PredictiveMaintenanceEngine()
    pdm_karar, pdm_skor = pdm.sensor_trend_analiz()
    
    if pdm_skor > 65.0:
        bot.send_emergency_alert("WARNING", "Yüksek PdM Arıza Skoru", f"AnKA GLC Sx verilerinde anomali: PdM Skor %{pdm_skor}")

    # 4. Saha & Kuvvet
    optimizer = SahaOptimizer()
    if optimizer.baglanti_kontrol():
        realizer = ForceRealizer(malzeme="CELIK", etki_alani_mm2=4500)
        k_N, ton = realizer.gereken_kuvveti_hesapla()
        realizer.pres_tetikle(k_N, ton)
        
        # Warp Simülasyonu & Aeron Telemetri
        warp_res = aeron_warp.run_warp_mesh_simulation(pres_bar=k_N, sicaklik_c=43.2)
        aeron_warp.aeron_publish_telemetry(warp_res)
        
        # T3 Gemstone NPU & PCIe 5.0 SSD Kayıt
        sample_data = {"basinc_kN": k_N, "tonaj": ton, "pdm_skor": pdm_skor, "warp_peak": warp_res["warp_stress_peak"]}
        enc_packet = gemstone.gemstone_npu_inference(sample_data)
        gemstone.pcie5_nvme_ultra_log(enc_packet)
        
    logging.info(f"🎯 Saha Döngüsü Aeron/Warp Motoru ve Telegram Alarm Kalkanıyla Tamamlandı.")

if __name__ == "__main__":
    otonom_saha_dongusu()
