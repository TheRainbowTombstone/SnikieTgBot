from aiogram.dispatcher.filters.state import StatesGroup, State


class Load_task(StatesGroup):
    TextT = State()
    DeadlineT = State()