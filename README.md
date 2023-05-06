In this project, I have used image recognition to detect fruit in uploaded files and retrieve data about the fruit from a MySQL database. To accomplish this, I created a file called impor.py, which contains functions that handle the image identification process. Inside this file, I loaded a trained model called FV.h5, which is crucial for fruit detection.

The FV.h5 file represents a model that has been trained using machine learning or deep learning techniques. It has been specifically trained on a large dataset of fruit images to learn patterns and features necessary for accurate fruit identification. This trained model will be used to make predictions and classify the fruits in the uploaded images.

In the main file of the application, App.py, I combined the functionality from impor.py with the Tkinter library to create a graphical user interface (GUI). The GUI allows users to upload an image file, which is then passed to the image recognition functions from impor.py. The functions in impor.py preprocess the image, extract features, and apply the trained model to make predictions about the detected fruit.

Once the fruit is detected, the application retrieves additional information about the fruit from a MySQL database. This information could include the fruit's name, nutritional facts, or any other relevant details stored in the database. By leveraging the database, I can provide users with comprehensive information about the recognized fruit.

It's important to note that the application requires Python version 3.6.7 and pip version 21.3.1 to run properly. The GUI created using Tkinter provides a user-friendly interface where users can upload their images, view the results of fruit detection, and access the associated data from the MySQL database.
