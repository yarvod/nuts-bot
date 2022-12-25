import re

from django.conf import settings
from django.core.management import BaseCommand

from telegram import KeyboardButton, ReplyKeyboardMarkup, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

import emoji
import logging

from ... import utils
from ...constants import MainButtons
from ...messages import MessageGetHelp, MessageInfo, MessageGreeting

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


# funcs
def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    buttons = [
        [KeyboardButton(MainButtons.ORDER)],
        [KeyboardButton(MainButtons.CATALOG)],
        [KeyboardButton(MainButtons.INFO)],
        [KeyboardButton(MainButtons.CART)],
        [KeyboardButton(MainButtons.HISTORY)],
        [KeyboardButton(MainButtons.COMMENT)],
        [KeyboardButton(MainButtons.WRITE_ATEPAPT)]
    ]

    user = update.effective_user
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=MessageGreeting.format(*(emoji.emojize(":waving_hand:"), user.username)),
        reply_markup=ReplyKeyboardMarkup(buttons)
    )

    utils.update_or_create_user(user)
    

def get_product(update: Update, context: CallbackContext):
    slug = re.findall(r"/prod_(\w*)", update.message.text)[0]
    if not slug:
        update.message.reply_text("Продукт не найден :(")
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
    text = "\n".join([f"{i+1}. /prod_{item['slug']} {item['title']}" for i, item in enumerate(data)])
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text
    )


def write_atepart(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=MessageGetHelp
    )


def get_info(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=MessageInfo
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text(f"""Чтобы начать: /start\n""")


def main() -> None:
    updater = Updater(settings.TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help_command))
    dispatcher.add_handler(MessageHandler(Filters.regex(MainButtons.CATALOG), get_catalog))
    dispatcher.add_handler(MessageHandler(Filters.regex(MainButtons.WRITE_ATEPAPT), write_atepart))
    dispatcher.add_handler(MessageHandler(Filters.regex(MainButtons.INFO), get_info))
    dispatcher.add_handler(MessageHandler(Filters.text, get_product))

    updater.start_polling()
    updater.idle()


class Command(BaseCommand):

    def handle(self, *args, **options):

        main()
