import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

#https://www.tensorflow.org/tutorials/keras/basic_classification

#preparing data
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
train_images = train_images / 255.0
test_images = test_images / 255.0

#preprocess data
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])

#building model
model = keras.Sequential([
            keras.layers.Flatten(input_shape=(28,28)), #1st layer, flatten image
            keras.layers.Dense(128, activation=tf.nn.relu), #2nd fully connected(dense) layer, 128 nodes
            keras.layers.Dense(64, activation=tf.nn.relu), #3rd fully connected(dense) layer, 128 nodes
            keras.layers.Dense(10, activation=tf.nn.softmax) #4th fully connected layer. 10 classes thus 10 nodes
            ]) 

#compile model
model.compile(
    optimizer=tf.train.AdamOptimizer(),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'])

print('training model')
model.fit(train_images, train_labels, epochs=7)

#evaluate accuracy
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('accuracy=', test_acc)

#predicting
predictions = model.predict(test_images)
print(predictions[0])
print(class_names[np.argmax(predictions[0])])