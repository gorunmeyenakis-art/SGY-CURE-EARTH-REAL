import time, logging
import global_exception_handler
from cyber_matrix_protocol import CyberTevhidProtocol
from robotik_otonom_core import OtonomRobotikMimarisi
from redis_bus_engine import RedisBusEngine
from sgy_air_ground_fleet import SGYAirGroundFleetController

logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] - %(message)s")

def otonom_saha_dongusu():
    print("\n🏰 SGY CURE-EARTH FULL OTONOM KARARGAH VE LOJİSTİK ORKESTRASI 🏰\n")
    
    # 1. Siber Güvenlik ve Redis
    cyber = CyberTevhidProtocol()
    cyber.rogue_hacker_scan()
    
    redis_engine = RedisBusEngine()
    redis_engine.set_cache("karargah_durumu", {"os": "Debian-13", "redis": "ACTIVE", "fleet": "IN_POSITION"})
    
    # 2. Hava & Kara Lojistik ve Muhafız Jetler
    fleet = SGYAirGroundFleetController()
    fleet.jet_escort_and_patrol()
    fleet.heavy_cargo_air_fleet()
    fleet.ground_autonomous_vehicles()
    
    # 3. Robotik Kontrol
    robot = OtonomRobotikMimarisi()
    robot.imu_dengelenme_analizi()
    robot.lidar_slam_haritalama()
    
    logging.info("🎯 Karargah lojistiği, hava savunması ve otonom kara hatları tam kapasite kilitlendi.")

if __name__ == "__main__":
    otonom_saha_dongusu()
