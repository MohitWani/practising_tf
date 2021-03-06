# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14auWEE-niD2hgLyDtzSm2U-L29Q8FL4U

##Importing libraries
"""

import tensorflow as tf
import numpy as np

"""##loading dataset"""

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train/255.0, x_test/255.0

"""##Build a machine learning model"""

model = tf.keras.models.Sequential([
                                    tf.keras.layers.Flatten(input_shape=(28,28)),
                                    tf.keras.layers.Dense(128, activation='relu'),
                                    tf.keras.layers.Dropout(0.2),
                                    tf.keras.layers.Dense(10)

])

prediction = model(x_train[:1]).numpy()
prediction

tf.nn.softmax(prediction).numpy()

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

loss_fn(y_train[:1], prediction).numpy()

model.compile(optimizer='adam',
              loss= loss_fn,
              metrics= ['accuracy']
)

model.fit(x_train, y_train, epochs=5)

model.evaluate(x_test, y_test, verbose=2)

probability_model = tf.keras.Sequential([
                                         model,
                                         tf.keras.layers.Softmax()
])

probability_model(x_test[:5])

