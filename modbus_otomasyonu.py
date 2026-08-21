import time, logging
from pymodbus.client import ModbusTcpClient

logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] - %(message)s")

class PLCController:
    def __init__(self, host="127.0.0.1", port=5020):
        self.host = host
        self.port = port
        self.client = ModbusTcpClient(self.host, port=self.port)

    def baglan(self):
        return self.client.connect()

    def acil_durum_tetikle(self, valve_id=0):
        """Anomali durumunda sahadaki röleyi/vanayı anında kapatır veya açar"""
        if self.baglan():
            # Coil (Röle) Tetikleme -> True (1)
            response = self.client.write_coil(valve_id, True)
            logging.info(f"⚡ PLC SAHA EYLEMİ: Vana/Röle #{valve_id} Güvenlik Moduna Alındı!")
            self.client.close()
            return True
        else:
            logging.error("❌ PLC İletişim Hatası! Saha cihazına ulaşılamıyor.")
            return False

if __name__ == "__main__":
    print("\n🏭 SGY CURE-EARTH PLC OTOMASYON MODÜLÜ TESTİ 🏭\n")
    plc = PLCController()
    # Test amaçlı güvenlik tetiklemesi
    plc.acil_durum_tetikle(valve_id=1)
