from gpiozero import Button
import asyncio
import telegram
from telegram.ext import Updater, CommandHandler, CallbackContext
from time import localtime, strftime, sleep

tokenfile = ""
channel = ""
kytkin = Button(23)

with open(tokenfile, 'r') as file:
    token = file.readline().strip()

def print_help(update: telegram.Update, context: CallbackContext):
    update.message.reply_text("/help - print this message\n/iltaa - show the clubroom door status")

def status(update: telegram.Update, context: CallbackContext):
    global kytkin

    if kytkin.is_pressed:
        update.message.reply_text("Spinni is closed.")
    else:
        update.message.reply_text("Spinni is open!")

async def remove(msg_id):
    global token
    bot = telegram.Bot(token)
    global channel

    try:
        bot.delete_message(channel, msg_id)
    except telegram.error.NetworkError:
        pass

async def send(status):
    global token
    bot = telegram.Bot(token)
    global channel

    if status:
        door_status = "closed."
    else:
        door_status = "open!"
    
    timestamp = f"\n({strftime('%F %R', localtime())})"
    message = f"Spinni is {door_status}{timestamp}"
    
    try:
        sent_message = bot.send_message(channel, message)
        message_id = sent_message.message_id
        return message_id
    except telegram.error.NetworkError:
        pass
    

def main():
    global token
    
    global kytkin
    message_id = None
    edellinen_tila = kytkin.is_pressed
    edellinen_id = None
    updater = telegram.ext.Updater(token)
    
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("help", print_help))
    dispatcher.add_handler(CommandHandler("iltaa", status))
    updater.start_polling()
    
    while True:
        nykyinen_tila = kytkin.is_pressed
        if nykyinen_tila != edellinen_tila:
        
            if not edellinen_id == message_id:
                asyncio.run(remove(message_id))
                edellinen_id = message_id
                sleep(0.1)

            message_id = asyncio.run(send(nykyinen_tila))
            edellinen_tila = nykyinen_tila
        
        sleep(0.9)
        

if __name__ == "__main__":
    main()
