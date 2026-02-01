from telethon import TelegramClient, events
import requests
import asyncio

# ====== إعدادات Telegram ======
api_id = 39864754          # حط الـ api_id بتاعك
api_hash = "254da5354e8595342d963ef27049c772"  # حط الـ api_hash بتاعك

# القناة الخاصة (ID أو username)
CHANNEL_ID = -1003808609180  # استبدل بالـ ID بتاع قناتك

# لينك الموقع مع endpoint
WEBHOOK_URL = "https://telethon-production-ad53.up.railway.app/webhook"

# إنشاء الجلسة
client = TelegramClient("selva_session", api_id, api_hash)


@client.on(events.NewMessage(chats=CHANNEL_ID))
async def handler(event):
    msg = event.text
    if not msg:
        return

    payload = {
        "message": f"Successful Number in selva panel✅\n\n{msg}"
    }

    try:
        response = requests.post(WEBHOOK_URL, json=payload, timeout=10)
        if response.status_code == 200:
            print("تم إرسال الرسالة بنجاح ✅")
        else:
            print("فشل الإرسال:", response.status_code)
    except Exception as e:
        print("Error:", e)


async def main():
    await client.start()
    print("Telethon bot is running...")
    await client.run_until_disconnected()

asyncio.run(main())
