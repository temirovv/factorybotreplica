from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from data.config import SOCIALS, SOCIAL_NAMES


async def get_socials():
    builder = InlineKeyboardBuilder()
    all_in_one = [(SOCIAL_NAMES[i], SOCIALS[i]) for i in range(len(SOCIALS))]
    for name, social in all_in_one:
        builder.button(text=name, url=social)

    menu = InlineKeyboardMarkup(inline_keyboard=[])
    builder.attach(InlineKeyboardBuilder.from_markup(menu))
    builder.adjust(1)
    return builder
