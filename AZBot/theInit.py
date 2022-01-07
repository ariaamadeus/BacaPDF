import pandas as pd
from datetime import datetime, timedelta

from Responses import HARI_HARI, TELE_CLASS_CODE

jadwalDt = [[],[],[],[],[],[],[]]
jadwalCCode = [[[]],[[]],[[]],[[]],[[]],[[]],[[]]]

def iniTime(year,month,day):
    global jadwalDt, jadwalCCode
    #senin[0] -> minggu[6]
    jadwal = [[],[],[],[],[],[],[]]
    
    jamOn = False
    keywords = []
    buffCCode = ''
    Index = 0
    dateRange = pd.date_range(start=datetime(year,month,day), periods = 6).to_pydatetime().tolist()
    
    with open('keywords.txt','r') as textKey:
        word = ''
        for x in textKey.read():
            if (x == ' ')or(x == '\n'):
                keywords.append(word)
                word = ''
            else:
                word += x
                
    for word in keywords:
        if word.casefold() in TELE_CLASS_CODE:
            buffCCode = word
        if word.casefold() in HARI_HARI:
            IndexHari = HARI_HARI.index(word.casefold())
            jamOn = True
            continue
        
        if jamOn:
            if word in ['s/d','Tanggal','tgl']:
                jamOn = False
                continue
            
            if word not in jadwal[IndexHari]:
                jadwal[IndexHari].append(word)
            
            IndexWaktu = jadwal[IndexHari].index(word)
            if len(jadwalCCode[IndexHari][IndexWaktu]) == 0:
                jadwalCCode[IndexHari].append([])
            jadwalCCode[IndexHari][IndexWaktu].append(buffCCode)
            
            jamOn = False
            
    for HARI in jadwal:
        Index = jadwal.index(HARI)
        for WAKTU in HARI:
            if WAKTU:
                jam, menit, detik = WAKTU.split(':')
                tahun, bulan, hari = dateRange[Index].strftime('%Y:%m:%d').split(':')
                jadwalDt[Index].append(datetime(int(tahun),int(bulan),int(hari),int(jam),int(menit),int(detik)))
            
    #return jadwalDt, jadwalCCode

def nexTime(jadwal, interval=0):
    for HARI in jadwal:
        for WAKTU in HARI:
            if WAKTU > datetime.now() + timedelta(minutes=interval) + timedelta(hours=7):
                return WAKTU, jadwal.index(HARI), HARI.index(WAKTU)
            
if __name__ == "__main__":
    #print(int(pd.date_range(start=datetime.now(), periods = 6).to_pydatetime().tolist()[0].strftime('%Y:%m:%d').split(':')[2]))
    iniTime(2022,1,3)
    print(jadwalDt)
            
            
