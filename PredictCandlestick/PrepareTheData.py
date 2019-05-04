import pandas as pd
import datetime
import qtpylib

def GetTheInput():
    # import the candle stick data
    DIR='PredictCandlestick/DATA/EURUSD'
    MyRawData = pd.read_csv(DIR+'/EURUSD1M.csv', delimiter=',')

    #calculate time series
    MyRawData['time'] = pd.to_datetime(MyRawData['Gmt time'])
    MyRawData['Day of Week'] = MyRawData['time'].apply(lambda time: time.dayofweek)
    MyRawData['Hour'] = MyRawData['Gmt time'].str[11:13]
    MyRawData['Minute'] = MyRawData['Gmt time'].str[14:16]

    #calclate candle size parameters in pips
    MyRawData['BodyPips'] = (abs(MyRawData['Open']-MyRawData['Close']) * 10000)
    MyRawData['WickUpPips'] = (abs(MyRawData['Open']-MyRawData['High']) * 10000)
    MyRawData['WickDownPips'] = (abs(MyRawData['Close']-MyRawData['Low']) * 10000)


    #calculate the candle type - undecision, buy , sell
    MyRawData.loc[MyRawData.BodyPips == 0, 'GreenOrRed?'] = 0
    MyRawData.loc[MyRawData.Open < MyRawData.Close, 'GreenOrRed?'] = 1
    MyRawData.loc[MyRawData.Open > MyRawData.Close, 'GreenOrRed?'] = 2


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
    MyFinalData = MyRawData[:-1]

    return MyFinalData


print(GetTheInput())