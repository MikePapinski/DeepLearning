import pandas as pd
import datetime
import qtpylib
from talib import RSI, BBANDS, CCI, MACD

#import matplotlib.pyplot as plt

def GetTheInput_Single():
    # import the candle stick data
    DIR='PredictCandlestick/DATA/EURUSD'
    MyRawData = pd.read_csv(DIR+'/EURUSD_15M.csv', delimiter=',')

    #calculate time series
    MyRawData['time'] = pd.to_datetime(MyRawData['Gmt time'])
    MyRawData['Day of Week'] = MyRawData['time'].apply(lambda time: time.dayofweek)
    MyRawData['Hour'] = MyRawData['Gmt time'].str[11:13]
    MyRawData['Minute'] = MyRawData['Gmt time'].str[14:16]

    #calculate candle size parameters in pips
    MyRawData['BodyPips'] = (abs(MyRawData['Open']-MyRawData['Close']) * 10000)
    MyRawData['WickUpPips'] = (abs(MyRawData['Open']-MyRawData['High']) * 10000)
    MyRawData['WickDownPips'] = (abs(MyRawData['Close']-MyRawData['Low']) * 10000)


    #calculate the candle type - undecision, buy , sell
    MyRawData.loc[MyRawData.BodyPips == 0, 'GreenOrRed?'] = 0
    MyRawData.loc[MyRawData.Open < MyRawData.Close, 'GreenOrRed?'] = 1
    MyRawData.loc[MyRawData.Open > MyRawData.Close, 'GreenOrRed?'] = 2


    #add custom indicators
    MyRawData['RSI'] = RSI(MyRawData['Close'], timeperiod=14)
    MyRawData['BB_up'], MyRawData['BB_mid'], MyRawData['BB_low'] = BBANDS(MyRawData['Close'], timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    MyRawData['CCI'] = CCI(MyRawData['High'], MyRawData['Low'], MyRawData['Close'], timeperiod=14)
    MyRawData['MACD'], MyRawData['MACD_Signal'], MyRawData['MACD_Hist'] = MACD(MyRawData['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    #populate las column with the output
    MyRawData['output'] = MyRawData['GreenOrRed?'].shift(-1)


    #remove not important fields
    del MyRawData['Gmt time']
    del MyRawData['Open']
    del MyRawData['High']
    del MyRawData['Low']
    del MyRawData['Close']
    del MyRawData['Volume']
    del MyRawData['time']

    #remove last row without output value
    MyFinalData = MyRawData[50:-1]

    return MyFinalData


def GetTheInput_Multiple():
    # import the candle stick data
    DIR='PredictCandlestick/DATA/EURUSD'
    MyRawData = pd.read_csv(DIR+'/EURUSD_15M.csv', delimiter=',')

    #calculate time series
    MyRawData['time'] = pd.to_datetime(MyRawData['Gmt time'])
    MyRawData['Day of Week'] = MyRawData['time'].apply(lambda time: time.dayofweek)
    MyRawData['Hour'] = MyRawData['Gmt time'].str[11:13]
    MyRawData['Minute'] = MyRawData['Gmt time'].str[14:16]

    #calculate candle size parameters in pips
    MyRawData['BodyPips'] = (abs(MyRawData['Open']-MyRawData['Close']) * 10000)
    MyRawData['WickUpPips'] = (abs(MyRawData['Open']-MyRawData['High']) * 10000)
    MyRawData['WickDownPips'] = (abs(MyRawData['Close']-MyRawData['Low']) * 10000)


    #calculate the candle type - undecision, buy , sell
    MyRawData.loc[MyRawData.BodyPips == 0, 'GreenOrRed?'] = 0
    MyRawData.loc[MyRawData.Open < MyRawData.Close, 'GreenOrRed?'] = 1
    MyRawData.loc[MyRawData.Open > MyRawData.Close, 'GreenOrRed?'] = 2


    #add custom indicators
    MyRawData['RSI'] = RSI(MyRawData['Close'], timeperiod=14)
    MyRawData['BB_up'], MyRawData['BB_mid'], MyRawData['BB_low'] = BBANDS(MyRawData['Close'], timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    MyRawData['CCI'] = CCI(MyRawData['High'], MyRawData['Low'], MyRawData['Close'], timeperiod=14)
    MyRawData['MACD'], MyRawData['MACD_Signal'], MyRawData['MACD_Hist'] = MACD(MyRawData['Close'], fastperiod=12, slowperiod=26, signalperiod=9)



    #add 4 more history candle sticks
    for CandleCount in range(4):
        ActualCandleCount = CandleCount + 1
        MyRawData['BodyPips' + '_' + str(ActualCandleCount)] = MyRawData['BodyPips'].shift(-ActualCandleCount)
        MyRawData['WickUpPips' + '_' + str(ActualCandleCount)] = MyRawData['WickUpPips'].shift(-ActualCandleCount)
        MyRawData['WickDownPips' + '_' + str(ActualCandleCount)] = MyRawData['WickDownPips'].shift(-ActualCandleCount)
        MyRawData['GreenOrRed?' + '_' + str(ActualCandleCount)] = MyRawData['GreenOrRed?'].shift(-ActualCandleCount)
        MyRawData['RSI' + '_' + str(ActualCandleCount)] = MyRawData['RSI'].shift(-ActualCandleCount)
        MyRawData['BB_up' + '_' + str(ActualCandleCount)] = MyRawData['BB_up'].shift(-ActualCandleCount)
        MyRawData['BB_mid' + '_' + str(ActualCandleCount)] = MyRawData['BB_mid'].shift(-ActualCandleCount)
        MyRawData['BB_low' + '_' + str(ActualCandleCount)] = MyRawData['BB_low'].shift(-ActualCandleCount)
        MyRawData['CCI' + '_' + str(ActualCandleCount)] = MyRawData['CCI'].shift(-ActualCandleCount)
        MyRawData['MACD' + '_' + str(ActualCandleCount)] = MyRawData['MACD'].shift(-ActualCandleCount)
        MyRawData['MACD_Signal' + '_' + str(ActualCandleCount)] = MyRawData['MACD_Signal'].shift(-ActualCandleCount)
        MyRawData['MACD_Hist' + '_' + str(ActualCandleCount)] = MyRawData['MACD_Hist'].shift(-ActualCandleCount)

 

    #populate las column with the output
    MyRawData['output'] = MyRawData['GreenOrRed?'].shift(-5)


    #remove not important fields
    del MyRawData['Gmt time']
    del MyRawData['Open']
    del MyRawData['High']
    del MyRawData['Low']
    del MyRawData['Close']
    del MyRawData['Volume']
    del MyRawData['time']

    #remove last row without output value
    MyFinalData = MyRawData[100:-5]

    MyFinalData.to_csv('test', sep='\t')
    






    return MyFinalData


test = GetTheInput_Single()
print(len(test.columns))
print(test)