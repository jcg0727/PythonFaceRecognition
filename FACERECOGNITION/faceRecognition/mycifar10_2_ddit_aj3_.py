import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

x_train = np.load('x_train.npy')
y_train = np.load('y_train.npy')

print(x_train.shape)
print(x_train[0])


inputs = keras.Input(shape=(64, 64, 3))
x = inputs
x = layers.Conv2D(64, 3, activation='relu', padding="same")(x)
x = layers.Conv2D(64, 3, activation='relu', padding="same")(x)
x = layers.MaxPooling2D(2)(x)
x = layers.Conv2D(128, 3, activation='relu', padding="same")(x)
x = layers.Conv2D(128, 3, activation='relu', padding="same")(x)
x = layers.MaxPooling2D(2)(x)
x = layers.Conv2D(256, 3, activation='relu', padding="same")(x)
x = layers.Conv2D(256, 3, activation='relu', padding="same")(x)
x = layers.MaxPooling2D(2)(x)
  
x = layers.Flatten()(x)
x = layers.Dense(256)(x)
x = layers.Dense(256)(x)
x = layers.Dense(12, activation='softmax')(x)
outputs = x
  
model = keras.Model(inputs, outputs)
model.summary()
  
  
#   48+68 116

  
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=20)
model.save("my_brain.h5")
