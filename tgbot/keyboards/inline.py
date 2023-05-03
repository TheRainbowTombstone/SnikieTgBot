from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.keyboards.callback_datas import *

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Добавить задачу", callback_data=branch_callback.new(action="add")),
            InlineKeyboardButton(text="Посмотреть задачу", callback_data=branch_callback.new(action="view"))
        ]
    ]
)

add_task_categories_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Дом", callback_data=category_callback.new(action="add", category="home")),
            InlineKeyboardButton(text="Работа", callback_data=category_callback.new(action="add", category="work"))
        ],
        [
            InlineKeyboardButton(text="Учёба", callback_data=category_callback.new(action="add", category="study")),
            InlineKeyboardButton(text="Родители", callback_data=category_callback.new(action="add", category="parents"))
        ],
        [
            InlineKeyboardButton(text="Личная жизнь", callback_data=category_callback.new(action="add", category="pri_live")),
            InlineKeyboardButton(text="Друзья", callback_data=category_callback.new(action="add", category="friends"))
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data=category_callback.new(action="add", category="back"))
        ]
    ]
)
