import asyncio
import schedule
import time
from telegram import Bot

# استبدل هذا بالتوكن الخاص بك
TOKEN = "7899301801:AAFdIIhuPAXwo5_ylksHnPdbcs4qP59Wdy0"
CHANNEL_ID = "@DhikrAllahSWT"

# إنشاء كائن البوت
bot = Bot(token=TOKEN)

# دالة إرسال الرسالة
async def send_message():
    try:
        await bot.send_message(chat_id=CHANNEL_ID, text="لا إله إلا الله وحده لا شريك له، له الملك وله الحمد وهو على كل شيء قدير")
        print("تم إرسال الرسالة!")
    except Exception as e:
        print(f"حدث خطأ: {e}")

# جدولة الرسائل كل 5 دقائق
def schedule_message():
    schedule.every(5).minutes.do(lambda: asyncio.run(send_message()))

# تشغيل البوت
def run():
    print("بدء تشغيل البوت 🚀")
    schedule_message()
    while True:
        schedule.run_pending()
        print("البوت يعمل...")
        time.sleep(1)

run()