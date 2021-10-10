import keyboard,click,time,sys,os
import pyautogui as pyg
import textract as txr
import datetime as dt
import logging as log
import tkinter as tk
import PyPDF2 as pdr


from pynput.mouse import Listener
from tkinter import filedialog

    
waktu = dt.datetime.now()
hari = waktu.strftime('%a')
if hari == "Mon":
    hari = "Senin"
elif hari == "Tue":
    hari = "Selasa"
elif hari == "Wed":
    hari = "Rabu"
elif hari == "Thu":
    hari = "Kamis"
elif hari == "Fri":
    hari = "Jumat"
elif hari == "Sat":
    hari = "Sabtu"
elif hari == "Sun":
    hari = "Minggu"
jam = waktu.strftime('%H')
menit = waktu.strftime('%M')

root = tk.Tk()
root.geometry("1400x300")
root.resizable(True,False)
formatter = log.Formatter('%(levelname)s:root:%(message)s')

label = tk.Label(text="1. Input kode kelas:")
label1 = tk.Label(text="3. Buka file")
label2 = tk.Label(text="4. Result:")
label3 = tk.Label(text="Prodi")
label4 = tk.Label(text="2. Input jumlah hal:")
label5 = tk.Label(text='')
label6 = tk.Label(text="Nama tampilan zoom:")
label7 = tk.Label(text="Upcoming Class: ",font='Helvetica 8 bold')

dengansks = True
jumhal_save = 0
count = 0
count1 = 0
pathzoom = ""
filepath = ""
filepath_save = ""
pathsearch = ""
for x in os.getcwd():
    if x == '\\':
        x = '/'
    pathsearch+=x

pathlogzoom=pathsearch+'/lib/1423/213153.log'
pathlogjadw=pathsearch+'/lib/1423/213114.log'
pathlogmpdf=pathsearch+'/lib/1423/213124.log'
pathlogkode=pathsearch+'/lib/1423/213134.log'
pathlogjumh=pathsearch+'/lib/1423/213144.log'
pathlognama=pathsearch+'/lib/1423/213154.log'
pathjoinyes=pathsearch+'/lib/5867/joinyes.png'
pathjoinpass=pathsearch+'/lib/5867/joinpass.png'
pathjoinmeet=pathsearch+'/lib/5867/joinmeet.png'
pathjoinnot=pathsearch+'/lib/5867/joinnot.png'
pathentermeet=pathsearch+'/lib/5867/entermeet.png'
pathenterpass=pathsearch+'/lib/5867/enterpass.png'
pathentername1=pathsearch+'/lib/5867/entername1.png'
pathentername2=pathsearch+'/lib/5867/entername2.png'
pathentername3=pathsearch+'/lib/5867/entername3.png'
pathconfirm1=pathsearch+'/lib/5867/confirm1.png'
pathconfirm2=pathsearch+'/lib/5867/confirm2.png'
pathconfirm3=pathsearch+'/lib/5867/confirm3.png'
pathconfirm4=pathsearch+'/lib/5867/confirm4.png'
pathconfirm5=pathsearch+'/lib/5867/confirm5.png'
pathmoveschedule=pathsearch+'/lib/5867/ifyes.png'

def setup_logger(name, log_file, level=log.INFO):
    handler = log.FileHandler(log_file)
    handler.setFormatter(formatter)
    
    logger = log.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    
    return logger
logzoom = setup_logger('213153', pathlogzoom)
logjadw = setup_logger('213114', pathlogjadw)
logmpdf = setup_logger('213124', pathlogmpdf)
logkode = setup_logger('213134', pathlogkode)
logjumh = setup_logger('213144', pathlogjumh)
lognama = setup_logger('213154', pathlognama)

with open (pathlogzoom) as Flie:
    for x in Flie:
        count += 1
        count1 = 0
        pathzoom = ''
        for y in x:
            if len(x)-1 > count1 > 9:
                pathzoom+=y
                count1+=1
            else:
                count1+=1
if count>0:
    print(pathzoom)
else:
    pass
count = 0
count1 = 0

keywords = []
stopper = ["akuntansi","informatika","manajemen","psikologi","sastra","sistem","teknik","google"]
tologlist = []

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def zoomchange():
    global pathzoom
    global pathlogzoom
    count = 0
    pathzoom = filedialog.askopenfilename()
    with open(pathlogzoom,'w'):
        pass
    logzoom.info(pathzoom)
    with open (pathlogzoom) as Flie:
        for x in Flie:
            count = 0
            pathzoom = ''
            for y in x:
                if len(x)-1 > count > 9:
                    pathzoom+=y
                    count+=1
                else:
                    count+=1
    if len(pathzoom) == 0:
        print('Zoom path not changed')
    else:
        print('Zoom path changed sucessfuly')
        print(pathzoom)

def openNew(yasef = False):
    global filepath
    global filepath_save
    global keywords
    global jumhal_save
    if yasef:
        pass
    else:
        filepath = filedialog.askopenfilename()
        with open(pathlogmpdf,'w'):
            pass
        logmpdf.info(filepath)
    if len(filepath) == 0:
        try:
            filepath = filepath_save
            print('No file selected')
        except:
            print('No file selected')
    else:
        keywords = []
        filepath_save = filepath
        pdfFileObj = open(filepath,'rb')
        pdfReader = pdr.PdfFileReader(pdfFileObj)
        num_pages = entry2.get()
        if len(num_pages)>0:
            if num_pages.isdigit():
                if int(num_pages) != jumhal_save:
                    num_pages = int(entry2.get())
                    jumhal_save = num_pages
                else:
                    num_pages = int(entry2.get())
            else:
                num_pages = 1
        else:
            num_pages = 1
        print("Processing "+str(num_pages)+" Pages")
        count = 0
        text = ''
        print(f"{bcolors.ENDC}")
        while count < num_pages:
            pageObj = pdfReader.getPage(count)
            count+=1
            print(str(count))
            if len(pageObj.extractText())>0:
                text+=pageObj.extractText()
        word = ''
        for x in text:
            if (x == ' ')or(x == '\n'):
                keywords.append(word)
                word = ''
            else:
                word += x
        
        openFile()
manualFlag = True
def join_meet():
    global time
    global manualFlag
    global pathzoom
    global pathlogjadw
    global pathlogzoom
    global hari
    global jam
    global menit
    count = 0
    meetid = ''
    passw = ''
    with open (pathlogzoom) as Flie:
        for x in Flie:
            count = 0
            pathzoom = ''
            for y in x:
                if len(x)-1 > count > 9:
                    pathzoom+=y
                    count+=1
                else:
                    count+=1
    if count == 0:
        zoomchange()
    matkul,hare,jamuu,menuu,jambis,menis,meetid,passw,indhare,indhari = checkjadw()
    if indhare > indhari:
        manualFlag = False
    elif indhare == indhari:
        if int(jamuu) > int(jam):
            manualFlag = False
        elif int(jamuu) == int(jam):
            if int(menuu) > int(menit):
                manualFlag = False
    count = 0
    count1 = 0
    nama = entry3.get()
    print('Matkul:',matkul)
    if len(nama) == 0:
        nama = "Ukrida"
    with open (pathlognama,'w'):
        pass
    lognama.info(nama)
    print('Checking Meet ID...')
    if len(meetid)<=4:
        print('Error: Meet ID not found... Using GMeet?')
        return
    print('Checking Passcode...')
    if len(meetid)<=4:
        print('Error: Passcode not found...')
        return
    print('Opening Zoom Meeting...')
    os.startfile(pathzoom)
    waittime = 60
    while True:
        tryyes = False
        while waittime>=0:#joinmeet
            join_btn = pyg.locateCenterOnScreen(pathjoinyes, grayscale=False )
            if join_btn!=None:
                pyg.moveTo(join_btn)
                pyg.click()
                tryyes = True
                break
            join_btn = pyg.locateCenterOnScreen(pathjoinnot,grayscale=False)
            if join_btn!=None:
                pyg.moveTo(join_btn)
                pyg.click()
                break
            print("Waiting Zoom... "+str(waittime)+'s')
            waittime-=1
            time.sleep(0.5)
        if waittime < 0:
            print('Error: Zoom not opened or join button not found')
            break
        waittime = 60
        while waittime>=0:#entermeetid
            meetentry = pyg.locateCenterOnScreen(pathentermeet, grayscale=False )
            if meetentry!=None:
                pyg.moveTo(meetentry)
                pyg.click()
                time.sleep(1)
                pyg.typewrite(str(meetid),interval=0)
                break
            if tryyes:
                meetentry = pyg.locateCenterOnScreen(pathmoveschedule, grayscale=False )
                if meetentry!=None:
                    pyg.moveTo(meetentry)
                    time.sleep(1)
                    print("Move")
                    tryyes = False
            print("Waiting Meet Entry... "+str(waittime)+'s')
            waittime-=1
            time.sleep(0.75)
        if waittime < 0:
            print('Error: Meet ID entry not found')
            break
        waittime = 30
        while waittime>=0:#entername
            nameentry = pyg.locateCenterOnScreen(pathentername1, grayscale=False )
            if nameentry!=None:
                pyg.moveTo(nameentry)
                pyg.click()
                time.sleep(1)
                pyg.hotkey('ctrl','a')
                pyg.keyDown('backspace')
                pyg.keyUp('backspace')
                pyg.typewrite(str(nama),interval=0)
                break
            nameentry = pyg.locateCenterOnScreen(pathentername2,grayscale=False)
            if nameentry!=None:
                pyg.moveTo(nameentry)
                pyg.click()
                time.sleep(1)
                pyg.hotkey('ctrl','a')
                pyg.keyDown('backspace')
                pyg.keyUp('backspace')
                pyg.typewrite(str(nama),interval=0)
                break
            nameentry = pyg.locateCenterOnScreen(pathentername1, grayscale=False)
            if nameentry!=None:
                pyg.moveTo(nameentry)
                pyg.click()
                time.sleep(1)
                pyg.hotkey('ctrl','a')
                pyg.keyDown('backspace')
                pyg.keyUp('backspace')
                pyg.typewrite(str(nama),interval=0)
                break
            nameentry = pyg.locateCenterOnScreen(pathentername3,grayscale=False)
            if nameentry!=None:
                pyg.moveTo(nameentry)
                pyg.click()
                time.sleep(1)
                pyg.hotkey('ctrl','a')
                pyg.keyDown('backspace')
                pyg.keyUp('backspace')
                pyg.typewrite(str(nama),interval=0)
                break
            print("Waiting Name Entry... "+str(waittime)+'s')
            waittime-=1
            time.sleep(0.25)
        if waittime < 0:
            print('Error: Name too long or not found')
            break
        waittime = 30
        while waittime>=0:#clickjoin
            joinbtn = pyg.locateCenterOnScreen(pathjoinmeet, grayscale=False)
            if joinbtn!=None:
                pyg.moveTo(joinbtn)
                pyg.click()
                break
            print("Waiting Button1... "+str(waittime)+'s')
            waittime-=1
            time.sleep(0.75)
        if waittime < 0:
            print('Error: Join button not found')
            break
        waittime = 60
        while waittime>=0:#enterpass
            passentry = pyg.locateCenterOnScreen(pathenterpass, grayscale=False)
            if passentry!=None:
                pyg.moveTo(passentry)
                pyg.click()
                time.sleep(1)
                pyg.typewrite(str(passw),interval=0)
                break
            print("Waiting Pass Entry... "+str(waittime)+'s')
            waittime-=1
            time.sleep(0.75)
        if waittime < 0:
            print('Error: Passcode entry not found')
            break
        waittime = 15
        while waittime>=0:#clickjoin
            joinbuttt = pyg.locateCenterOnScreen(pathjoinpass, grayscale=False)
            if joinbuttt!=None:
                pyg.moveTo(joinbuttt)
                pyg.click()
                time.sleep(1)
                break
            conf = pyg.locateCenterOnScreen(pathconfirm1, grayscale=False)
            if conf!=None:
                break
            conf = pyg.locateCenterOnScreen(pathconfirm2, grayscale=False)
            if conf!=None:
                break
            conf = pyg.locateCenterOnScreen(pathconfirm3, grayscale=False)
            if conf!=None:
                break
            conf = pyg.locateCenterOnScreen(pathconfirm4, grayscale=False)
            if conf!=None:
                break
            conf = pyg.locateCenterOnScreen(pathconfirm5, grayscale=False)
            if conf!=None:
                break
            print("Waiting Button2... "+str(waittime)+'r')
            waittime-=1
        if waittime < 0:
            print('Where is the button?')
            break
        print('Done!')
        break

flag = True
lastMatkul = 'a'
def clock():
    global flag
    global manualFlag
    global hari
    global jam
    global menit
    global lastMatkul
    waktu = dt.datetime.now()
    hari = waktu.strftime('%a')
    if hari == "Mon":
        hari = "Senin"
    elif hari == "Tue":
        hari = "Selasa"
    elif hari == "Wed":
        hari = "Rabu"
    elif hari == "Thu":
        hari = "Kamis"
    elif hari == "Fri":
        hari = "Jumat"
    elif hari == "Sat":
        hari = "Sabtu"
    elif hari == "Sun":
        hari = "Minggu"
    tanggal = waktu.strftime('%d')
    bulan = waktu.strftime('%m')
    tahun = waktu.strftime('%Y')
    jam = waktu.strftime('%H')
    menit = waktu.strftime('%M')
    detik = waktu.strftime('%S')
    matkul,hare,jamuu,menuu,jambis,menis,meetid,passw,indhare,indhari = checkjadw()
    button5['text'] ="Join "+matkul+"Now"
    if matkul != lastMatkul:
        manualFlag = True
    lastMatkul = matkul
    if flag and manualFlag:
        if hare.casefold() == hari.casefold():
            if int(jam) == int(jambis):
                if int(menit) <= int(menis):
                    join_meet()
                    flag = False
            elif int(jam) >= int(jamuu):
                if int(menit) >= int(menuu):
                    join_meet()
                    flag = False

    submitlog(False)
    total = hari+', '+tanggal+'-'+bulan+'-'+tahun+' '+jam+':'+menit+':'+detik
    label5.config(text=total)
    label5.after(1000, clock)

def checkjadw():
    global pathlogjadw
    global hari
    global jam
    global menit
#     global enableDetik
    theday = ['sabtu','minggu','senin','selasa','rabu','kamis','jumat']
    count1 = 0
    count = 0
    matkul = 'a'
    hare ='a'
    jamuu = '0'
    menuu = '0'
    jambis = '0'
    menis = '0'
    meetid = '0'
    passw = '0'
    matkuls = 'a'
    hares = 'a'
    jamuus = '0'
    menuus = '0'
    jambiss = '0'
    meniss = '0'
    meetids = '0'
    passws = '0'
    indhare = 0
    indhari = 0
    indhares = 0
    saveon = False
    with open (pathlogjadw) as Flie:
        for x in Flie:
#             print(x)
            count1 = 0
            count = 0
            matkul = ''
            hare = ''
            jamuu = ''
            menuu = ''
            jambis = ''
            menis = ''
            meetid = ''
            passw = ''
            for y in x:
                if len(x)-1 > count1 > 9:
                    if y =="|":
                        count+=1
                        continue
                    elif count == 0:
                        matkul+=y
                    elif count == 1:
                        hare+=y
                    elif count == 2:
                        if y ==":":
                            count+=1
                            continue
                        else:
                            jamuu+=y
                    elif count == 3:
                        if y =="-":
                            count+=1
                            continue
                        else:
                            menuu+=y
                    elif count == 4:
                        if y ==":":
                            count+=1
                            continue
                        else:
                            jambis+=y
                    elif count == 5:
                        menis+=y
                    elif count == 6:
                        meetid+=y
                    elif count == 7:
                        passw+=y
                    count1+=1
                else:
                    count1+=1
#             hari = 'senin'
#             jam = '9'
            indhare = 0
            indhari = 0
            indhares = 0
            for z in theday:
                if z == hare.casefold():
                    break
                else:
                    indhare+=1
            for z in theday:
                if z == hari.casefold():
                    break
                else:
                    indhari+=1
            for z in theday:
                if z == hares.casefold():
                    break
                else:
                    indhares+=1
            saveon = False
            if indhari < indhare:
                if len(matkuls)==1:
                    saveon = True
                elif indhare < indhares:
#                     print('yes3')
                    saveon = True
                elif indhare == indhares:
#                     print('yes4')
                    if int(jambis) < int(jambiss):
#                         print('yes5')
                        saveon = True
                    elif int(jambis) == int(jambiss):
#                         print('yes6')
                        if int(menis) < int(meniss):
#                             print('yes7')
                            saveon = True
            elif indhari == indhare:
                if len(matkuls)==1:
                    if int(jam) <= int(jambis):
#                         print('yes8')
                        saveon = True
                    elif int(jam) == int(jambis):
                        if int(menit) <= int(menis):
#                             print('yes9')
                            saveon = True
                elif int(jambis) < int(jambiss):
#                     print('yes10')
                    saveon = True
                elif int(jambis) == int(jambiss):
#                     print('yes11')
                    if int(menis) < int(meniss):
#                         print('yes12')
                        saveon = True
#             if same:
                
            if saveon:
#                 print('save')
                matkuls = matkul
                hares = hare
                jamuus = jamuu
                menuus = menuu
                jambiss = jambis
                meniss = menis
                meetids = meetid
                passws = passw
    return matkuls,hares,jamuus,menuus,jambiss,meniss,meetids,passws,indhares,indhari

def submitlog(yasef = True):
    global pathlogjadw
    global tologlist
    global hari
    global jam
    global menit
    global flag
    if yasef:
        with open(pathlogjadw,'w'):
            pass
        for x in tologlist:
            logjadw.info(x)
    matkul,hare,jamuu,menuu,jambis,menis,meetid,passw,indhare,indhari = checkjadw()
#     print(hari,jam,menit)
    if hare.casefold() == hari.casefold():
        if int(jam) == int(jambis):
            if int(menit)<int(menis):
                label7.config(text="ONGOING Class: "+matkul+'on '+hare+' till '+str(jambis)+':'+str(menis),font='Helvetica 8 bold',fg='dark green')
            else:
                if matkul == 'a':
                    label7.config(text="Upcoming Class: No Upcoming Class on "+hare+' at '+str(jamuu)+':'+str(menuu),font='Helvetica 8 bold',fg='dark red')
                    flag = True
                else:
                    label7.config(text="Upcoming Class: "+matkul+'on '+hare+' at '+str(jamuu)+':'+str(menuu),font='Helvetica 8 bold',fg='black')
                    flag = True
        elif int(jam) >= int(jamuu):
            if int(menit) >= int(menuu):
                label7.config(text="ONGOING Class: "+matkul+'on '+hare+' till '+str(jambis)+':'+str(menis),font='Helvetica 8 bold',fg='dark green')
            else:
                if matkul == 'a':
                    label7.config(text="Upcoming Class: No Upcoming Class on "+hare+' at '+str(jamuu)+':'+str(menuu),font='Helvetica 8 bold',fg='dark red')
                    flag = True
                else:
                    label7.config(text="Upcoming Class: "+matkul+'on '+hare+' at '+str(jamuu)+':'+str(menuu),font='Helvetica 8 bold',fg='black')
                    flag = True
        elif int(jam)<int(jamuu):
            if matkul == 'a':
                label7.config(text="Upcoming Class: No Upcoming Class on "+hare+' at '+str(jamuu)+':'+str(menuu),font='Helvetica 8 bold',fg='dark red')
                flag = True
            else:
                label7.config(text="Upcoming Class: "+matkul+'on '+hare+' at '+str(jamuu)+':'+str(menuu),font='Helvetica 8 bold',fg='black')
                flag = True
        else:
            label7.config(text="Upcoming Class: No Upcoming Class on "+hare+' at '+str(jamuu)+':'+str(menuu),font='Helvetica 8 bold',fg='dark red')
            flag = True
    elif indhari<indhare:
        if matkul == 'a':
            label7.config(text="Upcoming Class: No Upcoming Class on "+hare+' at '+str(jamuu)+':'+str(menuu),font='Helvetica 8 bold',fg='dark red')
            flag = True
        else:
            label7.config(text="Upcoming Class: "+matkul+'on '+hare+' at '+str(jamuu)+':'+str(menuu),font='Helvetica 8 bold',fg='black')
            flag = True
    else:
        label7.config(text="Upcoming Class: No Upcoming Class on "+hare+' at '+str(jamuu)+':'+str(menuu),font='Helvetica 8 bold',fg='dark red')
        flag = True

def openFile():
    global dengansks
    global keywords
    global tologlist
    global jumhal_save
    num_pages = entry2.get()
    if len(num_pages)>0:
        if num_pages.isdigit():
            if int(num_pages) != jumhal_save:
                openNew(True)
    search = entry.get().casefold()
    with open(pathlogkode,'w'):
        pass
    with open(pathlogjumh,'w'):
        pass
    with open(pathlognama,'w'):
        pass
    nama = entry3.get()
    if len(nama) == 0:
        nama = "Ukrida"
    lognama.info(nama)
    logkode.info(entry.get())
    logjumh.info(num_pages)
    keypoint = []
    tologlist = []
    count1 = 0
    for x in keywords:
        if x.casefold() == search:
            keypoint.append(count1)
        count1 += 1
    count2 = 1#nomor
    count3 = 1
    count4 = 0
    countsks = 0
    digit = 0
    iden = 0
    text2 = []
    text1.configure(state='normal')
    text1.delete(1.0,tk.END)
    entry1.config(state="normal")
    entry1.delete(0, tk.END)
    entry1.config(state="disabled")
    if dengansks:
        text1.insert(tk.INSERT, " No |               Mata Kuliah               | SKS |  Kelas  |   Hari  |    Waktu    |                        Nama Dosen                       |  Meeting ID   | Pass\n")
    else:
        text1.insert(tk.INSERT, " No |               Mata Kuliah               |  Kelas  |  Hari  |    Waktu    |                        Nama Dosen                        |  Meeting ID   | Pass\n")
    for x in search:
        if x.isdigit():
            digit+=1
        else:
            iden+=1
    if (0<digit<3) and (iden == 4):
        texx = "found: "+str(len(keypoint))+" of "+search.upper()
        print(f"{bcolors.ENDC}"+texx)
        for x in keypoint:
            once1 = True
            text1.insert(tk.INSERT, " "+str(count2)+"  | ")
            tolog = ''
            while True:
                digit = 0
                iden = 0
                ocount = 0
                for y in keywords[x-count3]:
                    if y.isdigit():
                        digit+=1
                    else:
                        iden+=1
                    if y.casefold() == 'o':
                        ocount+=1
                    count4 +=1
                if once1:
                    if len(keywords[x-count3])>0:
                        if keywords[x-count3].isdigit():
                            sks = keywords[x-count3]
                            countsks+=1
                        else:
                            sks = ' '
                            once1 = False
                            continue
                    else:
                        sks = ' '
                    count3+=1
                    once1 = False
                    continue
                elif (digit == 0) and (iden == 0):
                    count3+=1
                    continue
                elif (digit == iden) or (iden == digit-1):
                    count3+=1
                    continue
                elif (digit+iden == 8) and (iden-ocount == 4):
                    count3+=1
                    continue
                elif (digit == 2) or (keywords[x-count3].casefold() == "passcode") or (keywords[x-count3].casefold() == "meet") or (keywords[x-count3].casefold() == "r") or (keywords[x-count3].casefold() == "k"):
                    count5 = 1
                    for i in stopper:
                        if i == keywords[x-count3+1].casefold():
                            break
                        else:
                            count5+=1
                    if count5<5:
                        entry1.config(state="normal")
                        entry1.delete(0, tk.END)
                        entry1.insert(tk.END,text2[0])
                        entry1.config(state="disabled")
                        text2.pop(0)
                    else:
                        entry1.config(state="normal")
                        entry1.delete(0, tk.END)
                        entry1.insert(tk.END,text2[0])
                        entry1.insert(tk.END," ")
                        entry1.insert(tk.END,text2[1])
                        entry1.config(state="disabled")
                        text2.pop(0)
                        text2.pop(0)
                    count4 = 0
                    for i in text2:
                        tolog+=i
                        tolog+=' '
                        count4+=1
                        for j in i:
                            count4+=1
                    text1.insert(tk.END, text2)
                    tolog+='|'
                    text2 = []
                    iden = 0
                    digit = 0
                    for z in range (count4,41):
                        text1.insert(tk.END, " ")
                    text1.insert(tk.END, "|  ")
                    if dengansks:
                        text1.insert(tk.END,sks)
                        text1.insert(tk.END,"  |  ")
                    text1.insert(tk.END, search.upper())
                    if len(search) == 6:
                        text1.insert(tk.END, " | ")
                    else:
                        text1.insert(tk.END, "  | ")
                   
                    count4 = 0
                    count2 += 1
                    count3 = 1
                    digit = 0
                    iden = 0
                    once = True
                    nama = ""
                    while True:
                        if keywords[x+count3].casefold() == "online":
                            count3+=1
                            continue
                        else:
                            digit = 0
                            iden = 0
                            kasis = keywords[x+count3].casefold()
                            for y in kasis:
                                if y.isdigit():
                                    digit+=1
                                else:
                                    iden+=1
#                             print(keywords[x+count3])
                            if (digit >= 8) and iden >= 2:
#                                 text1.insert(tk.END, "| ")
                                if iden == 3:
                                    text1.insert(tk.END, keywords[x+count3])
                                    tolog+=keywords[x+count3]
                                    tolog+='|'
                                elif iden == 5:
                                    count5 = 0
                                    for b in keywords[x+count3]:
                                        if 0<=count5<=4 or 8<=count5<=11 :
                                            text1.insert(tk.END, b)
                                            tolog+=b
                                            count5+=1
                                    count5 = 0
                                tolog+='|'
                                text1.insert(tk.END, " | ")
                            elif (digit == 6) and (iden == 2):
#                                 text1.insert(tk.END, "| ")
                                count5 = 0
                                for b in keywords[x+count3]:
                                    if 0<=count5<=4 or 8<=count5<=11 :
                                        text1.insert(tk.END, b)
                                        tolog+=b
                                        count5+=1
                                count5 = 0
                                if count3 == 4:
                                    tolog+='|'
                                    text1.insert(tk.END, " | ")
                                count3+=1
                                continue
                            elif (digit == 0) and (iden > 0):
                                if keywords[x+count3] == '-':
                                    text1.insert(tk.END, '-')
                                    tolog+='-'
                                    count3+=1
                                    continue
                                elif keywords[x+count3].casefold == 'k' or keywords[x+count3].casefold == 'r': #Kuliah(K)/Responsi(R)
                                    count3+=1
                                    continue
                                if (kasis == "senin") or (kasis == "selasa") or (kasis == "rabu") or (kasis == "kamis") or(kasis == "jumat") or (kasis == "sabtu"):
                                    text1.insert(tk.END, keywords[x+count3])
                                    tolog+=keywords[x+count3].capitalize()
                                    tolog+='|'
                                    for b in range(len(kasis),6):
                                        text1.insert(tk.END, " ")
                                    text1.insert(tk.END, " |")
                                elif len(keywords[x+count3]) >= 2:
                                    nomeet = False
                                    for b in stopper:
                                        if b == keywords[x+count3].casefold():
                                            nomeet = True
                                    if nomeet:
                                        break
                                    text1.insert(tk.END, keywords[x+count3].capitalize())#nama Dosen
                                    nama+=keywords[x+count3].capitalize()
                                    nama+=" "
                                text1.insert(tk.END, " ")
                            elif (digit>0) and (iden == 0):
                                if len(keywords[x+count3])== 2:
                                    tolog+='|'
                                    tolog+=keywords[x+count3] 
                                    text1.insert(tk.END, " | ")
                                    text1.insert(tk.END, keywords[x+count3])
                                    break
                                else:
                                    if once:
                                        for b in range(len(nama),56):
                                            text1.insert(tk.END, " ")
                                        text1.insert(tk.END, "|")
                                        nama = ""
                                        once = False
                                tolog+=keywords[x+count3] 
                                text1.insert(tk.END, " ")
                                text1.insert(tk.END, keywords[x+count3])
                            count3+=1
                    text1.insert(tk.END, "\n")
                    count3 = 1
                    digit = 0
                    iden = 0
                    tologlist.append(tolog)
                    tolog = ''
                    break
                else:
                    text2.insert(0,keywords[x-count3].capitalize()) #matkul
                    count3+=1
                    count4+=1
                    digit = 0
                    iden = 0
        if countsks<3 and len(keypoint)>4 and dengansks:
            dengansks = False
            openFile()
        elif countsks<2 and len(keypoint)<5 and dengansks:
            dengansks = False
            openFile()
        elif countsks>3 and (not dengansks):
            dengansks = True
            openFile()
    elif search.casefold() == 'aria' or search.casefold() == 'aria amadeus' or search.casefold() == 'aria amadeus salim':
        print('HAI!')
        text1.insert(tk.END, "HAI!")
    else:
        texx = 'Forbidden: "'+search+'" is not a class code'
        print(f"{bcolors.FAIL}"+texx)
    text1.configure(state='disabled')

def editJadwal():
    global thePopUp
    thePopUp = tk.Toplevel(root)
    thePopUp.geometry("600x400")
    thePopUp.title("Edit Jadwal")
    thePopUp.grab_set()
    thePopUp.protocol("WM_DELETE_WINDOW", editTutup)
    button4.config(state = "disabled")
    tk.Button(thePopUp, text = "Save Jadwal",font='Arial 8 bold',fg='black',state = "disabled").pack()
    boxEdit = tk.Text(thePopUp)
    boxEdit.pack()
    with open (pathlogjadw) as Flie:
        for x in Flie:
            boxEdit.insert(tk.END,x)
def editTutup():
    thePopUp.grab_release()
    thePopUp.destroy()
    button4.config(state = "normal")

button = tk.Button(text="Open",command=openNew)
button1 = tk.Button(text="Refresh",command=openFile)
button2 = tk.Button(text="Zoom Path",command=zoomchange)
button3 = tk.Button(text="Submit Jadwal",command=submitlog,font='Arial 8 bold',fg='black')
button4 = tk.Button(text="Edit Jadwal",command=editJadwal,fg='red')
button5 = tk.Button(text="Join _ Now",command=join_meet,font='Helvetica 8 bold',fg='green')
entry = tk.Entry()
entry1 = tk.Entry()
entry2 = tk.Entry()
entry3 = tk.Entry()
text1 = tk.Text(height=10, width=170)

entry.pack()
button.pack()
label2.pack()

text1.place(relx = 0, rely = 0.3)
button1.place(relx = 0.55, rely = 0.065)
button2.place(relx = 0.62, rely = 0.065)
button3.place(relx = 0.62, rely = 0.16)
button4.place(relx = 0.55, rely = 0.16)
button5.place(relx = 0.8, rely = 0.16)
label.place(relx = 0.35, rely = 0)
label1.place(relx = 0.35, rely = 0.06)
label3.place(relx = 0.1, rely = 0.14)
label4.place(relx = 0.6, rely = 0.0)
label5.place(relx = 0.1, rely = 0)
label6.place(relx = 0.7, rely = 0.07)
label7.place(relx = 0.03, rely = 0.06)
entry1.place(relx = 0.13, rely = 0.14)
entry2.place(relx = 0.7, rely = 0.0)
entry3.place(relx = 0.7, rely = 0.14)
text1.insert(tk.INSERT, " No |               Mata Kuliah               | SKS |  Kelas  |  Hari  |    Waktu    |                        Nama Dosen                        |  Meeting ID   | Pass\n")
text1.configure(state='disabled')
entry1.config(state='disabled')
root.title("UKRIDA beta v.1.1.0")
count = 0
count1 = 0
search = ''
with open (pathlogkode) as Flie:
    for x in Flie:
        count += 1
        count1 = 0
        for y in x:
            if len(x)-1 > count1 > 9:
                search+=y
                count1+=1
            else:
                count1+=1
if count>0:
    entry.insert(0,search)
count = 0
count1 = 0
search = ''
with open (pathlogjumh) as Flie:
    for x in Flie:
        count += 1
        count1 = 0
        for y in x:
            if len(x)-1 > count1 > 9:
                search+=y
                count1+=1
            else:
                count1+=1
if count>0:
    entry2.insert(0,search)
count = 0
count1 = 0
search = ''
with open (pathlognama) as Flie:
    for x in Flie:
        count += 1
        count1 = 0
        for y in x:
            if len(x)-1 > count1 > 9:
                search+=y
                count1+=1
            else:
                count1+=1
if count>0:
    entry3.insert(0,search)
count = 0
count1 = 0
with open (pathlogjadw) as Flie:
    for x in Flie:
        count += 1
if count>0:
    submitlog(False)
count = 0
with open (pathlogmpdf) as Flie:
    for x in Flie:
        count += 1
        count1 = 0
        for y in x:
            if len(x)-1 > count1 > 9:
                filepath+=y
                count1+=1
            else:
                count1+=1
if count>0:
    filepath_save = filepath
    openNew(True)
count = 0
count1 = 0
#Listener
keyboard.on_press_key("enter",lambda _:openFile())
clock()
root.mainloop()
quit()