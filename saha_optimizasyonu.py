import time, random, logging
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] - %(message)s")

class SahaOptimizer:
    def __init__(self, target_ip="127.0.0.1", port=502):
        self.target_ip = target_ip
        self.port = port
        self.is_connected = False
        self.buffer = []

    def baglanti_kontrol(self):
        """Saha cihazına bağlantı optimizasyonu ve yeniden bağlanma döngüsü"""
        retry_count = 0
        while not self.is_connected and retry_count < 3:
            logging.info(f"🔄 Saha Cihazına Bağlanılıyor ({self.target_ip}:{self.port})... Denede: {retry_count+1}")
            # Simüle edilmiş asenkron bağlantı testi
            time.sleep(0.2)
            if random.choice([True, True, False]): # %66 Bağlantı Başarısı Simülasyonu
                self.is_connected = True
                logging.info("✅ OT Ağ Bağlantısı Optimize Edildi ve Kilitlendi.")
                return True
            retry_count += 1
            time.sleep(0.5)
        
        logging.warning("⚠️ Saha Bağlantısı Başarısız! Sistem lokal önbellekleme (Offline Mode) moduna geçiyor.")
        return False

    def veri_filtrele_ve_islem(self, ham_veri):
        """Sensör verilerini kenarda (Edge) filtreleme ve anomali tespiti"""
        # Hareketli ortalama filtresi simülasyonu
        self.buffer.append(ham_veri)
        if len(self.buffer) > 5:
            self.buffer.pop(0)
        
        ortalama = sum(self.buffer) / len(self.buffer)
        
        # Anomali kontrolü (Eşik Değer)
        if abs(ham_veri - ortalama) > 15:
            logging.warning(f"🚨 ANOMALİ TESPİT EDİLDİ! Ham Veri: {ham_veri:.2f} | Ortalama: {ortalama:.2f}")
            return "KRİTİK_ELEM_TETİKLE"
        return "NORMAL"

# --- Saha Testi Başlatma ---
if __name__ == "__main__":
    print("\n⚡ SGY CURE-EARTH SAHA OPTİMİZASYON MOTORU BAŞLATILDI ⚡\n")
    optimizer = SahaOptimizer()
    
    if optimizer.baglanti_kontrol():
        print("\n📊 Sensör Akışı ve Kenar İşleme Test Ediliyor...")
        for i in range(10):
            # Rastgele okunan sıcaklık/basınç verisi simülasyonu
            okunan_veri = 50 + random.uniform(-5, 5) if i != 6 else 85.0 # 6. adımda yapay anomali
            durum = optimizer.veri_filtrele_ve_islem(okunan_veri)
            print(f"[{i+1}/10] Sensör Değeri: {okunan_veri:.2f} -> Sistem Durumu: {durum}")
            time.sleep(0.3)
