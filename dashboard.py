import time, os, sys, random

def clear():
    os.system('clear')

def render_dashboard():
    clear()
    print("\033[95m======================================================================\033[0m")
    print("\033[96m        🌌 SGY CURE-EARTH (KIZILELMA) CANLI SAHA & SİBER PANEL 🌌      \033[0m")
    print("\033[95m======================================================================\033[0m")
    
    # 1. Kök Sunucu & Siber-Matrix Katmanı
    print("\n\033[93m[1] CEBRAİL PROTOKOLÜ & PORT GÜVENLİK STATÜSÜ\033[0m")
    print(" ├─ E2EE Şifreleme   : \033[92m[AKTİF - SIFIR PARAZİT]\033[0m")
    print(" ├─ Firewall Modu   : \033[92m[RAJİM ENFORCEMENT ON]\033[0m")
    print(" └─ Port Taraması   : \033[92mEGO [KİLİTLİ]\033[0m | \033[91mKORKU [BANLANDI]\033[0m | \033[92mŞEHVET [KİLİTLİ]\033[0m")
    
    # 2. Saha & OT Haberleşme Katmanı
    status_color = "\033[92m" if random.choice([True, True, False]) else "\033[91m"
    print("\n\033[93m[2] SAHA OTOMASYONU & MODBUS NETWORK\033[0m")
    print(" ├─ Edge Gateway IP : 127.0.0.1:5020")
    print(f" ├─ PLC Bağlantı    : {status_color}ONLINE (0.2 ms Ping)\033[0m")
    print(" └─ Oto-Onarım      : \033[92mAUTO-RECONNECT READY\033[0m")
    
    # 3. Fiziksel Pres & Şekillendirme Kuvveti
    tonaj = 192.66 + random.uniform(-1.5, 1.5)
    print("\n\033[93m[3] HİDROLİK / SERVO PRES KİNEMATİĞİ\033[0m")
    print(f" ├─ İşlenen Malzeme : ÇELİK (4500 mm²)")
    print(f" ├─ Anlık Kuvvet    : \033[96m1890.00 kN\033[0m (~{tonaj:.2f} Ton)")
    print(" └─ Hidrolik Valf   : \033[92m[BASINÇ KİLİTLENDİ]\033[0m")
    
    # 4. Anomali & Sistem Durumu
    anomali = random.choice(["GÜVENLİ (STABLE)", "GÜVENLİ (STABLE)", "🚨 ANOMALİ (TETİK)"])
    anom_color = "\033[92m" if "GÜVENLİ" in anomali else "\033[91m"
    print("\n\033[93m[4] KENAR ANALİTİK (EDGE AI)\033[0m")
    print(f" └─ Saha Sağlığı    : {anom_color}{anomali}\033[0m")
    
    print("\n\033[95m======================================================================\033[0m")
    print("\033[90mDöngü güncelleniyor... Çıkış için CTRL+C yapın.\033[0m")

if __name__ == "__main__":
    try:
        for _ in range(5):  # Demo amaçlı 5 yenileme döngüsü
            render_dashboard()
            time.sleep(1.5)
        print("\n\033[92m[+] Dashboard testi başarıyla tamamlandı.\033[0m\n")
    except KeyboardInterrupt:
        print("\n\033[91m[-] Dashboard durduruldu.\033[0m")
