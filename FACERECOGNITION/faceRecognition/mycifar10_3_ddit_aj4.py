import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

x_train = np.load('x_train.npy')
y_train = np.load('y_train.npy')

print(x_train.shape)


model = tf.keras.models.load_model("my_ban.h5")

#3踰덉㎏�궗�엺�뜲�씠�꽣 -> 0,1,2
predictions = model.predict(x_train[108:109])
print(x_train[108:109].shape)
print(x_train[108:109])

print(np.argmax(predictions[0]))

