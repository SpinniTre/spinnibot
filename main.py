from unittest.mock import MagicMock
from gpiozero import Button
import telegram
from telegram.ext import Application, CommandHandler, CallbackContext
from telegram.ext import ContextTypes
from time import localtime, strftime, sleep

APP_VERSION = "0.0.1"

tokenfile = "tg_token.dev.txt"
channel = ""
kytkin =  MagicMock() #Button(23)
kytkin.is_pressed = False




def get_bot_token() -> str:
    
    # TODO: use environment variable
    def get_token_file_name() -> str:
        return "tg_token.dev.txt"
    
    with open(get_token_file_name(), 'r') as file:
        token = file.readline().strip()
        if not token:
            raise ValueError("Token was read but is empty")
        return token



async def door_open(ctx: ContextTypes.DEFAULT_TYPE):
    await ctx.bot.send_message(-1003404217068, "aaaaa")


async def cmd_help(update: telegram.Update, ctx: CallbackContext) -> None:
    print("help command called")
    await update.message.reply_text("/help - print this message\n/iltaa - show the clubroom door status")


async def cmd_status(update: telegram.Update, context: CallbackContext):
    global kytkin

    if kytkin.is_pressed:
        await update.message.reply_text("Spinni is closed.")
    else:
        await update.message.reply_text("Spinni is open!")

    

def main():

    token: str = get_bot_token()

    COMMANDS = (
        CommandHandler("help", cmd_help),
        CommandHandler("iltaa", cmd_status)
    )

    app = Application.builder().token(token).build()
    print(f"Bot initialized")


    for cmd_handler in COMMANDS:
        print(f"Adding command handler: {cmd_handler}")
        app.add_handler(cmd_handler)

    app.job_queue.run_repeating(door_open, first=1, interval=10, last=30)
    

    print("Running...")
    app.run_polling()
        

if __name__ == "__main__":
    main()
