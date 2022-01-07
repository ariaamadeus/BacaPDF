import time

import telebot
import BacaPdf as pdf
from Responses import HARI_HARI,DAY_DAY

with open('API_KEY.txt') as API_KEY:
    bot = telebot.TeleBot(API_KEY.read()[:-1])

def schedulesClock(ID, classCode, Hari, Waktu):
    queryClass = pdf.openFile(classCode)
    if len(queryClass) > 0:
        for kelas in queryClass:
            if HARI_HARI[DAY_DAY.index(Hari)] == kelas[1].casefold() and Waktu == kelas[2]:
                sendTo = "Matkul: "+kelas[0]+"\n"
                sendTo += "Waktu: "+kelas[1]+", "+kelas[2]+kelas[3]+"\n"
                sendTo += "Dosen: "+kelas[4]+"\n"
                try:
                    sendTo += "MeetID: "+kelas[5]+"\n"
                    sendTo += "Pass: "+kelas[6]
                except:
                    sendTo += "MeetID: Google Meet"
                bot.send_message(int(ID), sendTo) 
        bot.send_message(int(ID), "Semangat Kuliah!")
    else:
        bot.send_message(int(ID), "Maaf, kode kelas "+classCode.upper()+" belum ada di list.")

if __name__ == "__main__":
    bot.infinity_polling()