import asyncio
import sqlite3
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message, CallbackQuery, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command, Text
from aiogram.utils import i18n
logging.basicConfig(level=logging.INFO)
dp = Dispatcher()
sub_variants_buttons=[
    [
        InlineKeyboardButton(text="🔶 1 МЕСЯЦ", callback_data="sub_one"),
        InlineKeyboardButton(text="🔶 3 МЕСЯЦА | -15% ВЫГОДА", callback_data="sub_three")
    ],
]
sub_payments_buttons=[
    [
        InlineKeyboardButton(text="Оплатить через Boosty(Paypal / Банк)", callback_data="sub_boosty")
    ],
    [
        InlineKeyboardButton(text="Оплатить через Сбербанк", callback_data="sub_sber")
    ],
    [
        InlineKeyboardButton(text="🔙 Назад", callback_data="sub_back")
    ]
]
async def main():
    await dp.start_polling(Bot(token="6235859658:AAFR03q1rqvZDfUtUJfvSvkmLEtzcEDyrro"))
async def update_message(message: Message, new_value: str, keyboards: list):
    await message.edit_text(new_value, reply_markup=InlineKeyboardMarkup(inline_keyboard=keyboards))
@dp.message(Text("🛒 Тарифы"))
async def pay_subscribe(message: Message):
    await message.answer("Выберите желаемый тарифный план:", reply_markup=InlineKeyboardMarkup(inline_keyboard=sub_variants_buttons))
@dp.callback_query(Text(startswith="sub_"))
async def callback_analys(callback: CallbackQuery):
    action=callback.data.split("_")[1]
    if action=="one":
        await update_message(callback.message, "🔸 1 MONTH\nЦена: 10 USD\nСрок подписки: 30 дней\nВы получите приглашение в канал/чат 👇\n all 4 designer | a4d (private)", sub_payments_buttons)
    elif action=="three":
        await update_message(callback.message, "🔸 3 MONTH\nЦена: 30 USD 25 USD\nСрок подписки: 90 дней\nВы получите приглашение в канал/чат 👇\n all 4 designer | a4d (private)", sub_payments_buttons)
    elif action=="back":
        await update_message(callback.message, "Выберите желаемы тарифный план:", sub_variants_buttons)
@dp.message(Command("start"))
async def intro(message: Message):
    main_buttons=ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🛒 Тарифы")  
            ],
        ],
        resize_keyboard=True,
        input_field_placeholder="all 4 designer subsribe"
    )
    await message.answer(f"👋  Привет, {message.from_user.first_name}\n  \n   Приватный канал включает в себя все то, что опубликовано в демо канале — @all4designer_private. Это только экслюзивные и редкие материалы.\n \n  По вашим запросам мы можем находить нужные вам материалы в индивидуальном порядке или, если ваш ассет довольно востребованный - мы можем его купить.\n \n    Оплата происходит через сервис Boosty. Это аналог сервиса Patreon. Это единственный и самый дешевый способ перевода средств из-за рубежа в РФ. Этот сервис абсолютно безопасный. К сожалению, из-за санкций в моей стране невозможно принимать платежи из-за границы напрямую (Paypal, Revolut и тому подобные), поэтому использую только этот сервис для международных платежей. Если у вас не получается оплатить этим способом, то я помогу найти другой способ.\n \n    После успешной оплаты  будет отправлена пригласительная ссылка в приватный канал, где у вас будет безграничный доступ ко всем ресурсам.", reply_markup=main_buttons)
    await pay_subscribe(message)
if __name__=="__main__":
    asyncio.run(main())