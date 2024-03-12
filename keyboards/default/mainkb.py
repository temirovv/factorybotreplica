from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def get_main_kb():
    menu = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [KeyboardButton(text='📚 Kitoblar')],
            [KeyboardButton(text='📃 Mening buyurtmalarim')],
            [KeyboardButton(text='🔵 Biz ijtimoiy tarmoqlarda'),
             KeyboardButton(text='📞 Biz bilan bog\'lanish')],
        ]
    )

    return menu
