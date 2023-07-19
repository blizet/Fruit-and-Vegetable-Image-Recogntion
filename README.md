# Fruit Recognition with Image Analysis

This project utilizes image recognition techniques to detect fruits in uploaded files and retrieve corresponding data from a MySQL database. The core functionality is implemented in the `impor.py` file, which includes functions for handling image identification. The trained model, `FV.h5`, is loaded in this file for accurate fruit detection.

## Image Recognition and Trained Model

The `FV.h5` file represents a trained model that has been extensively trained on a diverse dataset of fruit images. It incorporates machine learning or deep learning techniques to learn patterns and features necessary for accurate fruit identification. This model is used to make predictions and classify fruits in uploaded images.

## Graphical User Interface (GUI) and Application Flow

The main file of the application, `App.py`, combines the functionality from `impor.py` with the Tkinter library to create a user-friendly GUI. The GUI enables users to upload an image file, which is then processed by the image recognition functions from `impor.py`. These functions preprocess the image, extract features, and apply the trained model to make predictions about the detected fruit.

MySQL Database Integration

Upon fruit detection, the application retrieves additional information about the recognized fruit from a MySQL database. This information can include the fruit's name, nutritional facts, or any other relevant details stored in the database. By leveraging the database, comprehensive information about the recognized fruit is provided to the user.

## Requirements and Usage

The application requires Python version 3.6.7 and pip version 21.3.1 to run correctly. The GUI created using Tkinter provides an intuitive interface where users can upload their images, view the results of fruit detection, and access the associated data from the MySQL database.

Please refer to the documentation or instructions provided in the repository to set up the necessary dependencies, configure the MySQL database, and run the application successfully.

## Conclusion

By combining image recognition techniques, a trained model, and integration with a MySQL database, this project provides a robust solution for fruit detection and retrieval of related data. The GUI enhances user experience and facilitates the seamless interaction with the application.
