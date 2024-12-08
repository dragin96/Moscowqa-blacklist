import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI

from features.blacklist.infrastructure.web.api import router as blacklist_router
from infrastructure.telegram.bot import TelegramBot
from features.blacklist.telegram.commands import register_commands
from infrastructure.database.session import Base, engine, SessionLocal
from features.blacklist.infrastructure.database.repositories import SQLAlchemyBlacklistRepository
from features.blacklist.domain.services import BlacklistService
from aiogram import Router

Base.metadata.create_all(bind=engine)

# Контекстный менеджер для управления жизненным циклом приложения
@asynccontextmanager
async def lifespan(app: FastAPI):
    telegram_bot = TelegramBot()
    dp = telegram_bot.get_dispatcher()

    # Инициализация сервисов
    session = SessionLocal()
    repository = SQLAlchemyBlacklistRepository(session)
    blacklist_service = BlacklistService(repository)

    # Регистрация команд
    router = Router()
    register_commands(router, blacklist_service)
    dp.include_router(router)

    # Запуск Telegram-бота
    bot_task = asyncio.create_task(dp.start_polling(telegram_bot.bot))

    yield  # Здесь приложение FastAPI будет доступно для запросов

    # Завершение работы бота
    bot_task.cancel()
    try:
        await bot_task
    except asyncio.CancelledError:
        pass

    # Закрытие ресурсов
    await session.close()

# FastAPI приложение
app = FastAPI(lifespan=lifespan)
app.include_router(blacklist_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
