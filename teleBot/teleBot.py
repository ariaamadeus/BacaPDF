import telebot

from teleResponses import TELE_HI_GREET, TELE_CLASS_CODE

with open('API_KEY.txt') as API_KEY:
    bot = telebot.TeleBot(API_KEY.read()[:-1])

#Message type check
def Greet(message):
    if (message.text).lower() in TELE_HI_GREET:
        return True
    return False

def TimeGreet(message):
    #if (message.text).lower() in TELE_HI_GREET:
    #    return True
    return False

def ClassCode(message):
    if (message.text).lower() in TELE_CLASS_CODE:
        return True
    return False

#Auto register
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,"Hey! Welcome to bot Ukrida")

@bot.message_handler(func=Greet)
def sendRespon(message):
    bot.send_message(message.chat.id, "Halo "+message.chat.first_name+" :)")

@bot.message_handler(func=ClassCode)
def sendRespon(message):
    bot.send_message(message.chat.id, "Oke, kelas "+(message.text).upper())

if __name__ == "__main__":
    bot.infinity_polling()
