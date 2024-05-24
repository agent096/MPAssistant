import asyncio
import logging

from aiogram import Bot, Dispatcher

from src.config import settings
from src.handlers import routers


async def main():
    logging.basicConfig(level="INFO")

    bot = Bot(settings.bot_token)
    dp = Dispatcher()

    dp.include_routers(*routers)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())