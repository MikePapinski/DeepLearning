# # # View on GitHub
# # # Home
# # # Documentation

################### https://mrjbq7.github.io/ta-lib/func.html #######################

# # # TA-Lib
# # # Python wrapper for TA-Lib (http://ta-lib.org/).
# # # Download this project as a .zip fileDownload this project as a tar.gz file
# # # Momentum Indicator Functions
# # # ADX - Average Directional Movement Index
# # # NOTE: The ADX function has an unstable period.

# # # real = ADX(high, low, close, timeperiod=14)
# # # Learn more about the Average Directional Movement Index at tadoc.org.

# # # ADXR - Average Directional Movement Index Rating
# # # NOTE: The ADXR function has an unstable period.

# # # real = ADXR(high, low, close, timeperiod=14)
# # # Learn more about the Average Directional Movement Index Rating at tadoc.org.

# # # APO - Absolute Price Oscillator
# # # real = APO(close, fastperiod=12, slowperiod=26, matype=0)
# # # Learn more about the Absolute Price Oscillator at tadoc.org.

# # # AROON - Aroon
# # # aroondown, aroonup = AROON(high, low, timeperiod=14)
# # # Learn more about the Aroon at tadoc.org.

# # # AROONOSC - Aroon Oscillator
# # # real = AROONOSC(high, low, timeperiod=14)
# # # Learn more about the Aroon Oscillator at tadoc.org.

# # # BOP - Balance Of Power
# # # real = BOP(open, high, low, close)
# # # Learn more about the Balance Of Power at tadoc.org.

# # # CCI - Commodity Channel Index
# # # real = CCI(high, low, close, timeperiod=14)
# # # Learn more about the Commodity Channel Index at tadoc.org.

# # # CMO - Chande Momentum Oscillator
# # # NOTE: The CMO function has an unstable period.

# # # real = CMO(close, timeperiod=14)
# # # Learn more about the Chande Momentum Oscillator at tadoc.org.

# # # DX - Directional Movement Index
# # # NOTE: The DX function has an unstable period.

# # # real = DX(high, low, close, timeperiod=14)
# # # Learn more about the Directional Movement Index at tadoc.org.

# # # MACD - Moving Average Convergence/Divergence
# # # macd, macdsignal, macdhist = MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
# # # Learn more about the Moving Average Convergence/Divergence at tadoc.org.

# # # MACDEXT - MACD with controllable MA type
# # # macd, macdsignal, macdhist = MACDEXT(close, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0)
# # # MACDFIX - Moving Average Convergence/Divergence Fix 12/26
# # # macd, macdsignal, macdhist = MACDFIX(close, signalperiod=9)
# # # MFI - Money Flow Index
# # # NOTE: The MFI function has an unstable period.

# # # real = MFI(high, low, close, volume, timeperiod=14)
# # # Learn more about the Money Flow Index at tadoc.org.

# # # MINUS_DI - Minus Directional Indicator
# # # NOTE: The MINUS_DI function has an unstable period.

# # # real = MINUS_DI(high, low, close, timeperiod=14)
# # # Learn more about the Minus Directional Indicator at tadoc.org.

# # # MINUS_DM - Minus Directional Movement
# # # NOTE: The MINUS_DM function has an unstable period.

# # # real = MINUS_DM(high, low, timeperiod=14)
# # # Learn more about the Minus Directional Movement at tadoc.org.

# # # MOM - Momentum
# # # real = MOM(close, timeperiod=10)
# # # Learn more about the Momentum at tadoc.org.

# # # PLUS_DI - Plus Directional Indicator
# # # NOTE: The PLUS_DI function has an unstable period.

# # # real = PLUS_DI(high, low, close, timeperiod=14)
# # # Learn more about the Plus Directional Indicator at tadoc.org.

# # # PLUS_DM - Plus Directional Movement
# # # NOTE: The PLUS_DM function has an unstable period.

# # # real = PLUS_DM(high, low, timeperiod=14)
# # # Learn more about the Plus Directional Movement at tadoc.org.

# # # PPO - Percentage Price Oscillator
# # # real = PPO(close, fastperiod=12, slowperiod=26, matype=0)
# # # Learn more about the Percentage Price Oscillator at tadoc.org.

# # # ROC - Rate of change : ((price/prevPrice)-1)*100
# # # real = ROC(close, timeperiod=10)
# # # Learn more about the Rate of change : ((price/prevPrice)-1)*100 at tadoc.org.

# # # ROCP - Rate of change Percentage: (price-prevPrice)/prevPrice
# # # real = ROCP(close, timeperiod=10)
# # # Learn more about the Rate of change Percentage: (price-prevPrice)/prevPrice at tadoc.org.

# # # ROCR - Rate of change ratio: (price/prevPrice)
# # # real = ROCR(close, timeperiod=10)
# # # Learn more about the Rate of change ratio: (price/prevPrice) at tadoc.org.

# # # ROCR100 - Rate of change ratio 100 scale: (price/prevPrice)*100
# # # real = ROCR100(close, timeperiod=10)
# # # Learn more about the Rate of change ratio 100 scale: (price/prevPrice)*100 at tadoc.org.

# # # RSI - Relative Strength Index
# # # NOTE: The RSI function has an unstable period.

# # # real = RSI(close, timeperiod=14)
# # # Learn more about the Relative Strength Index at tadoc.org.

# # # STOCH - Stochastic
# # # slowk, slowd = STOCH(high, low, close, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
# # # Learn more about the Stochastic at tadoc.org.

# # # STOCHF - Stochastic Fast
# # # fastk, fastd = STOCHF(high, low, close, fastk_period=5, fastd_period=3, fastd_matype=0)
# # # Learn more about the Stochastic Fast at tadoc.org.

# # # STOCHRSI - Stochastic Relative Strength Index
# # # NOTE: The STOCHRSI function has an unstable period.

# # # fastk, fastd = STOCHRSI(close, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
# # # Learn more about the Stochastic Relative Strength Index at tadoc.org.

# # # TRIX - 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
# # # real = TRIX(close, timeperiod=30)
# # # Learn more about the 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA at tadoc.org.

# # # ULTOSC - Ultimate Oscillator
# # # real = ULTOSC(high, low, close, timeperiod1=7, timeperiod2=14, timeperiod3=28)
# # # Learn more about the Ultimate Oscillator at tadoc.org.

# # # WILLR - Williams' %R
# # # real = WILLR(high, low, close, timeperiod=14)
# # # Learn more about the Williams' %R at tadoc.org.

# # # Documentation Index All Function Groups

# # # TA-Lib written by mrjbq7 and contributors

# # # Published with GitHub Pages


# # View on GitHub
# # Home
# # Documentation

# # TA-Lib
# # Python wrapper for TA-Lib (http://ta-lib.org/).
# # Download this project as a .zip fileDownload this project as a tar.gz file
# # Pattern Recognition Functions
# # CDL2CROWS - Two Crows
# # integer = CDL2CROWS(open, high, low, close)
# # CDL3BLACKCROWS - Three Black Crows
# # integer = CDL3BLACKCROWS(open, high, low, close)
# # CDL3INSIDE - Three Inside Up/Down
# # integer = CDL3INSIDE(open, high, low, close)
# # CDL3LINESTRIKE - Three-Line Strike
# # integer = CDL3LINESTRIKE(open, high, low, close)
# # CDL3OUTSIDE - Three Outside Up/Down
# # integer = CDL3OUTSIDE(open, high, low, close)
# # CDL3STARSINSOUTH - Three Stars In The South
# # integer = CDL3STARSINSOUTH(open, high, low, close)
# # CDL3WHITESOLDIERS - Three Advancing White Soldiers
# # integer = CDL3WHITESOLDIERS(open, high, low, close)
# # CDLABANDONEDBABY - Abandoned Baby
# # integer = CDLABANDONEDBABY(open, high, low, close, penetration=0)
# # CDLADVANCEBLOCK - Advance Block
# # integer = CDLADVANCEBLOCK(open, high, low, close)
# # CDLBELTHOLD - Belt-hold
# # integer = CDLBELTHOLD(open, high, low, close)
# # CDLBREAKAWAY - Breakaway
# # integer = CDLBREAKAWAY(open, high, low, close)
# # CDLCLOSINGMARUBOZU - Closing Marubozu
# # integer = CDLCLOSINGMARUBOZU(open, high, low, close)
# # CDLCONCEALBABYSWALL - Concealing Baby Swallow
# # integer = CDLCONCEALBABYSWALL(open, high, low, close)
# # CDLCOUNTERATTACK - Counterattack
# # integer = CDLCOUNTERATTACK(open, high, low, close)
# # CDLDARKCLOUDCOVER - Dark Cloud Cover
# # integer = CDLDARKCLOUDCOVER(open, high, low, close, penetration=0)
# # CDLDOJI - Doji
# # integer = CDLDOJI(open, high, low, close)
# # CDLDOJISTAR - Doji Star
# # integer = CDLDOJISTAR(open, high, low, close)
# # CDLDRAGONFLYDOJI - Dragonfly Doji
# # integer = CDLDRAGONFLYDOJI(open, high, low, close)
# # CDLENGULFING - Engulfing Pattern
# # integer = CDLENGULFING(open, high, low, close)
# # CDLEVENINGDOJISTAR - Evening Doji Star
# # integer = CDLEVENINGDOJISTAR(open, high, low, close, penetration=0)
# # CDLEVENINGSTAR - Evening Star
# # integer = CDLEVENINGSTAR(open, high, low, close, penetration=0)
# # CDLGAPSIDESIDEWHITE - Up/Down-gap side-by-side white lines
# # integer = CDLGAPSIDESIDEWHITE(open, high, low, close)
# # CDLGRAVESTONEDOJI - Gravestone Doji
# # integer = CDLGRAVESTONEDOJI(open, high, low, close)
# # CDLHAMMER - Hammer
# # integer = CDLHAMMER(open, high, low, close)
# # CDLHANGINGMAN - Hanging Man
# # integer = CDLHANGINGMAN(open, high, low, close)
# # CDLHARAMI - Harami Pattern
# # integer = CDLHARAMI(open, high, low, close)
# # CDLHARAMICROSS - Harami Cross Pattern
# # integer = CDLHARAMICROSS(open, high, low, close)
# # CDLHIGHWAVE - High-Wave Candle
# # integer = CDLHIGHWAVE(open, high, low, close)
# # CDLHIKKAKE - Hikkake Pattern
# # integer = CDLHIKKAKE(open, high, low, close)
# # CDLHIKKAKEMOD - Modified Hikkake Pattern
# # integer = CDLHIKKAKEMOD(open, high, low, close)
# # CDLHOMINGPIGEON - Homing Pigeon
# # integer = CDLHOMINGPIGEON(open, high, low, close)
# # CDLIDENTICAL3CROWS - Identical Three Crows
# # integer = CDLIDENTICAL3CROWS(open, high, low, close)
# # CDLINNECK - In-Neck Pattern
# # integer = CDLINNECK(open, high, low, close)
# # CDLINVERTEDHAMMER - Inverted Hammer
# # integer = CDLINVERTEDHAMMER(open, high, low, close)
# # CDLKICKING - Kicking
# # integer = CDLKICKING(open, high, low, close)
# # CDLKICKINGBYLENGTH - Kicking - bull/bear determined by the longer marubozu
# # integer = CDLKICKINGBYLENGTH(open, high, low, close)
# # CDLLADDERBOTTOM - Ladder Bottom
# # integer = CDLLADDERBOTTOM(open, high, low, close)
# # CDLLONGLEGGEDDOJI - Long Legged Doji
# # integer = CDLLONGLEGGEDDOJI(open, high, low, close)
# # CDLLONGLINE - Long Line Candle
# # integer = CDLLONGLINE(open, high, low, close)
# # CDLMARUBOZU - Marubozu
# # integer = CDLMARUBOZU(open, high, low, close)
# # CDLMATCHINGLOW - Matching Low
# # integer = CDLMATCHINGLOW(open, high, low, close)
# # CDLMATHOLD - Mat Hold
# # integer = CDLMATHOLD(open, high, low, close, penetration=0)
# # CDLMORNINGDOJISTAR - Morning Doji Star
# # integer = CDLMORNINGDOJISTAR(open, high, low, close, penetration=0)
# # CDLMORNINGSTAR - Morning Star
# # integer = CDLMORNINGSTAR(open, high, low, close, penetration=0)
# # CDLONNECK - On-Neck Pattern
# # integer = CDLONNECK(open, high, low, close)
# # CDLPIERCING - Piercing Pattern
# # integer = CDLPIERCING(open, high, low, close)
# # CDLRICKSHAWMAN - Rickshaw Man
# # integer = CDLRICKSHAWMAN(open, high, low, close)
# # CDLRISEFALL3METHODS - Rising/Falling Three Methods
# # integer = CDLRISEFALL3METHODS(open, high, low, close)
# # CDLSEPARATINGLINES - Separating Lines
# # integer = CDLSEPARATINGLINES(open, high, low, close)
# # CDLSHOOTINGSTAR - Shooting Star
# # integer = CDLSHOOTINGSTAR(open, high, low, close)
# # CDLSHORTLINE - Short Line Candle
# # integer = CDLSHORTLINE(open, high, low, close)
# # CDLSPINNINGTOP - Spinning Top
# # integer = CDLSPINNINGTOP(open, high, low, close)
# # CDLSTALLEDPATTERN - Stalled Pattern
# # integer = CDLSTALLEDPATTERN(open, high, low, close)
# # CDLSTICKSANDWICH - Stick Sandwich
# # integer = CDLSTICKSANDWICH(open, high, low, close)
# # CDLTAKURI - Takuri (Dragonfly Doji with very long lower shadow)
# # integer = CDLTAKURI(open, high, low, close)
# # CDLTASUKIGAP - Tasuki Gap
# # integer = CDLTASUKIGAP(open, high, low, close)
# # CDLTHRUSTING - Thrusting Pattern
# # integer = CDLTHRUSTING(open, high, low, close)
# # CDLTRISTAR - Tristar Pattern
# # integer = CDLTRISTAR(open, high, low, close)
# # CDLUNIQUE3RIVER - Unique 3 River
# # integer = CDLUNIQUE3RIVER(open, high, low, close)
# # CDLUPSIDEGAP2CROWS - Upside Gap Two Crows
# # integer = CDLUPSIDEGAP2CROWS(open, high, low, close)
# # CDLXSIDEGAP3METHODS - Upside/Downside Gap Three Methods
# # integer = CDLXSIDEGAP3METHODS(open, high, low, close)
# # Documentation Index All Function Groups

# # TA-Lib written by mrjbq7 and contributors

# # Published with GitHub Pages



# View on GitHub
# Home
# Documentation

# TA-Lib
# Python wrapper for TA-Lib (http://ta-lib.org/).
# Download this project as a .zip fileDownload this project as a tar.gz file
# Overlap Studies Functions
# BBANDS - Bollinger Bands
# upperband, middleband, lowerband = BBANDS(close, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
# Learn more about the Bollinger Bands at tadoc.org.

# DEMA - Double Exponential Moving Average
# real = DEMA(close, timeperiod=30)
# Learn more about the Double Exponential Moving Average at tadoc.org.

# EMA - Exponential Moving Average
# NOTE: The EMA function has an unstable period.

# real = EMA(close, timeperiod=30)
# Learn more about the Exponential Moving Average at tadoc.org.

# HT_TRENDLINE - Hilbert Transform - Instantaneous Trendline
# NOTE: The HT_TRENDLINE function has an unstable period.

# real = HT_TRENDLINE(close)
# Learn more about the Hilbert Transform - Instantaneous Trendline at tadoc.org.

# KAMA - Kaufman Adaptive Moving Average
# NOTE: The KAMA function has an unstable period.

# real = KAMA(close, timeperiod=30)
# Learn more about the Kaufman Adaptive Moving Average at tadoc.org.

# MA - Moving average
# real = MA(close, timeperiod=30, matype=0)
# MAMA - MESA Adaptive Moving Average
# NOTE: The MAMA function has an unstable period.

# mama, fama = MAMA(close, fastlimit=0, slowlimit=0)
# Learn more about the MESA Adaptive Moving Average at tadoc.org.

# MAVP - Moving average with variable period
# real = MAVP(close, periods, minperiod=2, maxperiod=30, matype=0)
# MIDPOINT - MidPoint over period
# real = MIDPOINT(close, timeperiod=14)
# Learn more about the MidPoint over period at tadoc.org.

# MIDPRICE - Midpoint Price over period
# real = MIDPRICE(high, low, timeperiod=14)
# Learn more about the Midpoint Price over period at tadoc.org.

# SAR - Parabolic SAR
# real = SAR(high, low, acceleration=0, maximum=0)
# Learn more about the Parabolic SAR at tadoc.org.

# SAREXT - Parabolic SAR - Extended
# real = SAREXT(high, low, startvalue=0, offsetonreverse=0, accelerationinitlong=0, accelerationlong=0, accelerationmaxlong=0, accelerationinitshort=0, accelerationshort=0, accelerationmaxshort=0)
# SMA - Simple Moving Average
# real = SMA(close, timeperiod=30)
# Learn more about the Simple Moving Average at tadoc.org.

# T3 - Triple Exponential Moving Average (T3)
# NOTE: The T3 function has an unstable period.

# real = T3(close, timeperiod=5, vfactor=0)
# Learn more about the Triple Exponential Moving Average (T3) at tadoc.org.

# TEMA - Triple Exponential Moving Average
# real = TEMA(close, timeperiod=30)
# Learn more about the Triple Exponential Moving Average at tadoc.org.

# TRIMA - Triangular Moving Average
# real = TRIMA(close, timeperiod=30)
# Learn more about the Triangular Moving Average at tadoc.org.

# WMA - Weighted Moving Average
# real = WMA(close, timeperiod=30)
# Learn more about the Weighted Moving Average at tadoc.org.

# Documentation Index All Function Groups

# TA-Lib written by mrjbq7 and contributors

# Published with GitHub Pages