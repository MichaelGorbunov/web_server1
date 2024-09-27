import os
from dotenv import load_dotenv
#
# from aiogram import Bot, Dispatcher, executor, types
#
#

#
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command


load_dotenv()

API_TOKEN = os.getenv('BOT_TOKEN')

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=API_TOKEN)
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Start!")
@dp.message(Command("hi"))
async def cmd_start(message: types.Message):
    await message.answer("Hi!")

@dp.message() #Создаём новое событие, которое запускается в ответ на любой текст, введённый пользователем.
async def echo(message: types.Message): #Создаём функцию с простой задачей — отправить обратно тот же текст, что ввёл пользователь.
   await message.answer(message.text)




# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())