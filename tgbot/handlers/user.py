from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery

from tgbot.keyboards.inline import menu, add_task_categories_menu, view_task_categories_menu, period_task_menu


async def show_menu(message: Message):
    await message.answer("Что вы хотите сделать?", reply_markup=menu)

async def back_show_menu(call: CallbackQuery):
    await call.message.edit_text("Что вы хотите сделать?")
    await call.message.edit_reply_markup(reply_markup=menu)

async def add_categories_task(call: CallbackQuery):
    await call.message.edit_text("К какой категории относится эта задача?")
    await call.message.edit_reply_markup(reply_markup=add_task_categories_menu)

async def view_categories_task(call: CallbackQuery):
    await call.message.edit_text("К какой категории относится эта задача?")
    await call.message.edit_reply_markup(reply_markup=view_task_categories_menu)


async def adding_task(call: CallbackQuery):
    await call.message.answer("Опишите вашу задачу!")

async def viewing_task(call: CallbackQuery):
    await call.message.edit_text("За какой период вы хотите посмотреть задачи?")
    await call.message.edit_reply_markup(reply_markup=period_task_menu)





def register_menu(dp: Dispatcher):
    dp.register_message_handler(show_menu, commands=["start"], state="*")

def register_categories_task(dp: Dispatcher):
    dp.register_callback_query_handler(add_categories_task, Text(startswith="add"), state="*")
    dp.register_callback_query_handler(view_categories_task, Text(startswith="view"), state="*")


def register_adding_task(dp: Dispatcher):
    dp.register_callback_query_handler(adding_task, text_contains=["add", "home"], state="*")
    dp.register_callback_query_handler(adding_task, text_contains=["add", "work"], state="*")
    dp.register_callback_query_handler(adding_task, text_contains=["add", "study"], state="*")
    dp.register_callback_query_handler(adding_task, text_contains=["add", "parents"], state="*")
    dp.register_callback_query_handler(adding_task, text_contains=["add", "friends"], state="*")
    dp.register_callback_query_handler(adding_task, text_contains=["add", "pri_live"], state="*")
    dp.register_callback_query_handler(back_show_menu, text_contains=["add", "back"], state="*")


def register_viewing_task(dp: Dispatcher):
    dp.register_callback_query_handler(viewing_task, text_contains=["view", "home"], state="*")
    dp.register_callback_query_handler(viewing_task, text_contains=["view", "work"], state="*")
    dp.register_callback_query_handler(viewing_task, text_contains=["view", "study"], state="*")
    dp.register_callback_query_handler(viewing_task, text_contains=["view", "parents"], state="*")
    dp.register_callback_query_handler(viewing_task, text_contains=["view", "friends"], state="*")
    dp.register_callback_query_handler(viewing_task, text_contains=["view", "pri_live"], state="*")
    dp.register_callback_query_handler(viewing_task, text_contains=["view", "etc"], state="*")
    dp.register_callback_query_handler(back_show_menu, text_contains=["view", "back"], state="*")


