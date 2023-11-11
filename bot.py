from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN, ADMIN, dp, bot
import main_handlers
# import logging
# logging.basicConfig(level=logging.INFO)


async def send_to_admin(dp):
    await bot.send_message(chat_id=ADMIN, text="Bot ishga tushdi")
    commands = [
            types.BotCommand(command="/start", description="Botni ishga tushurish"),
            types.BotCommand(command="/help", description="Yordam"),
        ]
    await bot.set_my_commands(commands)



if __name__ == '__main__':
    # executor.start_polling(dp, on_startup=send_to_admin)
    executor.start_polling(dp, skip_updates=True, on_startup=send_to_admin)
    