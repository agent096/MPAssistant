from aiogram import types, Router
from aiogram.filters import CommandStart
from src.keyboards import kb_menu
from aiogram.filters import Command
#from src.fsm import MathState

router = Router()




@router.message(CommandStart())
async def start(message: types.Message) -> None:
    await message.answer('''Привет! Я бот, который поможет тебе рассчитывать себестоимость, точку безубыточности и запас финансовой прочности!📈 
/menu сли хочешь начать расчёты!
/bot_commands если хочешь узнать все команды!
(Если число с дробью пиши через точку. Пример: 1.5)''')

@router.message(Command("menu"))
async def menu(message: types.Message):
    await message.answer('''Выбери нужный тебе расчёт:''', reply_markup=kb_menu)

@router.message(Command("bot_commands"))
async def menu(message: types.Message):
    await message.answer('''Все команды бота:
    /start - запустить бота ▶
    /menu - запуск интерактивного меню 💬
    /bot_commands - все команды бота 🔎
    /cost_price - рассчёт себестоимости бота 📋
    /breakeven_point - расчёт точки безубыточности 📌
    /financial_strength - расчёт финансовой прочности 📊''')

#@router.message() #state=MathState.user_answer
#async def check_answer(message: types.Message):
