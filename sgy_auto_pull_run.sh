#!/bin/bash

# --- CONFIGURATION ---
GITHUB_USER="gorunmeyenakis-art"
REPO_NAME="SGY-CURE-EARTH"
MAIN_SCRIPT="sgy_master_orchestrator.py"

echo "=================================================="
echo "🚀 SGY OTONOM KARARGAH GITHUB SYNC & LAUNCHER 🚀"
echo "=================================================="

# 1. GitHub Repository Güncelleme / Klonlama
if [ -d ".git" ]; then
    echo "📡 [1/3] Mevcut repodan en güncel kodlar çekiliyor (git pull)..."
    git fetch origin
    git reset --hard origin/main || git reset --hard origin/master
    git pull
else
    echo "📦 [1/3] Repo yerelde bulunamadı, GitHub'dan sıfırdan çekiliyor..."
    git clone https://github.com/${GITHUB_USER}/${REPO_NAME}.git .
fi

# 2. Gerekli Python Paketleri ve Çalışma Alanı Kontrolü
echo "⚙️ [2/3] Bağımlılıklar ve sistem gereksinimleri taranıyor..."
python3 -c "import sys, logging" 2>/dev/null || pkg install python -y

# 3. Ana Orkestratörü Başlatma
echo "⚡ [3/3] Otonom Karargah ve Filo Kontrolü Devreye Alınıyor..."
echo "=================================================="

python3 ${MAIN_SCRIPT}

