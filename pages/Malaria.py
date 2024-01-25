#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import os
from PIL import Image
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
import pickle
import streamlit as st

# Streamlit app
st.title("Malaria Detection App")

# Image upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")

    # Model loading (you may need to adjust the path)
    loaded_model = keras.models.load_model('Models/malaria_model.h5')

    # Model prediction button
    if st.button("Predict"):
        # Ensure the shape matches the expected input shape of your model
        input_image_resized = cv2.resize(np.array(image), (128, 128))

        # Normalize the pixel values
        input_image_normalized = input_image_resized / 255

        if len(input_image_normalized.shape) == 2:
            input_image_normalized = np.stack((input_image_normalized,) * 3, axis=-1)

        # Reshape for model prediction
        input_image_reshaped = np.reshape(input_image_normalized, [1, 128, 128, 3])

        # Make predictions
        input_prediction = loaded_model.predict(input_image_reshaped)

        # Get the predicted label
        input_pred_label = np.argmax(input_prediction)

        # Display the predicted label
        if input_pred_label == 1:
            st.error('Malaria detected!')
        else:
            st.success('No The person is fine.')
