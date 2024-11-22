[텔레그램 봇파더 호출]

![image](https://github.com/user-attachments/assets/80959a71-f337-4e2a-a9a2-96942242accb)
---------------------------------------

[/start 보내기]

![image](https://github.com/user-attachments/assets/7644c12a-3d0d-4102-a2a3-536f843ac3a2)
---------------------------------------

[/newbot 보내기]

![image](https://github.com/user-attachments/assets/a197a6d9-16c9-4715-a2f1-fad88b7870f8)
---------------------------------------

[bot 이름 정하기]

![image](https://github.com/user-attachments/assets/98fee50c-9900-42e3-9459-8aef40b23a65)
---------------------------------------

[브라우저에 토큰 값 넣어서 호출]

Use this token to access the HTTP API:
8107204196:AAFxZTC5cRBR7QLRAdlifzrV9fz0tj7pvxE

https://api.telegram.org/bot8107204196:AAFxZTC5cRBR7QLRAdlifzrV9fz0tj7pvxE/getUpdates

![image](https://github.com/user-attachments/assets/a5937674-5d48-4830-a785-4d8922dad81b)
---------------------------------------

[만들어놓은 봇방에 아무 메세지나 보내기]

![image](https://github.com/user-attachments/assets/5ab3f74c-dcd3-4fb9-9fdb-85b59c7808d2)

[chat ID 얻기]

![image](https://github.com/user-attachments/assets/feef0d56-f329-44fd-ac88-83cd38a8cb21)
---------------------------------------

[아래는 실행코드]

```python
# pip install python-telegram-bot --upgrade
import asyncio
from telegram import Bot

TELEGRAM_TOKEN = "###"
CHAT_ID = "####"

async def send_telegram_message():
    bot = Bot(token=TELEGRAM_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text="안녕하세요! 파이썬에서 보내는 메시지입니다.")

asyncio.run(send_telegram_message())
```
---------------------------------------

[봇에 메세지 보내기]

![image](https://github.com/user-attachments/assets/92ce1c6a-fde6-4a3f-88fe-e5567f9d565a)
