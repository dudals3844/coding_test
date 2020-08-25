import pandas as pd
import sqlite3
from test3.etl import *
import datetime

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

class QuaterClosePrice:
    def __init__(self):
        self.tmp = True
        self.isQuaterTime = QuaterTime()

    def calculate(self, datatFrame):
        for i in range(len(datatFrame)):
            time = datatFrame['거래시간'].iloc[i]
            medoHoga = datatFrame['매도호가'].iloc[i]
            if self.isQuaterTime.isQuaterTimer(time) != self.tmp and self.isQuaterTime.isQuaterTimer(time) == True:
                pass

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
