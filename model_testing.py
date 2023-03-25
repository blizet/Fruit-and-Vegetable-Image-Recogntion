import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#importing libraries
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import models
from tensorflow.keras import layers
import matplotlib.pyplot as plt
import cv2

#Connect to drive
#REMAINING

#loading model
cnn=tf.keras.models.load_model(r"C:\Users\HP\Desktop\pythonpro\trained_model.h5")

##Visualization and Performing Prediction on single image

image_path=''
imag =cv2.imread(image_path)

image=tf.keras.preprocessing.image.load_img(image_path,target_size=(64,64))
input_arr=tf.keras.preprocessing.image.img_to_array(image)
input_arr = np.array([input_arr]) #converting single image to batch
predictions =cnn.predict(input_arr)

print(predictions[0])
print(max(predictions[0]))

test_set=tf.keras.utils.image_dataset_from_directory(
    '/content/drive/MyDrive/Training_data/test',
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

result_index =np.where(predictions[0] ==max(predictions[0]))
print(result_index[0][0])

#Display Image


#Single prediction
print("It's a {}".format(test_set.class_names[result_index[0][0]]))


