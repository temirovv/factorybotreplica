from loader import dp
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.default.mainkb import get_main_kb


@dp.message(CommandStart())
async def command_start_handler(msg: Message) -> None:
    await msg.answer(f"Assalomu alaykum! Tanlang.", reply_markup=await get_main_kb())


# @dp.message()
# async def echo_handler(message: Message) -> None:
#     try:
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         await message.answer("Nice try!")
