import os

import textract as txr
import PyPDF2 as pdr

#14-19 Maret 22

dengansks = True
jumhal_save = 0
count = 0
count1 = 0

prodi = ["akuntansi","informatika","manajemen","psikologi","sastra","sistem","teknik","informasi","inggris","sipil","elektro","industri"]

keywords = []
stopper = ["akuntansi","informatika","manajemen","psikologi","sastra","sistem","teknik","google","ptm"]
tologlist = []

def openNew(num_pages):
    global filepath
    global filepath_save
    global keywords
    global jumhal_save
    keywords = []
    pdfFileObj = open("nextPDF.pdf",'rb')
    pdfReader = pdr.PdfFileReader(pdfFileObj)
    print("Processing "+str(num_pages)+" Pages")
    count = 0
    text = ''
    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count+=1
        print(str(count))
        if len(pageObj.extractText())>0:
            text+=pageObj.extractText()
    word = ''
    
    #delete keywords
    with open('keywords.txt','w') as easyKey:
        pass
    for x in text:
        if (x == ' ')or(x == '\n'):
            with open('keywords.txt','a') as easyKey:
                easyKey.write(word+"\n")
            keywords.append(word)
            word = ''
        else:
            word += x
    print('done')

def openFile(search):
    global dengansks
    global tologlist
    global jumhal_save
    keypoint = []
    tologlist = []
    count1 = 0
    keywords = []
    
    #Step1 Open file & turn text into list
    with open('keywords.txt','r') as textKey:
        word = ''
        for x in textKey.read():
            if (x == ' ')or(x == '\n'):
                keywords.append(word)
                word = ''
            else:
                word += x
    
    #Step2, 
    for x in keywords:
        #ada berapa banyak kode kelas di pdf
        if x.casefold() == search.casefold():
            keypoint.append(count1)
        count1 += 1
    count2 = 1 #nomor
    count3 = 1
    count4 = 0
    countsks = 0
    digit = 0
    iden = 0
    text2 = []
    #check kode kelas atau bukan
    for x in search:
        if x.isdigit():
            digit+=1
        else:
            iden+=1
            
    #Kalau kode kelas :
    if (0<digit<3) and (iden == 4):
#         print("found: "+str(len(keypoint))+" of "+search.upper())
        for x in keypoint:
            once1 = True
            tolog = ''
            while True:
#ke kiri
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
                
                #skipper
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
                #skip None
                elif (digit == 0) and (iden == 0):
                    count3+=1
                    continue
                #skip Course ID
                elif (digit == iden) or (iden == digit-1):
                    count3+=1
                    continue
                #skip Course ID juga, tapi 0 nya O
                elif (digit+iden == 8) and (iden-ocount == 4):
                    count3+=1
                    continue
                
                #stopper matakuliah #14-19 if False
                elif (digit == 2) or (keywords[x-count3].casefold() == "passcode") or (keywords[x-count3].casefold() == "meet") or (keywords[x-count3].casefold() == "r") or (keywords[x-count3].casefold() == "k"):
                    count5 = 1
                    #Prodi kiri
                    if False:
                        for i in stopper:
                            if i == keywords[x-count3+1].casefold():
                                break
                            else:
                                count5+=1
                        if count5<5:
                            text2.pop(0)
                        else:
                            text2.pop(0)
                            text2.pop(0)
                    count4 = 0
                    #MATKUL
                    for i in text2:
                        tolog+=i
                        tolog+=' '
                        count4+=1
                        for j in i:
                            count4+=1
                    tolog+='|'
                    text2 = []
                    iden = 0
                    digit = 0
                    count4 = 0
                    count2 += 1
                    count3 = 1
                    digit = 0
                    iden = 0
                    once = True
                    nama = ""
#ke kanan
                    while True:
                        #lompatin online
                        if keywords[x+count3].casefold() == "online":
                            count3+=1
                            continue
                        #lompatin lab
                        elif keywords[x+count3].casefold() == "lab" or keywords[x+count3].casefold() == "t.sipil" or keywords[x+count3].casefold() == "sipil" or keywords[x+count3].casefold() == "t.elektro":
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
                            if (digit >= 8) and iden >= 2:
                                if iden == 3:
                                    #WAKTU
                                    tolog+=keywords[x+count3]
                                    
                                    tolog+='|'
                                elif iden == 5:
                                    count5 = 0
                                    #WAKTU
                                    for b in keywords[x+count3]:
                                        if 0<=count5<=4 or 8<=count5<=11 :
                                            tolog+=b
                                            count5+=1
                                    count5 = 0
                                tolog+='|'
                            elif (digit == 6) and (iden == 2):
                                count5 = 0
                                for b in keywords[x+count3]:
                                    #WAKTU Using now
                                    if 0<=count5<=4 or 8<=count5<=11 :
                                        tolog+=b
                                        count5+=1
                                count5 = 0
                                tolog+='|'
                                
                                #LOMPATIN KDS
                                #count3+=4
                                
                                #Gajadi lompatin KDS
                                count3+=1
                                continue
                            
                            elif (digit == 0) and (iden > 0):
                                if keywords[x+count3] == '-':
                                    tolog+='-'
                                    count3+=1
                                    continue
                                #Skip Prodi kanan
                                if keywords[x+count3].casefold() in prodi and True:
                                    count3+=1
                                    continue
                                
                                #Kuliah(K)/Responsi(R)
                                elif keywords[x+count3] == 'K' or keywords[x+count3] == 'R': 
                                    count3+=1
                                    continue
                                
                                if (kasis == "senin") or (kasis == "selasa") or (kasis == "rabu") or (kasis == "kamis") or(kasis == "jumat") or (kasis == "sabtu"):
                                    #HARI
                                    tolog+=keywords[x+count3].capitalize()
                                    tolog+='|'
                                
                                elif len(keywords[x+count3]) >= 2:
                                    nomeet = False
                                    if keywords[x+count3] == 'PTM' or keywords[x+count3].casefold() == 'meet':
                                        nama+='|'
                                        nama+=keywords[x+count3]
                                        tolog+=nama
                                        break
                                    for b in stopper:
                                        if b == keywords[x+count3].casefold():
                                            nomeet = True
                                    if nomeet:
                                        #Fetch nama dosen disini
                                        break
                                    nama+=keywords[x+count3].capitalize()
                                    nama+=" "
                            elif ((digit>0) and (iden == 0)):
                                #pass
                                if len(keywords[x+count3])== 2:
                                    tolog+='|'
                                    tolog+=keywords[x+count3]
                                    break
                                else:
                                    if once:
                                        tolog+=nama
                                        tolog+='|'
                                        nama = ""
                                        once = False
                                #meetID / PTM
                                
                                tolog+=keywords[x+count3]
                            #meetId bakal terus ditambahin sampe kena breaknya pass
                            count3+=1
                    count3 = 1
                    digit = 0
                    iden = 0
                    tologlist.append(tolog.split('|'))
                    tolog = ''
                    break
                else:
                    text2.insert(0,keywords[x-count3].capitalize()) #matkul
                    count3+=1
                    count4+=1
                    digit = 0
                    iden = 0
#         if countsks<3 and len(keypoint)>4 and dengansks:
#             dengansks = False
#             openFile()
#         elif countsks<2 and len(keypoint)<5 and dengansks:
#             dengansks = False
#             openFile()
#         elif countsks>3 and (not dengansks):
#             dengansks = True
#             openFile()
    
    return tologlist

if __name__ == "__main__":
    openNew(13)
    print(openFile('6peea'))
