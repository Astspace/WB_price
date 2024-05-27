from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import Router

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Приветик, любимая секретарша!')
    await message.reply('Как дела твои?')
