import sys, logging, traceback
from telegram_alarm_bot import TelegramAlarmDispatcher

logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] - %(message)s")

class SGYGlobalExceptionHandler:
    """Spagetti Try-Catch Yerine Merkezi Sistem Koruma Kalkanı (Global Exception Handling)"""
    def __init__(self):
        self.bot = TelegramAlarmDispatcher()
        # Python'un küresel yakalanmayan hata kancası
        sys.excepthook = self.handle_uncaught_exception

    def handle_uncaught_exception(self, exc_type, exc_value, exc_traceback):
        """Sistemde Yakalanmayan Herhangi Bir Hata Oluştuğunda Çalışır"""
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return

        error_msg = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
        logging.critical(f"💥 KÜRESEL KRİTİK HATA YAKALANDI:\n{error_msg}")
        
        # Otonom Telegram / SMS Botuna Kritik İhbarı Gönder
        self.bot.send_emergency_alert(
            level="CRITICAL_CRASH",
            title="Sistemde Beklenmeyen İstisna!",
            details=f"Hata Tipi: {exc_type.__name__} | Mesaj: {exc_value}"
        )

# Global Handler Başlatılıyor
global_shield = SGYGlobalExceptionHandler()

if __name__ == "__main__":
    print("\n🛡️ GLOBAL EXCEPTION HANDLING KALKANI AKTİF 🛡️\n")
    # Bilerek hata ürettirelim
    1 / 0
