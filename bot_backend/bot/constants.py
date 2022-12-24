
class Messages:
    ORDER = 'Заказ'
    CATALOG = 'Каталог'
    INFO = 'Общая информация'
    CART = 'Корзина'
    HISTORY = 'История заказов'
    COMMENT = 'Отзыв или комментарий'
    WRITE_ATEPAPT = 'Написать лично'
    
    DICT = dict((
        (ORDER, ORDER),
        (CATALOG, CATALOG),
        (INFO, INFO),
        (CART, CART),
        (HISTORY, HISTORY),
        (COMMENT, COMMENT),
        (WRITE_ATEPAPT, WRITE_ATEPAPT),
    ))


class Weights:
    WT90 = 90
    WT170 = 170
    WT500 = 500

    CHOICES = (
        (WT90, '90 грамм'),
        (WT170, '170 грамм'),
        (WT500, '500 грамм'),
    )