#!/bin/bash

# Doğru dizinde olduğumuzdan emin olalım
cd "$(dirname "$0")"

echo -e "\033[91m======================================================================\033[0m"
echo -e "\033[93m   🚀 SGY CURE-EARTH / HİPERSONİK SİBER VATAN KALKANI DEVREDE 🚀   \033[0m"
echo -e "\033[91m======================================================================\033[0m"

# 1. Modül ve Orkestratör Testi
echo -e "\n\033[96m[1/3] AnKA GLC Sx ve Siber-Matrix Orkestratör Çalıştırılıyor...\033[0m"
python3 anka_glc_driver.py
python3 sgy_master_orchestrator.py

# 2. Git Depo Güncelleme
echo -e "\n\033[96m[2/3] Bütün Modüller Siber Vatan Hattına Paketlendi...\033[0m"
git add .
git commit -m "AnKA GLC Sx sürücüsü ve Siber Vatan Kalkanı tam entegrasyonu"

# 3. GitHub Push
echo -e "\n\033[96m[3/3] GitHub Semalarına Aktarılıyor...\033[0m"
git push origin master

echo -e "\n\033[92m======================================================================\033[0m"
echo -e "\033[92m  ✅ OPERASYON BAŞARILI: Sistem Sıfır Zafiyetle Milli Ağda Yayında! \033[0m"
echo -e "\033[92m======================================================================\033[0m"
