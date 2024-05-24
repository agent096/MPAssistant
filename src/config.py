import os
from dotenv import load_dotenv

load_dotenv(".env")


class Settings:
    bot_token: str = os.getenv("BOT_TOKEN")

    card_size: int = 8


settings = Settings()