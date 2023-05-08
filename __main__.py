import asyncio
import sqlite3
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message, User, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command, Text
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils import i18n
logging.basicConfig(level=logging.INFO)
dp = Dispatcher()
async def main():
    await dp.start_polling(Bot(token="6235859658:AAFR03q1rqvZDfUtUJfvSvkmLEtzcEDyrro"))
@dp.message(Command("start"))
async def intro(message: Message):
    main_buttons=ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📊 Моя подписка"),
                KeyboardButton(text="🛒 Тарифы")  
            ],
        ],
        resize_keyboard=True,
        input_field_placeholder="all 4 designer subsribe"
    )
    await message.answer(f"👋  Привет, {message.from_user.first_name}\n  \n   Приватный канал включает в себя все то, что опубликовано в демо канале — @all4designer_private. Это только экслюзивные и редкие материалы.\n \n  По вашим запросам мы можем находить нужные вам материалы в индивидуальном порядке или, если ваш ассет довольно востребованный - мы можем его купить.\n \n    Оплата происходит через сервис Boosty. Это аналог сервиса Patreon. Это единственный и самый дешевый способ перевода средств из-за рубежа в РФ. Этот сервис абсолютно безопасный. К сожалению, из-за санкций в моей стране невозможно принимать платежи из-за границы напрямую (Paypal, Revolut и тому подобные), поэтому использую только этот сервис для международных платежей. Если у вас не получается оплатить этим способом, то я помогу найти другой способ.\n \n    После успешной оплаты  будет отправлена пригласительная ссылка в приватный канал, где у вас будет безграничный доступ ко всем ресурсам.", reply_markup=main_buttons)
    sub_variants_buttons=[
        [
            InlineKeyboardButton(text="🔶 1 МЕСЯЦ", callback_data="one_month"),
            InlineKeyboardButton(text="🔶 3 МЕСЯЦА | -15% ВЫГОДА", callback_data="three_month")
        ],
    ]
    await message.answer("Выберите желаемый тарифный план:", reply_markup=InlineKeyboardMarkup(inline_keyboard=sub_variants_buttons))
if __name__=="__main__":
    asyncio.run(main())