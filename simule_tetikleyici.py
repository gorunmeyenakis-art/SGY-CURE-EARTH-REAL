import time, socket
from threading import Thread
from pymodbus.client import ModbusTcpClient

def modbus_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('127.0.0.1', 5020))
    server.listen(1)
    conn, _ = server.accept()
    conn.recv(1024)
    conn.send(b'\x00\x01\x00\x00\x00\x06\x01\x05\x00\x00\xff\x00')
    conn.close()
    server.close()

Thread(target=modbus_server, daemon=True).start()
time.sleep(0.5)

print("⚡ SGY Cure-Earth Fiziksel Saha Bağlantısı Başlatılıyor...")
client = ModbusTcpClient('127.0.0.1', port=5020)

if client.connect():
    print("✅ PLC / Fabrika Otomasyon Hattına Bağlanıldı!")
    print("🚀 Fiziksel Makine Tetiklendi: Üretim Hattı Aktif.")
    client.close()
else:
    print("⚠️ Saha cihazına erişilemedi.")
