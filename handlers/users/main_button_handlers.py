from loader import dp
from aiogram.types import Message
from magic_filter import F
from aiogram import Router
from keyboards.inline.books_inline_btns import get_books_inline_kb
from keyboards.inline.socials_btn import get_socials
router = Router()
dp.include_router(router)


@router.message(F.text == "📚 Kitoblar")
async def answer_for_books_btn(msg: Message):
    builder = await get_books_inline_kb()
    await msg.answer("Kategoriyalardan birini tanlang", reply_markup=builder.as_markup())


@router.message(F.text == '🔵 Biz ijtimoiy tarmoqlarda')
async def answer_socials_btn(msg: Message):
    builder = await get_socials()
    await msg.answer('Biz ijtimoiy tarmoqlarda', reply_markup=builder.as_markup())

