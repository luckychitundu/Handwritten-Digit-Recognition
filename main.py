import cv2 as cv
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


data = tf.keras.datasets.mnist

(x_train,y_train),(x_test,y_test) = data.load_data()

x_train = tf.keras.utils.normalize(x_train,axis=1)
x_test = tf.keras.utils.normalize(x_test,axis=1)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
model.add(tf.keras.layers.Dense(units=128,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=128,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=10,activation=tf.nn.softmax))

model.compile(optimizer="adam",loss="sparse_categorical_crossentropy",metrics=["accuracy"])
model.fit(x_train,y_train,epochs=3)

loss,accuracy = model.evaluate(x_test,y_test)
print(f"Loss: {loss}")
print(f"Accuracy: {accuracy}")

for x in range(1,8):
    img = cv.imread(f"{x}.png")[:,:,0]
    img = np.invert(np.array([img]))
    prediction = model.predict(img)
    print("----------------------------------------")
    print("The number is probably ",np.argmax(prediction))
    print("----------------------------------------")
    plt.imshow(img[0],cmap=plt.cm.binary)
    plt.show()



