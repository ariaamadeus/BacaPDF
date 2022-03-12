import time

import telebot

from Responses import TELE_HI_GREET, TELE_CLASS_CODE
import BacaPdf as pdf
import csvHandler as csvH

with open('API_KEY.txt') as API_KEY:
    bot = telebot.TeleBot(API_KEY.read()[:-1])

#Message type check
#ClassCode, TimeInterval, Status, Feedback
messageBool = [False, False, False, False] 

def Echooo(themessage):
    for ID in csvH.AllID():
        bot.send_message(ID, themessage)

def Greet(message):
    print(message.text)
    if (message.text).lower() in TELE_HI_GREET:
        return True
    return False

def ClassCode(message):
    if (message.text).lower() in TELE_CLASS_CODE:
        return True
    return False

def TimeInterval(message):
    message = (message.text).lower()
    if message.isdigit():
        return True
    return False

def feedbackCatch(message):
    if messageBool[3]:
        return True
    return False

#Commands
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,"HEY! Welcome to bot Ukrida")
    if csvH.checkID(message.chat.id) == 0:
        classCom(message,True)
        csvH.newID(message.chat.id,
                message.chat.first_name,
                message.chat.username,
                "1PEEA", 10, 'active')

@bot.message_handler(commands=['classcode'])
def classCom(message, first = False):
    global messageBool
    messageBool = [True, False, False, False]
    if first:
        bot.send_message(message.chat.id, "Ketik kode kelasmu,\n(Contoh 1Peea):")
    else:
        bot.send_message(message.chat.id, "Ketik kode kelasmu, atau /cancel untuk membatalkan\n(Contoh 1Peea):")

@bot.message_handler(commands=['cancel'])
def cancelCom(message):
    global messageBool
    for x in messageBool:
        if x:
            messageBool = [False, False, False, False]
            bot.send_message(message.chat.id, "OK :)") 
            return

@bot.message_handler(commands=['feedback'])
def feedbackCom(message):
    global messageBool
    messageBool = [False, False, False, True]
    bot.send_message(message.chat.id, "Feedback, atau laporan error:")

@bot.message_handler(commands=['schedules'])
def schedulesCom(message,classCode=0):
    if classCode == 0:
        classCode = csvH.checkClass(message.chat.id)
    queryClass = pdf.openFile(classCode)
    if len(queryClass) > 0:
        for kelas in queryClass:
            sendTo = "Matkul: "+kelas[0]+"\n"
            sendTo += "Waktu: "+kelas[1]+", "+kelas[2]+kelas[3]+"\n"
            sendTo += "Dosen: "+kelas[4]+"\n"
            if kelas[5] == "PTM":
                sendTo += "Room:" + kelas[5]
            elif kelas[5] == "Meet":
                sendTo += "Room:" +'G'+ kelas[5]
            else:#angka
                sendTo += "MeetID: "+kelas[5]+"\n"
                sendTo += "Pass: "+kelas[6]
            bot.send_message(message.chat.id, sendTo) 
        bot.send_message(message.chat.id, "Selamat Kuliah!")
    else:
        bot.send_message(message.chat.id, "Maaf, kode kelas "+classCode.upper()+" belum ada di list.")

@bot.message_handler(commands=['timer', 'help'])
def notyetCom(message):
    bot.send_message(message.chat.id, "Under Construction")

#Commands Child
@bot.message_handler(func=Greet)
def GreetCH(message):
    bot.send_message(message.chat.id, "Halo "+message.chat.first_name+" :)")
    
@bot.message_handler(func=feedbackCatch)
def GreetCH(message):
    with open('feedback.txt','a') as f:
        f.write(message.text)
    #bot.send_message(895523970, str(message.chat.first_name)+":"+message.text)
    bot.send_message(message.chat.id, "Pesan terkirim :)")

@bot.message_handler(func=ClassCode)
def ClassCH(message):
    if messageBool[0]:
        bot.send_message(message.chat.id, "OK, kelasmu tercatat: "+(message.text).upper())
        schedulesCom(message,message.text)
        csvH.changeClass(csvH.checkID(message.chat.id), (message.text).upper())
        messageBool[0] = False
    else:
        bot.send_message(message.chat.id, "Ketik /classcode untuk mengganti kode kelas, atau /schedules untuk melihat jadwal kelasmu")

if __name__ == "__main__":
    Echooo("Hi! Server On 7-12 Maret 2022")
#     bot.infinity_polling()
#     time.sleep(2)
