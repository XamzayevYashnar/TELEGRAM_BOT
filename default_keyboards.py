from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phone_bitton = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📞 Telefon raqamni junatish", request_contact=True),]
    ],
    resize_keyboard=True
)