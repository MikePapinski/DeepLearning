from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from PrepareTheData import GetTheInput_Single, GetTheInput_Multiple
#import matplotlib.pyplot as plt


df = GetTheInput_Multiple()
dataset = df.values

X = dataset[:, 0:63]
Y = dataset[:, 63]

print('input:')
print(X)
print('output:')
print(Y)

min_max_scaler = preprocessing.MinMaxScaler()
X_scale = min_max_scaler.fit_transform(X)


X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X_scale, Y, test_size=0.3)

X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size=0.5)

print(X_train.shape, X_val.shape, X_test.shape, Y_train.shape, Y_val.shape, Y_test.shape)






# model = Sequential([
#     Dense(100, activation='relu', input_shape=(63,)),
#     Dense(200, activation='relu'),
#     Dense(100, activation='relu'),
#     Dense(1, activation='sigmoid'),
# ])

# model = Sequential()
# model.add(Dense(8, input_shape=(63,), activation='relu'))
# model.add(Dense(1, activation='softmax'))
# # Compile model
# model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
	

model = Sequential()
model.add(Dense(8, activation="relu", input_shape=(63,)))
model.add(Dense(1, activation="sigmoid"))

model.compile(loss='binary_crossentropy', optimizer='adam')
model.fit(X_train, Y_train, batch_size=1, epochs=1000)

# model.compile(optimizer='sgd',
#               loss='binary_crossentropy',
#               metrics=['accuracy'])


# hist = model.fit(X_train, Y_train,
#           batch_size=63, epochs=50,
#           validation_data=(X_val, Y_val))


model.evaluate(X_test, Y_test)[1]

