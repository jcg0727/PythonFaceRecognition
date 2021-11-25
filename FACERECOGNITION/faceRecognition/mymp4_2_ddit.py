import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0


print("x_train",len(x_train))
print("y_train",len(y_train))
print("x_test",len(x_test))
print("y_test",len(y_test))

print("x_train",x_train[0].shape)
print("y_train",y_train[0].shape)
print("x_test",x_test[0].shape)
print("y_test",y_test[0].shape)

print("x_train",x_train.shape)
print("y_train",y_train.shape)
print("x_test",x_test.shape)
print("y_test",y_test.shape)


print("x_train",x_train[0])
print("y_train",y_train[0])
print("x_test",x_test[0])
print("y_test",y_test[0])

print("y_train",y_train)
print("y_test",y_test)

print("y_train",y_train.shape)
print("y_test",y_test.shape)
 