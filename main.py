import subprocess
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackContext

# Замените 'YOUR_BOT_TOKEN' на полученный от BotFather токен
TOKEN = 'YOUR_BOT_TOKEN'

# Замените 'YOUR_CHAT_ID' на ваш Chat ID (можно узнать у @userinfobot в Телеграме)
CHAT_ID = 'YOUR_CHAT_ID'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Это бот для удаленного выполнения команд на сервере.')

def execute_command(update: Update, context: CallbackContext) -> None:
    # Проверяем, что команда вызвана из правильного чата
    if str(update.message.chat_id) != CHAT_ID:
        update.message.reply_text('Вы не имеете доступа к выполнению команд.')
        return

    # Получаем текст команды
    command = update.message.text

    try:
        # Выполняем команду на сервере
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout if result.returncode == 0 else result.stderr

        # Отправляем результат обратно в чат
        update.message.reply_text(output)

    except Exception as e:
        update.message.reply_text(f'Произошла ошибка: {str(e)}')

def main() -> None:
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, execute_command))
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
