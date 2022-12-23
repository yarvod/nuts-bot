from django.core.management import BaseCommand

from telegram import KeyboardButton, ReplyKeyboardMarkup, Update, ForceReply, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler

from bot_backend.settings import TOKEN

import emoji

from .utils import (
    update_or_create_user,
)

import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

MESSAGE_ORDER = 'Заказ'
MESSAGE_CATALOG = 'Каталог'
MESSAGE_INFO = 'Общая информация'
MESSAGE_CART = 'Корзина'
MESSAGE_HISTORY = 'История заказов'
MESSAGE_COMMENT = 'Отзыв или комментарий'
MESSAGE_WRITE_ATEPAPT = 'Написать лично'


# funcs
def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    buttons = [
        [KeyboardButton(MESSAGE_ORDER)], 
        [KeyboardButton(MESSAGE_CATALOG)], 
        [KeyboardButton(MESSAGE_INFO)],
        [KeyboardButton(MESSAGE_CART)],
        [KeyboardButton(MESSAGE_HISTORY)],
        [KeyboardButton(MESSAGE_COMMENT)],
        [KeyboardButton(MESSAGE_WRITE_ATEPAPT)]
    ]

    user = update.effective_user
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"""
            {emoji.emojize(":waving_hand:")} Привет, {user.username}! \nЯ - орешковый бот, моя цель - помочь тебе выбрать подходящее лакомство на сегодняшний день/вечер (зависит от времени старта) и договориться о сделке наиболее комфортным способом. \nГотов приступать к работе: используй доступные кнопки для взаимодействия со мной.""",
        reply_markup=ReplyKeyboardMarkup(buttons)
    )

    update_or_create_user(user)


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text(f"""Чтобы начать: /start\n""")


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


class Command(BaseCommand):

    def handle(self, *args, **options):

        main()
