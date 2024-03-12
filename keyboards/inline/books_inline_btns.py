from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

book_categories = ['⚡️IKAR', '📚 Factor books kitoblari', 'Biznes kitoblar',
                   'Diniy kitoblar', '📚 Boshqa kitoblar', 'Psixologik kitoblar',
                   'Tarbiyaviy-oilaviy kitoblar', 'Turk badiiy-ma\'rifiy kitoblar', 'Badiiy Romanlar',
                   'Qissa va romanlar', 'Badiiy kitoblar va qissalar']


async def get_books_inline_kb():
    builder = InlineKeyboardBuilder()
    for book in book_categories:
        builder.button(text=book, callback_data=book)

    builder.button(text='🔍 Qidirish', switch_inline_query='', switch_inline_query_current_chat='')

    markup = InlineKeyboardMarkup(inline_keyboard=[])
    builder.attach(InlineKeyboardBuilder.from_markup(markup))
    builder.adjust(2)
    return builder
