from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/cost_price 📋'), #СЕБЕСТОИМОСТЬ
        ],
        [
            KeyboardButton(text='/breakeven_point 📌'),  # ТОЧКА БЕЗУБЫТОЧНОСТИ
        ],
        [
            KeyboardButton(text='/financial_strength 📊'), #ФИН. ПРОЧНОСТЬ
        ]
    ],
    resize_keyboard=True
)

#Рассчёт себестоимости