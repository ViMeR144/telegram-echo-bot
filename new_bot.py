from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import logging
from flask import Flask
import threading
import os

# Инициализация Flask
app = Flask(__name__)

# Маршрут для проверки работоспособности
@app.route('/')
def home():
    return 'Бот работает!'

# Запуск Flask в отдельном потоке
def run_flask():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

# Включаем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Определяем обработчики команд
async def start_command(update, context):
    await update.message.reply_text('Привет! Я эхо-бот. Напиши мне что-нибудь!')

async def help_command(update, context):
    await update.message.reply_text('Просто напиши мне сообщение, и я его повторю!')

async def echo(update, context):
    await update.message.reply_text(update.message.text)

def main():
    print("Запуск бота...")
    
    # Запускаем Flask в отдельном потоке
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    print("Веб-сервер запущен")
    
    # Получаем токен из переменной окружения
    token = os.environ.get('TELEGRAM_TOKEN')
    if not token:
        print("Ошибка: не установлена переменная TELEGRAM_TOKEN")
        return
    
    # Создаем приложение
    app = ApplicationBuilder().token(token).build()
    
    print("Настройка обработчиков...")
    
    # Добавляем обработчики
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    print("Запуск процесса...")
    
    # Запускаем бота
    app.run_polling(allowed_updates=[])
    
    print("Бот остановлен")

if __name__ == "__main__":
    main() 