from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery
from aiogram.utils.callback_data import CallbackData

from tgbot import database
from tgbot.database import Task, DBComands
from tgbot.filters.states import Load_task
from tgbot.keyboards.inline import menu, add_task_categories_menu, view_task_categories_menu, period_task_menu

db = database.DBComands()

async def show_menu(message: Message):
    await message.answer("Что вы хотите сделать?", reply_markup=menu)

async def back_show_menu(call: CallbackQuery):
    await call.message.edit_text("Что вы хотите сделать?")
    await call.message.edit_reply_markup(reply_markup=menu)

async def add_categories_task(call: CallbackQuery):
    await call.message.edit_text("К какой категории относится эта задача?")
    await call.message.edit_reply_markup(reply_markup=add_task_categories_menu)

async def adding_task(call: CallbackQuery):
    await call.message.edit_text("Опишите вашу задачу!")

    await Load_task.TextT.set()

async def task_text(message: Message, state: FSMContext):
    task1 = message.text
    task = Task()
    task.task = task1
    await message.answer(f"Ваша задача: {task1}"
                         "\nУкажите дедлайн в формате (ДД/ММ/ГГ ЧЧ:ММ):")
    await Load_task.DeadlineT.set()
    await state.update_data(task = task)


async def task_deadline(message: Message, state: FSMContext):
    deadline = message.text

    data = await state.get_data()
    task: Task = data.get("task")
    deadline = message.text
    await task.create()

    await message.answer("Ваща задача добавлена.")
    await state.reset_state()



async def view_categories_task(call: CallbackQuery):
    await call.message.edit_text("К какой категории относится эта задача?")
    await call.message.edit_reply_markup(reply_markup=view_task_categories_menu)

async def viewing_task(call: CallbackQuery):
    await call.message.edit_text("За какой период вы хотите посмотреть задачи?")
    await call.message.edit_reply_markup(reply_markup=period_task_menu)

async def show_tasks(call: CallbackQuery):
    all_tasks = await database.Task.get()
    for _ in all_tasks:
        text = ("<b>Задача:</b> {task} \n"
                "<b>Дедлайн:</b> {deadline}")
        await call.message.answer(text)


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

def register_task_text(dp: Dispatcher):
    dp.register_message_handler(task_text, state=Load_task.TextT)
def register_task_deadline(dp: Dispatcher):
    dp.register_message_handler(task_deadline, state=Load_task.DeadlineT)

def register_show_tasks(dp: Dispatcher):
    dp.register_callback_query_handler(show_tasks, text_contains=["yesday"], state="*")
    dp.register_callback_query_handler(show_tasks, text_contains=["aftom"], state="*")
    dp.register_callback_query_handler(show_tasks, text_contains=["date"], state="*")
    dp.register_callback_query_handler(show_tasks, text_contains=["thisweek"], state="*")
    dp.register_callback_query_handler(show_tasks, text_contains=["specweek"], state="*")
    dp.register_callback_query_handler(show_tasks, text_contains=["thismonth"], state="*")

    dp.register_callback_query_handler(view_categories_task, text_contains=["back"], state="*")


