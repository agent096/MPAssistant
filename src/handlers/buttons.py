from aiogram import types, Router
from aiogram.filters import CommandStart
from src.keyboards import kb_menu
from aiogram.filters import Command, StateFilter
from aiogram import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from fsm import MathInput
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot
from src.config import settings
from aiogram.fsm.state import StatesGroup, State


bot = Bot(settings.bot_token)
router = Router()
storage = MemoryStorage()
dp = Dispatcher() #, storage=storage

#----------------------------------------------------------------------------------------------------

@router.message(StateFilter(None), Command('cost_price'))
async def cost_price(call: types.CallbackQuery, state: FSMContext):
    await call.answer(
        text="Введи закупучную стоимость товара в рублях:")
    await state.set_state(MathInput.num1)


@router.message(MathInput.num1)
async def get_num1(message: types.Message, state: FSMContext):
    await state.update_data(chosen_num1=message.text.lower())
    await message.answer(
        text="Введи стоимость доставки на одну штуку в рублях:")
    await state.set_state(MathInput.num2)


@router.message(MathInput.num2)
async def get_num6(message: types.Message, state: FSMContext):
    await state.update_data(chosen_num6=message.text.lower())
    await message.answer(
        text="Введи стоимость упаковки одной штуки в рублях:")
    await state.set_state(MathInput.num9)


@router.message(MathInput.num9)
async def get_num7(message: types.Message, state: FSMContext):
    await state.update_data(chosen_num7=message.text.lower())
    await message.answer(
        text="Введи стоимость работ по упаковке на одну штуку:")
    await state.set_state(MathInput.num11)


@router.message(MathInput.num11)
async def food_size_chosen(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(
        text=f"Себестоимость товара равна: {float(message.text.lower()) + float(user_data['chosen_num1']) + float(user_data['chosen_num6']) + float(user_data['chosen_num7'])} рублей.  \n"
    )
    await state.clear()

#----------------------------------------------------------------------------------------------------

@router.message(Command('financial_strength'))
async def financial_strength(call: types.CallbackQuery, state: FSMContext):
    await call.answer(
        text="Введи выручку в рублях:")
    await state.set_state(MathInput.num3)


@router.message(MathInput.num3)
async def get_num2(message: types.Message, state: FSMContext):
    await state.update_data(chosen_num2=message.text.lower())
    await message.answer(
        text="Введите точку безубыточности в рублях:")
    await state.set_state(MathInput.num4)


@router.message(MathInput.num4)
async def food_size_chosen(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(
        text=f"Запас финансовой прочности равен: {(float(message.text.lower()) - float(user_data['chosen_num2'])) / float(message.text.lower())}%.\n"
    )
    await state.clear()

#----------------------------------------------------------------------------------------------------
#постоянные затраты / (выручка-переменные затраты)
@router.message(Command('breakeven_point'))
async def Fixed_cost(call: types.CallbackQuery, state: FSMContext):
    await call.answer(
        text="Введи выручку за период в рублях:")
    await state.set_state(MathInput.num5)


@router.message(MathInput.num5)
async def revenue(message: types.Message, state: FSMContext):
    await state.update_data(revenue=message.text.lower())
    await message.answer(
        text="Введи переменные расходы с еденицы товара в рублях:")
    await state.set_state(MathInput.num6)


@router.message(MathInput.num6)
async def Variable_cost(message: types.Message, state: FSMContext):
    await state.update_data(Variable_cost=message.text.lower())
    await message.answer(
        text="Введи постоянные расходы на единицу товара в рублях:")
    await state.set_state(MathInput.num8)


@router.message(MathInput.num8)
async def breakeven_point(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(
        text=f"Точка безубыточности равна: {float(message.text.lower()) / (float(user_data['revenue']) - float(user_data['Variable_cost']))} штук.\n"
    )
    await state.clear()