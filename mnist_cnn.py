# mnist_cnn.py
# Deep Learning Midterm Project – Handwritten Digit Classification
# AI 100 – 2/16/2026
# Author: Nethra S.

import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.utils import to_categorical

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize pixel values
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# Reshape for CNN input (samples, height, width, channels)
x_train_cnn = x_train.reshape(-1, 28, 28, 1)
x_test_cnn = x_test.reshape(-1, 28, 28, 1)

# One-hot encode labels
y_train_cat = to_categorical(y_train, 10)
y_test_cat = to_categorical(y_test, 10)

# -----------------------------
# 1. Convolutional Neural Network
# -----------------------------
cnn_model = Sequential([
    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28,28,1)),
    MaxPooling2D(pool_size=(2,2)),
    Conv2D(64, kernel_size=(3,3), activation='relu'),
    MaxPooling2D(pool_size=(2,2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

cnn_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
print("Training CNN model...")
cnn_model.fit(x_train_cnn, y_train_cat, epochs=5, batch_size=64, verbose=2)
cnn_loss, cnn_acc = cnn_model.evaluate(x_test_cnn, y_test_cat, verbose=0)
print(f"CNN Test Accuracy: {cnn_acc*100:.2f}%")

# -----------------------------
# 2. Fully Connected Dense Network
# -----------------------------
# Flatten input for Dense model
x_train_dense = x_train.reshape(-1, 28*28)
x_test_dense = x_test.reshape(-1, 28*28)

dense_model = Sequential([
    Dense(256, activation='relu', input_shape=(28*28,)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

dense_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
print("Training Dense model...")
dense_model.fit(x_train_dense, y_train_cat, epochs=5, batch_size=64, verbose=2)
dense_loss, dense_acc = dense_model.evaluate(x_test_dense, y_test_cat, verbose=0)
print(f"Dense Model Test Accuracy: {dense_acc*100:.2f}%")
