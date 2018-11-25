import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation
from keras.optimizers import Adam
from keras.callbacks import TensorBoard
import time


batch_size = 128
num_classes = 10
epochs = 10
time = time.strftime("%Y_%m_%d_%H_%M_%S")

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(60000,28,28,1)
x_test = x_test.reshape(10000,28,28,1)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

model = Sequential()

model.add(Conv2D(32, (3,3), padding="same", input_shape=(28,28,1), activation= "relu"))
model.add(MaxPooling2D(pool_size=(3, 3)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(128, activation="relu"))
model.add(Dropout(0.5))

model.add(Dense(num_classes, activation='softmax'))

kerasboard = TensorBoard(log_dir="/tmp/tensorboard/{}".format(time),
                        batch_size=batch_size,
                        histogram_freq=1,
                        write_grads=True,
                        update_freq="epoch")

model.compile(loss="categorical_crossentropy",
              optimizer="adam",
              metrics=['accuracy'])

model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          validation_split=0.3,
          validation_data=(x_test, y_test),
          callbacks=[kerasboard])


print("tensorboard --logdir="+kerasboard.log_dir)