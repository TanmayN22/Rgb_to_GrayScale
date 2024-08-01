import numpy as np
import streamlit as st
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

st.title("Change image colour from RGB to GrayScale")

def rgb2gray(rgb):
    """Converts an RGB image to grayscale."""
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def display_grayscale_image(image):
    """Displays a grayscale image using the specified libraries."""
    gray = rgb2gray(image)
    plt.imshow(gray, cmap=plt.get_cmap('gray'))
    return plt

def process_image(uploaded_file):
    if uploaded_file is not None:
        image = mpimg.imread(uploaded_file)
        col1, col2 = st.columns(2)

        # Display original image on the left
        with col1:
            st.image(image)

        # Convert and display grayscale image on the right
        with col2:
            grayscale_plot = display_grayscale_image(image)
            st.pyplot(grayscale_plot)

# File uploader widget
uploaded_file = st.file_uploader("Upload an image")
process_image(uploaded_file)