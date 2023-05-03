from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from tgbot.keyboards.inline import menu, add_task_categories_menu


async def show_menu(message: Message):
    await message.answer("Что вы хотите сделать?", reply_markup=menu)

async def categories_task(call: CallbackQuery):
    await call.message.edit_text("К какой категории относится эта задача?")
    await call.message.edit_reply_markup(reply_markup=add_task_categories_menu)


def register_menu(dp: Dispatcher):
    dp.register_message_handler(show_menu, commands=["start"], state="*")

def register_adding_task(dp: Dispatcher):
    dp.register_callback_query_handler(categories_task, text_contains = "add", state="*")


