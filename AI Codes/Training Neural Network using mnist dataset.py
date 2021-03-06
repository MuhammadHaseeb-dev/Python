from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

#loading train and test data
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

#making network architecture
network = models.Sequential()
network.add(layers.Dense(512,activation="relu",input_shape=(28*28,)))
network.add(layers.Dense(10, activation='softmax'))

#specifying compile options for learning
network.compile(optimizer="rmsprop",loss="categorical_crossentropy",metrics=['accuracy'])

#applying data preprocessing
#limiting data range between 0 and 1
#one-hot-encoding
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

#preparing the lables
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

#train the network
network.fit(train_images, train_labels, epochs=5, batch_size=128)


#now evaluating the accuracy of trained model
test_loss, test_acc = network.evaluate(test_images, test_labels)
print('test accuracy of trained model:', test_acc)
