import pandas as pd
import time
import datetime
import sqlite3

class CSVFileName:
    def __init__(self):
        self.nameList = ['POLONIEX_SPOT_LTC_BTC', 'POLONIEX_SPOT_LTC_USDC', 'POLONIEX_SPOT_LTC_USDT']

    def getList(self):
        return self.nameList


class DirName:
    def __init__(self):
        self.start = datetime.datetime(2020, 7, 19)


    def standardFormat(self):
        standardFormat = self.start.strftime("%Y%m%d")
        return standardFormat

    def addOneDay(self):
        self.start = self.start +datetime.timedelta(days=1)
        return self.start


class DataBase:
    def __init__(self):
        pass

    def connect(self, dataName):
        self.con = sqlite3.connect('./'+dataName+'.db')

    def dataFrameToDataBase(self, dataFrame, tablename):
        dataFrame.to_sql(tablename, self.con)

    def close(self):
        self.con.close()
class StandardTime:
    def modified(self, timeString):
        replaceTimeString = timeString.replace("T", " ")
        return replaceTimeString

class PriceData:
    def processToDataFrame(self, dataFrame):
        standardTime = StandardTime()
        priceList = []
        for i in range(len(dataFrame)):
            tmp = dataFrame.iloc[i]
            tmpList = list(tmp)
            tmp = tmpList[0]
            tmp = tmp.split(';')
            tmp[1] = standardTime.modified(tmp[1])
            tmp[2] = standardTime.modified(tmp[2])
            priceList.append(tmp)
        print('분석끝')
        priceDataFrame = pd.DataFrame(priceList, columns=['아이디', '거래시간', 'api시간', '매도호가', '매도호가잔량', '매수호가', '매수호가잔량'])
        return priceDataFrame


if __name__ == '__main__':
    dir = DirName()
    csvFileName = CSVFileName()
    fileNameList = csvFileName.getList()
    while True:
        try:

            dirName = dir.standardFormat()
            dataBase = DataBase()
            print(dirName)
            for fileName in fileNameList:
                print(fileName)
                path = '../data/quotes/'+dirName +'/'+fileName+'.csv'
                originalDataFrame = pd.read_csv(path)
                priceData = PriceData()
                priceDataFrame = priceData.processToDataFrame(dataFrame=originalDataFrame)
                dataBase.connect(dataName=fileName)
                dataBase.dataFrameToDataBase(dataFrame=priceDataFrame, tablename=dirName)
                dataBase.close()

            print('날짜추가')
            dir.addOneDay()

        except Exception as e:
            print(e)
            break
