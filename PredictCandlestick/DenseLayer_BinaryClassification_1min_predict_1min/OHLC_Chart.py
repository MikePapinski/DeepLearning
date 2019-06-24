import pandas as pd
# import pandas_datareader as datareader
import matplotlib.pyplot as plt
import datetime
from mpl_finance import candlestick_ohlc
# from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
from PrepareTheData3 import GetTheInput_OHLC
from CustomIndicators import moving_average, relative_strength, moving_average_convergence

 
print('*** Program Started ***')



df = GetTheInput_OHLC()
prices = df['Close'].values
df['CandleCounter'] = range(len(df))

nslow = 26
nfast = 12
nema = 9
emaslow, emafast, macd = moving_average_convergence(prices, nslow=nslow, nfast=nfast)
ema9 = moving_average(macd, nema, type='exponential')
rsi = relative_strength(prices)

wins = 10000



# Creating required data in new DataFrame OHLC
ohlc= df[['CandleCounter', 'Open', 'High', 'Low','Close']]
ohlc =ohlc.tail(wins)

fig = plt.figure()


ax1 = plt.subplot2grid((8,1), (1,0), rowspan=4, colspan=4)
candlestick_ohlc(ax1, ohlc.values, width=.1, colorup='green', colordown='red')

# ### rsi

plt.subplot2grid((8, 1), (5, 0))
plt.plot(rsi[-wins:], color='black', lw=1)
plt.axhline(y=30,     color='red',   linestyle='-')
plt.axhline(y=70,     color='blue',  linestyle='-')


## MACD

plt.subplot2grid((8, 1), (6, 0))

plt.plot(ema9[-wins:], 'red', lw=1)
plt.plot(macd[-wins:], 'blue', lw=1)


#plt.subplot2grid((8, 1), (7, 0))

plt.plot(macd[-wins:]-ema9[-wins:], 'k', lw = 2)
plt.axhline(y=0, color='b', linestyle='-')



plt.show()



print('*** Program ended ***')
