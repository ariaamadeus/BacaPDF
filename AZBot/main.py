import threading
import time

from teleBot import *
from timeHandler import *
# from theInit import *
# 
# iniTime(2022,1,3)

def first():
    bot.infinity_polling()

def second():
    tahun, bulan, hari = (2022,1,10)
    begin(tahun, bulan, hari)
    checkNext(tahun, bulan, hari) #initialize
    while True:
        checkForSend(tahun, bulan, hari)

if __name__ == "__main__":
    t1 = threading.Thread(target = first)
    t2 = threading.Thread(target = second)
    
    t1.start()
    t2.start()
