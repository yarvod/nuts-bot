from django.conf import settings
from django.core.management import BaseCommand

from telegram import KeyboardButton, ReplyKeyboardMarkup, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

import emoji
import logging

from ... import utils
from ...constants import Messages

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


# funcs
def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    buttons = [
        [KeyboardButton(Messages.ORDER)],
        [KeyboardButton(Messages.CATALOG)],
        [KeyboardButton(Messages.INFO)],
        [KeyboardButton(Messages.CART)],
        [KeyboardButton(Messages.HISTORY)],
        [KeyboardButton(Messages.COMMENT)],
        [KeyboardButton(Messages.WRITE_ATEPAPT)]
    ]

    user = update.effective_user
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"""
            {emoji.emojize(":waving_hand:")} Привет, {user.username}! \nЯ - орешковый бот, моя цель - помочь тебе выбрать подходящее лакомство на сегодняшний день/вечер (зависит от времени старта) и договориться о сделке наиболее комфортным способом. \nГотов приступать к работе: используй доступные кнопки для взаимодействия со мной.""",
        reply_markup=ReplyKeyboardMarkup(buttons)
    )

    utils.update_or_create_user(user)
    

def get_product(update: Update, context: CallbackContext):
    slug = update.message.text.replace('/product', '').strip()
    product = utils.get_product(slug=slug)
    if not product:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Продукт не найден :('
        )
        return
    buttonsMenu = [
        [InlineKeyboardButton("Следующий", callback_data="UpVote")],
        [InlineKeyboardButton("Предыдущий", callback_data="DownVote")],
    ]
    keyboard_markup = InlineKeyboardMarkup(buttonsMenu)
    caption = f"{product['title']}. {product['description']}"
    context.bot.sendPhoto(
        chat_id=update.message.chat_id,
        photo=product['photo'],
        caption=caption,
        reply_markup=keyboard_markup
    )


def get_catalog(update: Update, context: CallbackContext):
    data = utils.get_catalog()
    text = "\n".join([f"{i+1}. {item['slug']} {item['title']}" for i, item in enumerate(data)])
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text(f"""Чтобы начать: /start\n""")


def main() -> None:
    updater = Updater(settings.TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help_command))
    dispatcher.add_handler(MessageHandler(Filters.regex(Messages.CATALOG), get_catalog))
    dispatcher.add_handler(CommandHandler('product', get_product))

    updater.start_polling()
    updater.idle()


class Command(BaseCommand):

    def handle(self, *args, **options):

        main()
