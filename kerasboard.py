# coding: utf-8

# In[1]:

import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import Adam
from keras.callbacks import TensorBoard
import time

# In[2]:

batch_size = 128
num_classes = 10
epochs = 1
time = time.strftime("%Y_%m_%d_%H_%M_%S")

# In[3]:

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# In[4]:

x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype("float32")
x_test = x_test.astype("float32")
x_train /= 255
x_test /= 255

# In[5]:

print(x_train.shape, "train samples")
print(x_test.shape, "test samples") 

# In[6]:

y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

# In[7]:

print(y_train.shape, "train samples")
print(y_test.shape, "test samples") 

# In[8]:

model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(784,),name="Input"))
#model.add(Dropout(0.2, name="Dropout1")) 
model.add(Dense(512, activation='relu', name="Hidden"))              
#model.add(Dropout(0.2, name="Dropout2"))
model.add(Dense(num_classes, activation='softmax', name="Output")) 

# In[9]:

model.summary()   

# In[10]:

model.compile(loss="categorical_crossentropy",
              optimizer="adam",
              metrics=["accuracy"])

# In[11]:

kerasboard = TensorBoard(log_dir="/tmp/tensorboard/{}".format(time),
                        batch_size=batch_size,
                        update_freq="batch")

# In[12]:

model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          validation_data=(x_test, y_test),
          shuffle=True,
          callbacks=[kerasboard])

# In[13]:

print("tensorboard --logdir="+kerasboard.log_dir)

