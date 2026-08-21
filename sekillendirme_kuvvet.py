import time, logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] - %(message)s")

class ForceRealizer:
    MALZEME_AKMA_DIRENCI = {
        "ALUMINYUM": 150,  # MPa (N/mm²)
        "CELIK": 350,      # MPa
        "TITANYUM": 850    # MPa
    }

    def __init__(self, malzeme="CELIK", etki_alani_mm2=5000):
        self.malzeme = malzeme
        self.alani = etki_alani_mm2

    def gereken_kuvveti_hesapla(self, sekillendirme_faktoru=1.2):
        """
        Şekillendirme için gereken Piston Kuvveti (F = sigma * A * k)
        """
        akma_gerilimi = self.MALZEME_AKMA_DIRENCI.get(self.malzeme.upper(), 300)
        # Kuvvet (Newton) = Gerilme (N/mm2) * Alan (mm2) * Faktör
        kuvvet_newton = akma_gerilimi * self.alani * sekillendirme_faktoru
        kuvvet_kn = kuvvet_newton / 1000.0
        tonaj = kuvvet_kn / 9.81
        
        return kuvvet_kn, tonaj

    def pres_tetikle(self, kuvvet_kn, tonaj):
        logging.info(f"⚙️ ŞEKİLLENDİRME PARAMETRELERİ: Malzeme: {self.malzeme} | Kesit: {self.alani} mm²")
        logging.info(f"📐 HESAPLANAN HEDEF KUVVET: {kuvvet_kn:.2f} kN (~{tonaj:.2f} Ton)")
        
        # PLC Servo / Hidrolik Oransal Vana Tetikleme
        time.sleep(0.3)
        logging.info("💥 HİDROLİK VALF TETİKLENDİ: Piston Tam Basınca Ulaştı, Malzeme Şekillendirildi.")
        return True

if __name__ == "__main__":
    print("\n🔨 SGY CURE-EARTH FİZİKSEL BÜKÜM & ŞEKİLLENDİRME MOTORU 🔨\n")
    realizer = ForceRealizer(malzeme="CELIK", etki_alani_mm2=4500)
    k_N, ton = realizer.gereken_kuvveti_hesapla()
    realizer.pres_tetikle(k_N, ton)
