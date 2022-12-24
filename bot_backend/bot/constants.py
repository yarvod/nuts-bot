
class Messages:
    MESSAGE_ORDER = 'Заказ'
    MESSAGE_CATALOG = 'Каталог'
    MESSAGE_INFO = 'Общая информация'
    MESSAGE_CART = 'Корзина'
    MESSAGE_HISTORY = 'История заказов'
    MESSAGE_COMMENT = 'Отзыв или комментарий'
    MESSAGE_WRITE_ATEPAPT = 'Написать лично'


class Weights:
    WT90 = 90
    WT170 = 170
    WT500 = 500

    CHOICES = (
        (WT90, '90 грамм'),
        (WT170, '170 грамм'),
        (WT500, '500 грамм'),
    )