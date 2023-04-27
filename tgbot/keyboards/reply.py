from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Добавить задачу")
        ],
        [

            KeyboardButton(text="Посмотреть задачу")
        ]
    ],
    resize_keyboard=True
)

types_task_menu = ReplyKeyboardMarkup(
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
        ]
    ],
    resize_keyboard=True
)
