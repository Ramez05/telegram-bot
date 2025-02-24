import asyncio
import schedule
import time
from telegram import Bot

# استبدل بـ توكن البوت الخاص بك
TOKEN = "7899301801:AAFdIIhuPAXwo5_ylksHnPdbcs4qP59Wdy0"  
# استبدل بـ معرف قناتك
CHANNEL_ID = "@DhikrAllahSWT"  

bot = Bot(token=TOKEN)

# دالة لإرسال الرسالة
async def send_message():
    try:
        print("إرسال الرسالة الآن...")
        await bot.send_message(chat_id=CHANNEL_ID, text="لا إله إلا الله وحده لا شريك له، له الملك وله الحمد وهو على كل شيء قدير")
        print("تم إرسال الرسالة!")
    except Exception as e:
        print(f"حدث خطأ أثناء إرسال الرسالة: {e}")

# دالة للجوب (التي ستجدول الرسالة)
def job():
    print("الجوب بدأ")
    asyncio.run(send_message())

# جدولة الرسالة كل 5 دقائق
schedule.every(5).minutes.do(job)

# تشغيل الجدولة بشكل مستمر
while True:
    print("تشغيل الجدولة...")
    schedule.run_pending()
    time.sleep(1)