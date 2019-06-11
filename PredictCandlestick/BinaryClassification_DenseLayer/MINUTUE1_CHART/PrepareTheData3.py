import pandas as pd
import datetime
import numpy as np
from CustomIndicators import moving_average, relative_strength, moving_average_convergence

#import matplotlib.pyplot as plt

def GetTheInput_Single(filename):
    # import the candle stick data

    MyRawData = pd.read_csv(filename) 

    
    #MyRawData = MyRawData.tail(850000)
    #calculate time series
    MyRawData['time'] = pd.to_datetime(MyRawData['Gmt time'])
    MyRawData['Day of Week'] = MyRawData['time'].apply(lambda time: time.dayofweek)
    MyRawData['Hour'] = MyRawData['Gmt time'].str[11:13].astype(dtype=np.int64)
    MyRawData['Minute'] = MyRawData['Gmt time'].str[14:16].astype(dtype=np.int64)

    #calculate candle size parameters in pips
    MyRawData['BodyPips'] = abs((MyRawData['Open']-MyRawData['Close']) * 10000)
    MyRawData['WickUpPips'] = (abs(MyRawData['Open']-MyRawData['High']) * 10000)
    MyRawData['WickDownPips'] = (abs(MyRawData['Close']-MyRawData['Low']) * 10000)

    MyRawData['Day of Week Normal'] = (MyRawData['Day of Week'] /4)
    MyRawData['Hour Normal'] = (MyRawData['Day of Week'] /23)
    MyRawData['Minute Normal'] = (MyRawData['Minute'] /59)
    #calculate the candle type - undecision, buy , sell
    MyRawData.loc[MyRawData.BodyPips == 0, 'GreenOrRed?'] = 0
    MyRawData.loc[MyRawData.Open < MyRawData.Close, 'GreenOrRed?'] = 1
    MyRawData.loc[MyRawData.Open > MyRawData.Close, 'GreenOrRed?'] = 0

  

    nslow = 26
    nfast = 12
    nema = 9
    MyRawData['EmaSlow'], MyRawData['EmaFast'], MyRawData['MACD'] = moving_average_convergence(MyRawData['Close'].values, nslow=nslow, nfast=nfast)
    MyRawData['Ema9'] = moving_average(MyRawData['MACD'].values, nema, type='exponential')
    MyRawData['RSI'] = relative_strength(MyRawData['Close'].values)


   
    #add 4 more history candle sticks
    for CandleCount in range(10):
        ActualCandleCount = CandleCount + 1
        MyRawData['BodyPips' + '_' + str(ActualCandleCount)] = MyRawData['BodyPips'].shift(-ActualCandleCount)
        MyRawData['WickUpPips' + '_' + str(ActualCandleCount)] = MyRawData['WickUpPips'].shift(-ActualCandleCount)
        MyRawData['WickDownPips' + '_' + str(ActualCandleCount)] = MyRawData['WickDownPips'].shift(-ActualCandleCount)
        MyRawData['Day of Week Normal' + '_' + str(ActualCandleCount)] = MyRawData['Minute Normal'].shift(-ActualCandleCount)
        MyRawData['Hour Normal' + '_' + str(ActualCandleCount)] = MyRawData['Hour Normal'].shift(-ActualCandleCount)
        MyRawData['Minute Normal' + '_' + str(ActualCandleCount)] = MyRawData['Minute Normal'].shift(-ActualCandleCount)
        MyRawData['GreenOrRed?' + '_' + str(ActualCandleCount)] = MyRawData['GreenOrRed?'].shift(-ActualCandleCount)
        MyRawData['EmaSlow' + '_' + str(ActualCandleCount)] = MyRawData['EmaSlow'].shift(-ActualCandleCount)
        MyRawData['EmaFast' + '_' + str(ActualCandleCount)] = MyRawData['EmaFast'].shift(-ActualCandleCount)
        MyRawData['MACD' + '_' + str(ActualCandleCount)] = MyRawData['MACD'].shift(-ActualCandleCount)
        MyRawData['Ema9' + '_' + str(ActualCandleCount)] = MyRawData['Ema9'].shift(-ActualCandleCount)
        MyRawData['RSI' + '_' + str(ActualCandleCount)] = MyRawData['RSI'].shift(-ActualCandleCount)

    #populate las column with the output
    MyRawData['output'] = MyRawData['GreenOrRed?'].shift(11)

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
    MyFinalData = MyRawData[150:-150]

    return MyFinalData


def GetTheInput_OHLC():

     # import the candle stick data

    MyRawData = pd.read_csv(r"D:\Users\Mike\Desktop\New folder (5)\New folder (7)\DeepLearning\PredictCandlestick\BinaryClassification_DenseLayer\1_MINUTUE_CHART\filename.csv") 

    MyRawData = MyRawData.tail(1000)
    #calculate time series
    MyRawData['time'] = pd.to_datetime(MyRawData['Gmt time'])
    MyRawData['Day of Week'] = MyRawData['time'].apply(lambda time: time.dayofweek)
    MyRawData['Hour'] = MyRawData['Gmt time'].str[11:13].astype(dtype=np.int64)
    MyRawData['Minute'] = MyRawData['Gmt time'].str[14:16].astype(dtype=np.int64)

    #calculate candle size parameters in pips
    MyRawData['BodyPips'] = abs((MyRawData['Open']-MyRawData['Close']) * 10000)
    MyRawData['WickUpPips'] = (abs(MyRawData['Open']-MyRawData['High']) * 10000)
    MyRawData['WickDownPips'] = (abs(MyRawData['Close']-MyRawData['Low']) * 10000)

    MyRawData['Day of Week Normal'] = (MyRawData['Day of Week'] /4)
    MyRawData['Hour Normal'] = (MyRawData['Day of Week'] /23)
    MyRawData['Minute Normal'] = (MyRawData['Minute'] /59)
    #calculate the candle type - undecision, buy , sell
    MyRawData.loc[MyRawData.BodyPips == 0, 'GreenOrRed?'] = 0
    MyRawData.loc[MyRawData.Open < MyRawData.Close, 'GreenOrRed?'] = 1
    MyRawData.loc[MyRawData.Open > MyRawData.Close, 'GreenOrRed?'] = 0

  

    nslow = 26
    nfast = 12
    nema = 9
    MyRawData['EmaSlow'], MyRawData['EmaFast'], MyRawData['MACD'] = moving_average_convergence(MyRawData['Close'].values, nslow=nslow, nfast=nfast)
    MyRawData['Ema9'] = moving_average(MyRawData['MACD'].values, nema, type='exponential')
    MyRawData['RSI'] = relative_strength(MyRawData['Close'].values)



    #remove last row without output value
    MyFinalData = MyRawData[150:-150]

    return MyFinalData

