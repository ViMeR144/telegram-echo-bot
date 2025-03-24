# -*- coding: utf-8 -*-
import asyncio
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Обработчики команд
async def start(update, context):
    await update.message.reply_text('Привет! Я эхо-бот. Я буду повторять все ваши сообщения.')

async def help_command(update, context):
    await update.message.reply_text('Просто отправьте мне любое сообщение, и я повторю его.')

async def echo(update, context):
    await update.message.reply_text(update.message.text)

async def main():
    # Создаем бота и приложение
    bot = Bot('6158315214:AAHLZ71hGuVElic6snIagpZSRJ-XGvUtmKs')
    
    # Проверяем подключение
    try:
        await bot.get_me()
        print("Бот успешно подключен!")
    except Exception as e:
        print(f"Ошибка при подключении бота: {e}")
        return

    application = Application.builder().token('6158315214:AAHLZ71hGuVElic6snIagpZSRJ-XGvUtmKs').build()

    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Запускаем бота
    await application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    asyncio.run(main()) 