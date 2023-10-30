import os
import json
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Токен Telegram Bot API
TOKEN = 'your_token_here'

# Папка, которую нужно мониторить
FOLDER_PATH = '/path/to/your/folder'

# Файл для хранения списка пользователей
USERS_FILE = 'users.json'

# Создаем объект Telegram Bot API
bot = telegram.Bot(token=TOKEN)

# Список ID всех пользователей, которые запустили бота
user_ids = []


# Функция для отправки уведомлений
def send_notification():
    message = 'Новый файл загружен в папку!'
    for user_id in user_ids:
        bot.send_message(chat_id=user_id, text=message)


# Функция для загрузки списка пользователей из файла
def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    else:
        return []


# Функция для сохранения списка пользователей в файл
def save_users():
    with open(USERS_FILE, 'w') as f:
        json.dump(user_ids, f)


# Функция обработки команды /help
def help_command(update, context):
    update.message.reply_text('Отправьте мне текстовое сообщение, чтобы я отправил его в чат.')


# Функция обработки сообщений
def echo(update, context):
    text = update.message.text
    for user_id in user_ids:
        bot.send_message(chat_id=user_id, text=text)


# Функция обработки событий мониторинга папки
def on_new_file(event):
    if event.is_directory:
        return None
    elif event.event_type == 'created':
        # Проверяем, что файл загружен полностью
        file_size = os.path.getsize(event.src_path)
        if file_size == event.metadata['size']:
            send_notification()


# Функция обратного вызова для команды /start
def start(update, context):
    user_id = update.effective_user.id
    if user_id not in user_ids:
        user_ids.append(user_id)
        save_users()
    update.message.reply_text('Привет! Я бот!')


if __name__ == '__main__':
    # Загружаем список пользователей из файла
    user_ids = load_users()

    # Создаем объект мониторинга папки
    observer = Observer()
    observer.schedule(FileEventHandler(on_new_file), FOLDER_PATH)

    # Запускаем мониторинг папки
    observer.start()

    # Создаем объект Updater для общения с Telegram Bot API
    updater = Updater(TOKEN, use_context=True)

    # Добавляем обработчики команд и сообщений
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Запускаем бота
    updater.start_polling()

    # Останавливаем мониторинг папки при остановке бота
    updater.idle()

    # Останавливаем мониторинг папки
    observer.stop()
    observer.join()
