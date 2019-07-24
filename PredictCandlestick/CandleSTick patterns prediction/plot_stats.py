import matplotlib
import numpy as np
import pandas as pd
import datetime
import itertools

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc
import seaborn as sns


def get_win_loss_stat(alpha_distance,raw_predictions, target_predictions):
    counter = 0
    won = 0
    lost = 0
    for a in raw_predictions:
        if a > (1-alpha_distance) or a < alpha_distance :
            if (a > (1-alpha_distance) and target_predictions[counter] == 1) or (a < alpha_distance and target_predictions[counter] == 0):
                won=won+1
            else:
                lost=lost+1
        counter=counter+1
    return [won,lost]

def get_bullish_bearish_stat(alpha_distance,raw_predictions):
    bullish_count=0
    bearish_count=0
    for pred in raw_predictions:
        if pred < alpha_distance: bearish_count=bearish_count+1
        if pred > (1-alpha_distance): bullish_count=bullish_count+1
    return [bullish_count,bearish_count]

def get_consequitive_trades_stat(alpha_distance,raw_predictions,target_predictions):
    counter = 0
    ConsequtiveStats = []
    for a in raw_predictions:
            if a > (1-alpha_distance) or a < alpha_distance :
                if (a > (1-alpha_distance) and target_predictions[counter] == 1) or (a < alpha_distance and target_predictions[counter] == 0):
                    ConsequtiveStats.append(1)
                else:
                    ConsequtiveStats.append(0)
            counter=counter+1
    z = [(x[0], len(list(x[1]))) for x in itertools.groupby(ConsequtiveStats)]    
    MaxLost = 0
    MaxWon = 0
    for a in z:
        if a[0]==0:
            if a[1] > MaxLost: MaxLost = a[1]
        else:
            if a[1] > MaxWon: MaxWon = a[1]     
    return [MaxWon,MaxLost]

def get_trades_per_period_stat(alpha_distance,raw_predictions,timeperiod):
    output = []
    templist=[]
    addval=0
    counter=0
    for pre in raw_predictions:
        if counter % timeperiod == 0 and counter != 0 :
            output.append(sum(templist.copy()))
            templist=[]
        if pre < alpha_distance: addval = 1    
        elif pre > (1-alpha_distance): addval = 1
        else:
            addval = 0
        templist.append(addval)
        counter=counter+1
    return output

def get_week_activity(alpha_distance,raw_predictions,date_values):  
    Monday_ls = [0] * 24
    Tuesday_ls = [0] * 24
    Wendsday_ls = [0] * 24
    Thursday_ls = [0] * 24
    Friday_ls = [0] * 24

    counter = 0

    for a in raw_predictions:
        if a > (1-alpha_distance) or a < alpha_distance :
            raw_date_converted = datetime.datetime.strptime(date_values[counter], '%d.%m.%Y %H:%M:%S.000')
            week_day = raw_date_converted.weekday()
            hour = raw_date_converted.hour         
            if week_day==0: Monday_ls[hour-1]=Monday_ls[hour-1]+1
            if week_day==1: Tuesday_ls[hour-1]=Tuesday_ls[hour-1]+1
            if week_day==2: Wendsday_ls[hour-1]=Wendsday_ls[hour-1]+1
            if week_day==3: Thursday_ls[hour-1]=Thursday_ls[hour-1]+1
            if week_day==4: Friday_ls[hour-1]=Friday_ls[hour-1]+1
        counter=counter+1
        
    return [Monday_ls,Tuesday_ls,Wendsday_ls,Thursday_ls,Friday_ls]   

def get_model_insights(my_model,training_history,alpha_distance,X_input,Y_output,Y_datetimes):
    
    #Y_output
    raw_predictions=my_model.predict(X_input)
    if len(raw_predictions[0]) >1:
        new_predictions_raw = []
        new_Y_output = []
        for a in raw_predictions:
            new_predictions_raw.append(a[0])
        for b in Y_output:
            new_Y_output.append(b[0])
        raw_predictions=np.asarray(new_predictions_raw)
        Y_output=np.asarray(new_Y_output)
        
    split_time_period_month = 504
    split_time_period_week = 120
    split_time_period_day = 24
    
    won,lost = get_win_loss_stat(alpha_distance,raw_predictions, Y_output)
    bullish,bearish = get_bullish_bearish_stat(alpha_distance,raw_predictions)
    max_con_wins,max_con_lost = get_consequitive_trades_stat(alpha_distance,raw_predictions,Y_output)
    trades_per_month = get_trades_per_period_stat(alpha_distance,raw_predictions,split_time_period_month)
    trades_per_week = get_trades_per_period_stat(alpha_distance,raw_predictions,split_time_period_week)
    trades_per_day = get_trades_per_period_stat(alpha_distance,raw_predictions,split_time_period_day)
    
    week_activity=get_week_activity(alpha_distance,raw_predictions,Y_datetimes)
    
    
    # plot the charts
    plt.style.use('seaborn')
    f = plt.figure(figsize=(15,30))
    # model training loss function
    ax = f.add_subplot(621)
    ax.margins(0.1) 
    ax.plot(training_history.history['loss'])
    ax.plot(training_history.history['val_loss'])
    ax.set_title('Model loss')
    ax.set_ylabel('Loss')
    ax.set_xlabel('Epoch')
    ax.legend(['Train', 'Val'], loc='upper right')
    # model training accuracy
    ax2 = f.add_subplot(622)
    ax2.margins(0.1) 
    ax2.plot(training_history.history['acc'])
    ax2.plot(training_history.history['val_acc'])
    ax2.set_title('Model accuracy')
    ax2.set_ylabel('Accuracy')
    ax2.set_xlabel('Epoch')
    ax2.legend(['Train', 'Val'], loc='lower right')
    plt.show
    
    
    
    f = plt.figure(figsize=(15,5))
    ax3 = f.add_subplot(131)
    labels = 'WON', 'LOST'
    sizes = [won, lost]
    explode = (0, 0.1)  
    ax3.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
    ax3.set_title('Predictions above ' + str((round(1-alpha_distance,2)*100))  + '% confidence')
    ax3.legend(['WON', 'LOST'], loc='lower right')
    ax4 = f.add_subplot(132)
    labels = 'Bullish', 'Bearish'
    sizes = [bullish,bearish]
    explode = (0, 0.1)  
    ax4.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
    ax4.set_title('Bullish vs Bearish predictions')
    ax4.legend(['Bullish', 'Bearish'], loc='lower right')
    ax8 = f.add_subplot(133)
    ax8.set_title('Consequitive wins and losses in a row')
    x = ['Won','Lost']
    ax8.bar(x, [max_con_wins,max_con_lost])
    ax8.set_xticks(x, ('Won','Lost'))
    plt.show
    
    
    
    f = plt.figure(figsize=(15,10))
    ax5 = f.add_subplot(321)
    ax5.set_title('Trades per week')
    x = range(len(trades_per_week))
    ax5.bar(x, trades_per_week)
    weeks_with_trades = len(list(filter(lambda trades_per_week: trades_per_week > 0, trades_per_week)))
    weeks_with_zero_trades = len(list(filter(lambda trades_per_week: trades_per_week == 0, trades_per_week)))
    ax3 = f.add_subplot(322)
    labels = 'activity', 'no activity'
    sizes = [weeks_with_trades, weeks_with_zero_trades]
    explode = (0, 0.1)  
    ax3.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
    ax3.set_title('Weekly activity')

    
    
    ax6 = f.add_subplot(323)
    ax6.set_title('Trades per month')
    x = range(len(trades_per_month))
    ax6.bar(x, trades_per_month)
    months_with_trades = len(list(filter(lambda trades_per_month: trades_per_month > 0, trades_per_month)))
    months_with_zero_trades = len(list(filter(lambda trades_per_month: trades_per_month == 0, trades_per_month)))
    ax34 = f.add_subplot(324)
    labels = 'activity', 'no activity'
    sizes = [months_with_trades, months_with_zero_trades]
    explode = (0, 0.1)  
    ax34.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
    ax34.set_title('Monthly activity')

    
    ax7 = f.add_subplot(325)
    ax7.set_title('Trades per day')
    x = range(len(trades_per_day))
    ax7.bar(x, trades_per_day)
    days_with_trades = len(list(filter(lambda trades_per_day: trades_per_day > 0, trades_per_day)))
    days_with_zero_trades = len(list(filter(lambda trades_per_day: trades_per_day == 0, trades_per_day)))
    ax32 = f.add_subplot(326)
    labels = 'activity', 'no activity'
    sizes = [days_with_trades, days_with_zero_trades]
    explode = (0, 0.1)  
    ax32.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
    ax32.set_title('Daily activity')
    plt.show


    weekdays=['Monday','Tuesday','Wendsday','Thursday','Friday']
    plt.figure(figsize=(10,5))
    ax = sns.heatmap(week_activity,annot=True,annot_kws={"size": 15}, 
                        linewidth=0.5, yticklabels=weekdays,cmap="Blues")
    plt.title('Trade activity during the week')
    ax.set_ylabel('Week Days')
    ax.set_xlabel('Hours')
    
    plt.show
    
    return(True)
    
print('get_model_insights(my_model,training_history,alpha_distance,X_input,Y_output,Y_datetimes):')