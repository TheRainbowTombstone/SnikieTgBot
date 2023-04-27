from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from tgbot.keyboards.reply import menu, types_task_menu


async def show_menu(message: Message):
    await message.answer("Что вы хотите сделать?", reply_markup=menu)

async def add_task(message: Message):
    await message.answer("к каокой категории относится эта задача?", reply_markup=types_task_menu)


def register_menu(dp: Dispatcher):
    dp.register_message_handler(show_menu, commands=["start"], state="*")

def register_adding_task(dp: Dispatcher):
    dp.register_message_handler(add_task, Text(equals="Добавить задачу"), state="*")
