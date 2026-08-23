import time, logging
import global_exception_handler
from cyber_matrix_protocol import CyberTevhidProtocol
from robotik_otonom_core import OtonomRobotikMimarisi
from redis_bus_engine import RedisBusEngine

logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] - %(message)s")

def otonom_saha_dongusu():
    print("\n🐧 DEBIAN BASE & REDIS ACCELERATED OTONOM SİSTEM 🐧\n")
    
    # 1. Siber Güvenlik
    cyber = CyberTevhidProtocol()
    cyber.rogue_hacker_scan()
    
    # 2. Redis Bus & Önbellek
    redis_engine = RedisBusEngine()
    redis_engine.set_cache("sistem_durumu", {"os": "Debian-13-Netinst", "redis": "ACTIVE"})
    
    # 3. Otonom Robotik Kontrol
    robot = OtonomRobotikMimarisi()
    robot.imu_dengelenme_analizi()
    robot.lidar_slam_haritalama()
    
    logging.info("🎯 Sistem Debian tabanı, Redis in-memory hızı ve Global Exception korumasıyla kilitlendi.")

if __name__ == "__main__":
    otonom_saha_dongusu()
