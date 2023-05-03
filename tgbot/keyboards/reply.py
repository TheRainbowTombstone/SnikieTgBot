from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

view_task_categories_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Дом")
        ],
        [
            KeyboardButton(text="Работа")
        ],
        [
            KeyboardButton(text="Учёба")
        ],
        [
            KeyboardButton(text="Родители")
        ],
        [
            KeyboardButton(text="Личная жизнь")
        ],
        [
            KeyboardButton(text="Друзья")
        ],
        [
            KeyboardButton(text="Посмотреть все задачи")
        ]
    ],
    resize_keyboard=True
)

period_task_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Завтра")
        ],
        [
            KeyboardButton(text="Послезавтра")
        ],
        [
            KeyboardButton(text="Конкретная дата")
        ],
        [
            KeyboardButton(text="Ближайшая неделя")
        ],
        [
            KeyboardButton(text="Конкретная неделя")
        ],
        [
            KeyboardButton(text="Ближайший месяц")
        ]
    ],
    resize_keyboard=True
)
