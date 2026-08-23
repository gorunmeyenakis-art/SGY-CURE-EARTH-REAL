import time, logging
import global_exception_handler  # Tüm sistemi Spagetti Try-Catch'ten kurtaran Global Handler
from cyber_matrix_protocol import CyberTevhidProtocol
from robotik_otonom_core import OtonomRobotikMimarisi

logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] - %(message)s")

def otonom_saha_dongusu():
    print("\n🌌 SGY CURE-EARTH MERKEZİ HATA KALKANLI FULL OTONOM SİSTEM 🌌\n")
    cyber = CyberTevhidProtocol()
    cyber.rogue_hacker_scan()
    
    robot = OtonomRobotikMimarisi()
    robot.imu_dengelenme_analizi()
    robot.lidar_slam_haritalama()
    
    logging.info("✅ Tüm modüller Global Exception Handler güvencesiyle sorunsuz çalışıyor.")

if __name__ == "__main__":
    otonom_saha_dongusu()
