from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from tgbot.keyboards.reply import menu, add_task_categories_menu, view_task_categories_menu, period_task_menu


async def show_menu(message: Message):
    await message.answer("Что вы хотите сделать?", reply_markup=menu)

async def categories_task(message: Message):
    if message.text == "Добавить задачу":
        await message.answer("К какой категории относится эта задача?", reply_markup=add_task_categories_menu)
    if message.text == "Посмотреть задачу":
        await message.answer("К какой категории относится эта задача?", reply_markup=view_task_categories_menu)


def register_menu(dp: Dispatcher):
    dp.register_message_handler(show_menu, commands=["start"], state="*")

def register_adding_task(dp: Dispatcher):
    dp.register_message_handler(categories_task, Text(equals=["Добавить задачу", "Посмотреть задачу"]), state="*")
