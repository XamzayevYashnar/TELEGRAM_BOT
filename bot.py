from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from database import Database
import asyncio

API_TOKEN_BOT = "7790976582:AAGkgMonxvU7ZMdPGV0u3goB9ATn5Zn6vQU"
bot = Bot(token=API_TOKEN_BOT)
dp = Dispatcher()
db = Database()

@dp.message(Command("start"))
async def command_start(msg: Message):
    user_id = msg.from_user.id
    user = db.check_user(user_id)
    if user:
        await msg.answer("Malades ruyxatdan utgansan")
    else:
        await msg.answer("Siz ro'yxatdan o'tmagansiz iltimos /register orqali ro'yxatdan o'ting")

@dp.message(Command("register"))
async def register_handler(msg: Message):
    if db.check_user(msg.from_user.id):
        await msg.answer("Siz ro'yxatdan utgansiz")
    else:
        user_id = msg.from_user.id
        username = msg.from_user.username
        phone_number = msg.contact
        db.add_users(user_id, username, phone_number)
        await msg.answer("Malumotingiz muvaffaqiyatli ro'yxatdan o'tdi!")

async def main():
    print("🤖 Bot ishladi...")
    db.create_table()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())