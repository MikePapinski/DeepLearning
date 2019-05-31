from PrepareTheData3 import GetTheInput_Single
from sklearn.model_selection import train_test_split

from keras.models import Sequential
from keras.layers import Dense

import matplotlib.pyplot as plt
from sklearn import preprocessing


df = GetTheInput_Single()
dataset = df.values

X = dataset[:, 0:132]
Y = dataset[:, 132]

print('input:')
print(X)
print('output:')
print(Y)

min_max_scaler = preprocessing.MinMaxScaler()
X_scale = min_max_scaler.fit_transform(X)




X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X_scale, Y, test_size=0.3)

X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size=0.5)

print(X_train.shape, X_val.shape, X_test.shape, Y_train.shape, Y_val.shape, Y_test.shape)


model = Sequential()
model.add(Dense(128, input_dim=132, kernel_initializer='normal', activation='relu'))
model.add(Dense(32, kernel_initializer='normal', activation='relu'))
model.add(Dense(16, kernel_initializer='normal', activation='relu'))
model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))
	# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
	

# model.compile(optimizer='sgd',
#               loss='binary_crossentropy',
#               metrics=['accuracy'])


hist = model.fit(X_train, Y_train,
          batch_size=50, epochs=100,
          validation_data=(X_val, Y_val))


model.evaluate(X_test, Y_test)[1]

plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Val'], loc='upper right')
plt.show()


plt.plot(hist.history['acc'])
plt.plot(hist.history['val_acc'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Val'], loc='lower right')
plt.show()



