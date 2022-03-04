import time
from datetime import datetime, timedelta

from theInit import *
import csvHandler as csvH

nextJadwal, indexHari, indexWaktu, classCodes = (0,0,0,0)
once, changeJadwal = (True, False)

def begin(tahun, bulan, hari):
    iniTime(tahun, bulan, hari)

def checkNext(tahun, bulan, hari):
    global nextJadwal, indexHari, indexWaktu, classCodes
    nextJadwal, indexHari, indexWaktu = nexTime(jadwalDt)
    classCodes = jadwalCCode[indexHari][indexWaktu]

def checkForSend(tahun, bulan, hari, interval = 10):
    global changeJadwal, once
    earlyDelay = nextJadwal - timedelta(minutes = interval)
    pastDelay = nextJadwal + timedelta(minutes = 15)
    if  pastDelay >= datetime.now() + timedelta(hours=7) >= earlyDelay:
        if once:
            print('all registered ID sent the schedule once')
            changeJadwal = True
            csvH.checkIDclock(classCodes,nextJadwal.strftime('%A'),nextJadwal.strftime('%H:%M'))
            once = False
    elif changeJadwal:
        checkNext(tahun, bulan, hari)
        changeJadwal = False
        once = True
        
    time.sleep(1)

if __name__ == "__main__":
    tanggal = (2022,1,10)
    checkNext(tahun, bulan, hari)
    while True:
        checkForSend(tahun, bulan, hari)
    
