from PrepareTheData3 import GetTheInput_Single
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
from sklearn import preprocessing
import numpy as np
import itertools


#***** Get the Values from Pandas *****
df = GetTheInput_Single()
dataset = df.values
X = dataset[:, 0:132]
Y = dataset[:, 132]
#**************************************


#********** Normalize the Input Values ************
min_max_scaler = preprocessing.MinMaxScaler()
X_scale = min_max_scaler.fit_transform(X)
#**************************************************


#********** Cut Values to 3 piecies ************
#Normalized
X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X_scale, Y, test_size=0.3)
X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size=0.5)
#Raw
X_train_Raw, X_val_and_test_Raw, Y_train_Raw, Y_val_and_test_Raw = train_test_split(X, Y, test_size=0.3)
X_val_Raw, X_test_Raw, Y_val_Raw, Y_test_Raw = train_test_split(X_val_and_test_Raw, Y_val_and_test_Raw, test_size=0.5)
#print(X_train.shape, X_val.shape, X_test.shape, Y_train.shape, Y_val.shape, Y_test.shape)
#***********************************************



#********** Build the Model and Compile ************
model = Sequential()
model.add(Dense(128, input_dim=132, kernel_initializer='normal', activation='relu'))
model.add(Dense(32, kernel_initializer='normal', activation='relu'))
model.add(Dense(16, kernel_initializer='normal', activation='relu'))
model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#***************************************************


#********** Train the Model ********************
hist = model.fit(X_train, Y_train,batch_size=10, epochs=5,validation_data=(X_val, Y_val))
#***********************************************


#********** Test the Model on New Data ********************
test_loss, test_acc = model.evaluate(X_test, Y_test)
print('Test accuracy:', test_acc)
#*********************************************************


#********** Perform predictions on new Dataset ********************
predictions = model.predict(X_test)
#******************************************************************


#********** Calculate the Stats ********************
# 1.Define stats variables
TotalTrades = 0
GoodTrades = 0
counter = 0
WeekDayStats = {'Monday':[0,0],'Tuesday':[0,0],'Wendsday':[0,0],'Thursday':[0,0],'Friday':[0,0]}
ConsequtiveStats = {'Won':0,'Lost':0}

PredictedResults = []

LastWon = False

# 2.Loop through predictions
for prediction_check in predictions:
    if prediction_check > 0.70 or prediction_check < 0.30:
        # Predictions above threshold

        TotalTrades = TotalTrades+1

        # Check if won or lost
        if np.argmax(predictions[counter]) == Y_test[counter]:
            # Won
            GoodTrades = GoodTrades + 1
            PredictedResults.append(1)
        else:
            # Lost
            PredictedResults.append(0)
    counter = counter + 1

# 3. Append stats variables
ConsequtiveStats['Won'] = max(len(list(PredictedResults)) for g,PredictedResults in itertools.groupby(1))
ConsequtiveStats['Lost'] = max(len(list(PredictedResults)) for g,PredictedResults in itertools.groupby(0))

print ('Trades: ' + str(TotalTrades) + ' -- ' + 'Good trades: ' + str(GoodTrades) + ' -- ' + 'Percantage: ' + str(round(((GoodTrades/TotalTrades)*100),2))+ '%')


#******************************************************************






#********** Create the Charts Dashboard ********************

# Chart 1 - Model Loss
plt.subplot(331)
plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Val'], loc='upper right')

# Chart 2 - Model Accuracy
plt.subplot(332)
plt.plot(hist.history['acc'])
plt.plot(hist.history['val_acc'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Val'], loc='lower right')
 
# Chart 3 - Lost and Won trades % above 70%
plt.subplot(333)
labels = 'WON', 'LOST'
sizes = [GoodTrades, (TotalTrades-GoodTrades)]
explode = (0, 0.1)  
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Predictions above 70% confidence')

# Chart 4 - Average Trades per week day
plt.subplot(334)
N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)

ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans, width)
p2 = plt.bar(ind, womenMeans, width)

plt.ylabel('Trades')
plt.title('Trades per Week Daay')
plt.xticks(ind, ('Monday', 'Tuesday', 'Wendsday', 'Thursday', 'Friday'))
plt.legend((p1[0], p2[0]), ('WON', 'LOST'))

# Chart 5 - Consequtive Losses and Wins
plt.subplot(335)
objects = ('Wins in a row', 'Loss in a row')
y_pos = np.arange(len(objects))
performance = [ConsequtiveStats['Won'],ConsequtiveStats['Lost']]

plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos, objects)
plt.xlabel('Trades')
plt.title('Consquituive Wins and Losses')


# Show the Charts Dashboard
plt.show()
#******************************************************************

