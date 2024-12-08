from aiogram import Bot, Dispatcher
from config import TELEGRAM_API_TOKEN


class TelegramBot:
    def __init__(self):
        API_TOKEN = TELEGRAM_API_TOKEN
        if not API_TOKEN:
            raise ValueError("TELEGRAM_API_TOKEN is not set in the environment variables")

        self.bot = Bot(token=API_TOKEN)
        self.dp = Dispatcher()

    def register_feature_commands(self, register_function):
        register_function(self.dp)

    def get_dispatcher(self):
        return self.dp
