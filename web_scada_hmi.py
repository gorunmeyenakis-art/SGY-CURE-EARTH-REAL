import time, json, random
from flask import Flask, render_template_string, jsonify
from cyber_matrix_protocol import CyberTevhidProtocol
from predictive_maintenance import PredictiveMaintenanceEngine

app = Flask(__name__)
cyber = CyberTevhidProtocol()
pdm = PredictiveMaintenanceEngine()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SGY CURE-EARTH | Web SCADA Paneli</title>
    <style>
        body { background-color: #0e1117; color: #00ffcc; font-family: 'Courier New', monospace; padding: 20px; }
        .card { border: 1px solid #00ffcc; padding: 15px; margin-bottom: 15px; border-radius: 8px; background: #161b22; }
        h2 { color: #ff0055; text-align: center; }
        .status-ok { color: #00ff66; font-weight: bold; }
        .status-warn { color: #ffcc00; font-weight: bold; }
        .btn { background: #00ffcc; color: #000; padding: 10px 20px; border: none; font-weight: bold; cursor: pointer; border-radius: 5px; }
        .btn:hover { background: #ff0055; color: #fff; }
    </style>
</head>
<body>
    <h2>🚀 SGY CURE-EARTH CANLI WEB SCADA / HMI 🚀</h2>
    <div class="card">
        <h3>⚡ Donanım & Siber Güvenlik Statüsü</h3>
        <p>AnKA GLC Sx PLC: <span class="status-ok">ONLINE (Modbus RTU / 150MHz)</span></p>
        <p>Cebrail Şifreleme Kalkanı: <span class="status-ok">E2EE KİLİTLİ</span></p>
    </div>
    <div class="card">
        <h3>📊 Saha & Pres Parametreleri</h3>
        <p>Hidrolik Pres Basıncı: <b>1890.00 kN (~192.66 Ton)</b></p>
        <p>PT100 Sıcaklık: <span id="temp">42.5</span> °C</p>
        <p>Yapay Zeka PdM Sağlık Skoru: <span class="status-ok" id="pdm-score">%52.29</span></p>
    </div>
    <div class="card">
        <h3>🕹️ Saha Kontrol & Acil Müdahale</h3>
        <button class="btn" onclick="alert('AnKA GLC Sx SSR-1 Tetiklendi!')">SSR-1 Vana Aç/Kapat</button>
        <button class="btn" style="background:#ff0055; color:#fff;" onclick="alert('ACİL STOP TETİKLENDİ!')">⚠️ ACİL STOP</button>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/telemetry')
def telemetry():
    karar, skor = pdm.sensor_trend_analiz()
    return jsonify({
        "basinc_kn": 1890.00,
        "pdm_skor": skor,
        "status": "STABLE"
    })

if __name__ == "__main__":
    print("\n🌐 SGY CURE-EARTH WEB SCADA / HMI SUNUCUSU BAŞLATILIYOR (Port: 5000)...")
    # Termux localhost üzerinde web SCADA servisi
    app.run(host='0.0.0.0', port=5000, debug=False)
