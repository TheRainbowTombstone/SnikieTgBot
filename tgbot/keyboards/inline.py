from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.keyboards.callback_datas import category_callback, showing_callback

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Добавить задачу", callback_data="add"),
            InlineKeyboardButton(text="Посмотреть задачу", callback_data="view")
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

view_task_categories_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Дом", callback_data=category_callback.new(action="view", category="home")),
            InlineKeyboardButton(text="Работа", callback_data=category_callback.new(action="view", category="work"))
        ],
        [
            InlineKeyboardButton(text="Учёба", callback_data=category_callback.new(action="view", category="study")),
            InlineKeyboardButton(text="Родители", callback_data=category_callback.new(action="view", category="parents"))
        ],
        [
            InlineKeyboardButton(text="Личная жизнь", callback_data=category_callback.new(action="view", category="pri_live")),
            InlineKeyboardButton(text="Друзья", callback_data=category_callback.new(action="view", category="friends"))
        ],
        [
            InlineKeyboardButton(text="Другое", callback_data=category_callback.new(action="view", category="etc")),
            InlineKeyboardButton(text="Назад", callback_data=category_callback.new(action="view", category="back"))
        ]
    ]
)

period_task_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Завтра", callback_data=showing_callback.new(date="yesday")),
            InlineKeyboardButton(text="Послезавтра", callback_data=showing_callback.new(date="aftom"))
        ],
        [
            InlineKeyboardButton(text="Конкретная дата", callback_data=showing_callback.new(date="date")),
            InlineKeyboardButton(text="Ближайшая неделя", callback_data=showing_callback.new(date="thisweek"))
        ],
        [
            InlineKeyboardButton(text="Конкретная неделя", callback_data=showing_callback.new(date="specweek")),
            InlineKeyboardButton(text="Ближайший месяц", callback_data=showing_callback.new(date="thismonth"))
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data=showing_callback.new(date="back"))
        ]
    ],
    resize_keyboard=True
)
