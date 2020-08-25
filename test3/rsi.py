import pandas as pd
import sqlite3
from test3.etl import *
import datetime
import numpy as np

class DataBase(DataBase):
    def readToDataFrame(self, tableName):
        tableName = 'PRICE__' + tableName + "__TB"
        query = "SELECT * FROM " + tableName
        dataFrame = pd.read_sql(query, self.con, index_col=None)
        return dataFrame


class QuaterTime:

    def isQuaterTimer(self, time):
        time = time[14:16]
        time = int(time)
        if time % 15 == 0:
            return True
        else:
            return False

class RSI:
    def __init__(self):
        self.upList = []
        self.downList = []


    def calculate(self, indexRangeList, dataFrame):
        startIndex = 0
        for endIndex in indexRangeList:
            endIndex = int(endIndex)
            dataFrame = dataFrame['매도호가'].iloc[startIndex:endIndex-1]

            up = np.where(dataFrame.diff(1) > 0, dataFrame.diff(1), 0)
            down = np.where(dataFrame.diff(1) < 0, dataFrame.diff(1) * -1, 0)



            startIndex = endIndex



    def upORDown(self, medoHoga, afterMedoHoga):
        medoHoga = float(medoHoga)
        afterMedoHoga = float(afterMedoHoga)
        if medoHoga >= afterMedoHoga:
            spread = medoHoga - afterMedoHoga
            self.upList.append(spread)

        elif medoHoga <= afterMedoHoga:
            spread = afterMedoHoga - medoHoga
            self.downList.append(spread)

    def upORDownAverage(self):
        upMean = np.mean(self.upList)

        if len(self.downList) != 0:
            downMean = np.mean(self.downList)
        else:
            downMean = 0


        return upMean, downMean






class QuaterClosePriceIndex:
    def __init__(self):
        self.tmp = True
        self.QuaterTime = QuaterTime()

    def calculate(self, datatFrame):
        indexRangeList = []
        for i in range(len(datatFrame)):
            time = datatFrame['거래시간'].iloc[i]
            if self.QuaterTime.isQuaterTimer(time) != self.tmp and self.QuaterTime.isQuaterTimer(time) == True:
                i = str(i)
                indexRangeList.append(i)

            self.tmp = self.QuaterTime.isQuaterTimer(time)
        return indexRangeList

if __name__ == '__main__':
    csvName = CSVFileName()
    fileNameList = csvName.getList()
    bitcoin = fileNameList[0]

    dir = DirName()
    dirName = dir.standardFormat()
    dataBase = DataBase()

    dataBase.connect(bitcoin)
    df = dataBase.readToDataFrame(tableName=dirName)
    print(df)
    time = df['거래시간'].iloc[0]
    quaterTime = QuaterTime()
    print(quaterTime.isQuaterTimer(time))

    quaterCloseIndex = QuaterClosePriceIndex()
    indexRangeList = quaterCloseIndex.calculate(datatFrame=df)
    rsi = RSI()
    rsi.calculate(indexRangeList=indexRangeList, dataFrame=df)