import csv

import pandas as pd

from teleBotClock import *

def checkID(ID):
    with open('names.csv', 'r') as csvFile:
        count = sum(1 for row in csv.DictReader(csvFile))
        total = count + 1
    with open('names.csv', 'r') as csvFile:
        csvNama = csv.DictReader(csvFile)
        for line in csvNama:
            if int(line['ID']) == ID:
                return total - count
            count -= 1
        return count

def AllID():
    IDs = []
    with open('names.csv', 'r') as csvFile:
        csvNama = csv.DictReader(csvFile)
        for line in csvNama:
            IDs.append(line['ID'])
    return IDs
    
def checkClass(ID):
    with open('names.csv', 'r') as csvFile:
        count = sum(1 for row in csv.DictReader(csvFile))
        total = count + 1
    with open('names.csv', 'r') as csvFile:
        csvNama = csv.DictReader(csvFile)
        for line in csvNama:
            if int(line['ID']) == ID:
                return line['classCode']
            count -= 1
        return False
    
def checkIDclock(classCodes, Hari, Waktu):
    with open('names.csv', 'r') as csvFile:
        count = sum(1 for row in csv.DictReader(csvFile))
        total = count + 1
    with open('names.csv', 'r') as csvFile:
        csvNama = csv.DictReader(csvFile)
        for line in csvNama:
            if line['classCode'] in classCodes:
                df = pd.read_csv("names.csv")
                schedulesClock(df.loc[(total - count)-1,'ID'],line['classCode'], Hari, Waktu)
                #return total - count
            count -= 1
        #return count

def newID(ID, firstName, uname, classCode, timeInterval, status):
    with open('names.csv', 'a') as csv_write:
        csvWrite = csv.writer(csv_write)
        csvWrite.writerow([ID, firstName, uname, classCode, timeInterval, status])
        csv_write.close()

def changeClass(row, classCode):
    df = pd.read_csv("names.csv")
    df.loc[row-1,'classCode'] = classCode
    df.to_csv("names.csv", index = False)

def changeTime(row, timeInterval):
    df = pd.read_csv("names.csv")
    df.loc[row-1,'timeInterval'] = timeInterval
    df.to_csv("names.csv", index = False)

def changeStatus(row, status):
    df = pd.read_csv("names.csv")
    df.loc[row-1,'status'] = status
    df.to_csv("names.csv", index = False)

if __name__ == "__main__":
    print('Ukrida @2022')
    #changeClass(checkID(16))
    #if checkID(16) == 0:
        #newID(16, 'a','Aria','4PEEA', 10, 'active')
                