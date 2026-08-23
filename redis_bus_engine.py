import logging, json, time

logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] - %(message)s")

class RedisBusEngine:
    """In-Memory Redis Pub/Sub ve Cache Yönetim Katmanı"""
    def __init__(self):
        self.storage = {} # Redis In-Memory Mock Store
        
    def set_cache(self, key: str, value: dict, ttl_sec: int = 60):
        """Yüksek Hızlı Bellek İçi Önbellekleme (TTL Destekli)"""
        self.storage[key] = {
            "data": value,
            "expires_at": time.time() + ttl_sec
        }
        logging.info(f"⚡ REDIS CACHE SET -> Key: '{key}' (TTL: {ttl_sec}s)")

    def get_cache(self, key: str):
        """Önbellekten Milisaniyelik Okuma"""
        item = self.storage.get(key)
        if item and time.time() < item["expires_at"]:
            logging.info(f"🚀 REDIS CACHE HIT -> Key: '{key}'")
            return item["data"]
        logging.warning(f"⚠️ REDIS CACHE MISS -> Key: '{key}' (Süre dolmuş veya yok)")
        return None

if __name__ == "__main__":
    print("\n⚡ REDIS IN-MEMORY ENGINE AKTİF ⚡\n")
    r = RedisBusEngine()
    r.set_cache("telemetri_otonom", {"status": "STABLE", "temp": 38.5}, ttl_sec=10)
    data = r.get_cache("telemetri_otonom")
    print("Okunan Veri:", data)
