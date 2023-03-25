import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


# DATA PROCESSING
# Training image preprocessing

training_set=tf.keras.utils.image_dataset_from_directory(
    '/train',
    labels='inferred',
    label_mode='categorical',
    class_names=None,
    color_mode='rgb',
    batch_size=32,
    image_size=(64,64),
    shuffle=True,
    seed= None,
    validation_split=None,
    subset=None,
    interpolation='bilinear',
    follow_links=False,
    crop_to_aspect_ratio=False
    
)

#VALICATION IMAGE PREPROCESSING

validation_set=tf.keras.utils.image_dataset_from_directory(
    '/test',
    labels='inferred',
    label_mode='categorical',
    class_names=None,
    color_mode='rgb',
    batch_size=32,
    image_size=(64,64),
    shuffle=True,
    seed= None,
    validation_split=None,
    subset=None,
    interpolation='bilinear',
    follow_links=False,
    crop_to_aspect_ratio=False
    
)

#BUILDING MODEL


cnn= tf.keras.Sequentials()

#BULIDING CONVOLAUTION LAYER

cnn.add(tf.keras.layers.Conv2D(filters=64,kernel_size=3,activation='relu',input_shape=[64,64,3]))
cnn.add(tf.keras.layers.MaxPool12D(pool_size=2,strides=2))

cnn.add(tf.keras.layers.Conv2D(filters=64,kernel_size=3,activation='relu'))
cnn.add(tf.keras.layers.MaxPool12D(pool_size=2,strides=2)) 

cnn.add(tf.keras.layers.Dropout(0.5))#to avoid overfitting

cnn.add(tf.keras.layers.Flaten())

cnn.add(tf.keras.layers.Dense(units=128,activation='relu'))
#output layer
cnn.add(tf.keras.layers.Dense(units=36,activation='softmax'))

#COMPILATION AND TRAINING PHASE
cnn.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])
training_history=cnn.fit(x=training_set,validation_data=validation_set,epochs=30)

#SAVING MODEL

cnn.save('trained_model.h5')
training_history.history#return disctonry of history
#record history in json

import json
with open('training_hist.json','w') as f:
    json.dump(training_history.history,f)

#Calculating accuracy of model achieved on validation set

print("Validation set Accuracy: {} %".format(training_history.history['val_accuracy'][-1]*100))

#Accuracy visualization
#Training visualization

epochs = [i for i in range(1,31)]
plt.plot(epochs,training_history.history['accuracy'],color='red')
plt.xlabel('Epochs')
plt.ylabel('Training Accuracy')
plt.title('Visualixation of Training Accuracy')
plt.show()

#Validation Accuracy
plt.plot(epochs,training_history['val_accuracy'],color='blue')
plt.xlabel('No. of Epochs')
plt.ylabel('validation accuracy')
plt.title('Vizualization of Validation Accuracy Result')
plt.show()



