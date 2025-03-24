import asyncio
from telegram import Bot

async def test_bot():
    bot = Bot('6158315214:AAHLZ71hGuVElic6snIagpZSRJ-XGvUtmKs')
    try:
        me = await bot.get_me()
        print(f"Подключение успешно! Информация о боте:")
        print(f"ID: {me.id}")
        print(f"Имя: {me.first_name}")
        print(f"Username: {me.username}")
    except Exception as e:
        print(f"Ошибка при подключении: {e}")

if __name__ == '__main__':
    asyncio.run(test_bot()) 