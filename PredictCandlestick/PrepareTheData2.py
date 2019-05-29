import pandas as pd
import datetime
import numpy as np

#import matplotlib.pyplot as plt

def GetTheInput_Single():
    # import the candle stick data

    # Load the Pandas libraries with alias 'pd' 
    # Read data from file 'filename.csv' 
    # (in the same directory that your python process is based)
    # Control delimiters, rows, column names with read_csv (see later) 
    MyRawData = pd.read_csv(r"D:\Users\Mike\Desktop\daaaa\DeepLearning\PredictCandlestick\filename.csv") 
    # Preview the first 5 lines of the loaded data 
    MyRawData = MyRawData.tail(1000)
    #calculate time series
    MyRawData['time'] = pd.to_datetime(MyRawData['Gmt time'])
    MyRawData['Day of Week'] = MyRawData['time'].apply(lambda time: time.dayofweek)
    MyRawData['Hour'] = MyRawData['Gmt time'].str[11:13].astype(dtype=np.int64)
    MyRawData['Minute'] = MyRawData['Gmt time'].str[14:16].astype(dtype=np.int64)

    #calculate candle size parameters in pips
    MyRawData['BodyPips'] = (MyRawData['Open']-MyRawData['Close']) * 10000
    MyRawData['WickUpPips'] = (abs(MyRawData['Open']-MyRawData['High']) * 10000)
    MyRawData['WickDownPips'] = (abs(MyRawData['Close']-MyRawData['Low']) * 10000)

    MyRawData['Day of Week Normal'] = (MyRawData['Day of Week'] /4)
    MyRawData['Hour Normal'] = (MyRawData['Day of Week'] /23)
    MyRawData['Minute Normal'] = (MyRawData['Minute'] /59)
    #calculate the candle type - undecision, buy , sell
    #MyRawData.loc[MyRawData.BodyPips == 0, 'GreenOrRed?'] = 0
    #MyRawData.loc[MyRawData.Open < MyRawData.Close, 'GreenOrRed?'] = 1
    #MyRawData.loc[MyRawData.Open > MyRawData.Close, 'GreenOrRed?'] = 0

   #populate las column with the output
    #MyRawData['output'] = MyRawData['GreenOrRed?'].shift(-1)

   
    #add 4 more history candle sticks
    for CandleCount in range(4):
        ActualCandleCount = CandleCount + 1
        MyRawData['BodyPips' + '_' + str(ActualCandleCount)] = MyRawData['BodyPips'].shift(-ActualCandleCount)
        MyRawData['WickUpPips' + '_' + str(ActualCandleCount)] = MyRawData['WickUpPips'].shift(-ActualCandleCount)
        MyRawData['WickDownPips' + '_' + str(ActualCandleCount)] = MyRawData['WickDownPips'].shift(-ActualCandleCount)
        MyRawData['Day of Week Normal' + '_' + str(ActualCandleCount)] = MyRawData['Minute Normal'].shift(-ActualCandleCount)
        MyRawData['Hour Normal' + '_' + str(ActualCandleCount)] = MyRawData['Hour Normal'].shift(-ActualCandleCount)
        MyRawData['Minute Normal' + '_' + str(ActualCandleCount)] = MyRawData['Minute Normal'].shift(-ActualCandleCount)


   #populate las column with the output
    MyRawData['output'] = MyRawData['BodyPips'].shift(-5)

    #remove not important fields
    del MyRawData['Gmt time']
    del MyRawData['Open']
    del MyRawData['High']
    del MyRawData['Low']
    del MyRawData['Close']
    del MyRawData['Volume']
    del MyRawData['time']
    del MyRawData['Day of Week']
    del MyRawData['Hour'] 
    del MyRawData['Minute'] 

    #remove last row without output value
    MyFinalData = MyRawData[0:-100]
    print(MyFinalData)

    return MyFinalData


GetTheInput_Single()

