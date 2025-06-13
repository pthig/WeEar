import tensorflow as tf  # Install tensorflow
from keras.layers import TFSMLayer  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np
import time


# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the SavedModel as an inference-only layer
model = TFSMLayer("keras_Model", call_endpoint='serving_default')
# Example usage:
# import numpy as np
# input_data = np.array([...])  # Replace with your input data
# result = model(input_data)
# print(result)

# Load the labels
class_names = open("labels.txt", "r").readlines()

# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture(0)
start_time = time.time()
duration = 5 # Duration to display the text
while True:
    # Grab the webcamera's image.
    ret, image = camera.read()

    # Resize the raw image into (224-height,224-width) pixels
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Show the image in a window
    cv2.imshow("Webcam Image", image)

    # Make the image a numpy array and reshape it to the models input shape.
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    image = (image / 127.5) - 1

    # Predicts the model
    prediction = model(image)
    index = np.argmax(prediction)
    class_name = class_names[index]
    
    # If prediction is a dictionary, extract the output array first
    if isinstance(prediction, dict):
        output = list(prediction.values())[0]
        confidence_score = output[index]
    else:
        confidence_score = prediction[index]

    # Print the class name and confidence score
    print("The sign shown is:", class_name[2:], end="")
    break
    
    
    

camera.release()
cv2.destroyAllWindows()