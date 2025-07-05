

# 🍎 Fruit Recognition with Image Analysis and CNN

This project uses **Convolutional Neural Networks (CNNs)** to accurately detect fruits in uploaded images and retrieve additional information from a **MySQL database**. The primary model logic is contained in the `impor.py` file, and the user interface is built using Tkinter in `App.py`.

---

## 🧠 Image Recognition with CNN

The file `FV.h5` contains a pre-trained CNN model designed for classifying fruits based on image input. 

CNNs are a specialized type of deep learning architecture especially effective for image processing. They work by automatically learning to extract and recognize important features such as color, texture, and shape through layers of filters and pooling operations. This model was trained on a diverse dataset of fruit images, allowing it to generalize well across real-world input variations.

**Workflow:**

- Input image is resized and normalized.
- The CNN model (`FV.h5`) processes the image to identify key features.
- Based on learned patterns, the model classifies the fruit type.

---

## 📂 Project Structure

- `impor.py`: Handles image preprocessing, loads the trained CNN model, and returns predictions.
- `App.py`: Builds a GUI using Tkinter to allow image uploads and display predictions.
- `FV.h5`: Trained CNN model file used for image classification.
- **MySQL database**: Stores detailed fruit information (e.g., nutritional values, descriptions).

---

## 🖥️ Application Flow

1. User uploads an image through the GUI.
2. Image is passed to functions in `impor.py` for preprocessing and classification using the CNN model.
3. After classification, the application queries the MySQL database for additional information about the predicted fruit.
4. Results, including the fruit name and related data, are displayed in the GUI.

---

## ✅ Requirements

- Python 3.6.7
- pip 21.3.1
- TensorFlow / Keras
- MySQL Connector for Python
- Tkinter (for GUI functionality)

To install dependencies:

```bash
pip install -r requirements.txt
````

Set up the MySQL database as instructed in the setup guide before running the application.

---

## 🚀 Usage

1. Run `App.py`:

   ```bash
   python App.py
   ```
2. Upload an image using the interface.
3. View the detected fruit and its information retrieved from the database.

---

## 📌 Conclusion

This application combines the power of **CNN-based image recognition**, a **friendly graphical interface**, and **live database integration** to deliver an end-to-end fruit detection system. It’s ideal for educational demonstrations or as a foundation for more advanced image-based food analysis systems.

---

