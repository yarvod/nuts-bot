from django.conf import settings
from django.core.management import BaseCommand

from telegram import KeyboardButton, ReplyKeyboardMarkup, Update, ForceReply, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler


import emoji

from .utils import (
    update_or_create_user,
)

import logging

from ...constants import Messages

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


# funcs
def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    buttons = [
        [KeyboardButton(Messages.MESSAGE_ORDER)],
        [KeyboardButton(Messages.MESSAGE_CATALOG)],
        [KeyboardButton(Messages.MESSAGE_INFO)],
        [KeyboardButton(Messages.MESSAGE_CART)],
        [KeyboardButton(Messages.MESSAGE_HISTORY)],
        [KeyboardButton(Messages.MESSAGE_COMMENT)],
        [KeyboardButton(Messages.MESSAGE_WRITE_ATEPAPT)]
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
    updater = Updater(settings.TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    updater.start_polling()
    updater.idle()


class Command(BaseCommand):

    def handle(self, *args, **options):

        main()
