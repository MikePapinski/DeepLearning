#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:

#DIR='D:\Users\Mike\Desktop\New folder (4)\Machine-Learning-Projects\FirstNeuralNetwork'
#df = pd.read_csv('FRESHTEST.csv')
DIR='Machine-Learning-Projects/FirstNeuralNetwork'
df = pd.read_csv(DIR+'/FRESHTEST.csv', delimiter=',')

# In[3]:


df


# In[4]:


dataset = df.values


# In[5]:


dataset


# In[6]:


X = dataset[:,0:4]


# In[7]:


Y = dataset[:,4]


# In[14]:


X


# In[15]:


Y


# In[16]:


from sklearn import preprocessing


# In[17]:


min_max_scaler = preprocessing.MinMaxScaler()
X_scale = min_max_scaler.fit_transform(X)


# In[18]:


X_scale


# In[19]:


from sklearn.model_selection import train_test_split


# In[20]:


X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X_scale, Y, test_size=0.3)


# In[21]:


X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size=0.5)


# In[22]:


print(X_train.shape, X_val.shape, X_test.shape, Y_train.shape, Y_val.shape, Y_test.shape)


# In[23]:


from keras.models import Sequential
from keras.layers import Dense


# In[24]:


model = Sequential([
    Dense(50, activation='relu', input_shape=(4,)),
    Dense(50, activation='relu'),
    Dense(1, activation='sigmoid'),
])


# In[25]:


model.compile(optimizer='sgd',
              loss='binary_crossentropy',
              metrics=['accuracy'])


# In[ ]:


hist = model.fit(X_train, Y_train,
          batch_size=4, epochs=200000,
          validation_data=(X_val, Y_val))


# In[226]:


model.evaluate(X_test, Y_test)[1]


# In[227]:


import matplotlib.pyplot as plt


# In[228]:


plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Val'], loc='upper right')
plt.show()


# In[229]:


plt.plot(hist.history['acc'])
plt.plot(hist.history['val_acc'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Val'], loc='lower right')
plt.show()


# In[230]:


model_2 = Sequential([
    Dense(1000, activation='relu', input_shape=(4,)),
    Dense(1000, activation='relu'),
    Dense(1000, activation='relu'),
    Dense(1000, activation='relu'),
    Dense(1, activation='sigmoid'),
])
model_2.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
hist_2 = model_2.fit(X_train, Y_train,
          batch_size=36, epochs=200,
          validation_data=(X_val, Y_val))


# In[231]:


plt.plot(hist_2.history['loss'])
plt.plot(hist_2.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Val'], loc='upper right')
plt.show()


# In[232]:


plt.plot(hist_2.history['acc'])
plt.plot(hist_2.history['val_acc'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Val'], loc='lower right')
plt.show()


# In[233]:


from keras.layers import Dropout
from keras import regularizers


# In[234]:


model_3 = Sequential([
    Dense(1000, activation='relu', kernel_regularizer=regularizers.l2(0.01), input_shape=(4,)),
    Dropout(0.3),
    Dense(1000, activation='relu', kernel_regularizer=regularizers.l2(0.01)),
    Dropout(0.3),
    Dense(1000, activation='relu', kernel_regularizer=regularizers.l2(0.01)),
    Dropout(0.3),
    Dense(1000, activation='relu', kernel_regularizer=regularizers.l2(0.01)),
    Dropout(0.3),
    Dense(1, activation='sigmoid', kernel_regularizer=regularizers.l2(0.01)),
])


# In[235]:


model_3.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
hist_3 = model_3.fit(X_train, Y_train,
          batch_size=36, epochs=200,
          validation_data=(X_val, Y_val))


# In[236]:


plt.plot(hist_3.history['loss'])
plt.plot(hist_3.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Val'], loc='upper right')
plt.ylim(top=1.2, bottom=0)
plt.show()


# In[237]:


plt.plot(hist_3.history['acc'])
plt.plot(hist_3.history['val_acc'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Val'], loc='lower right')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




