from aiogram.fsm.state import State, StatesGroup


class Registration(StatesGroup):
    first_name = State()
    last_name = State()


class GetData(StatesGroup):
    location = State()
    lon = State()
    lat = State()
    day = State()
    photo = State()
    last = State()


class WeatherData(StatesGroup):
    location = State()
    lon = State()
    lat = State()
