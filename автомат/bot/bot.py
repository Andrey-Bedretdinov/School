import asyncio
from time import sleep
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from fastapi import FastAPI, Query

bot = Bot(token='5701039719:AAHp48PDSzjxcJnHDvEgUD-GxYHqpi24m6c')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler()
async def start(msg: types.Message):
    await bot.send_message(1471718311, 'Ку-ку')


async def push_message(message):
    await bot.send_message(1471718311, message)

app = FastAPI()

if __name__ == '__main__':
    # executor.start_polling(dp)
    pass
