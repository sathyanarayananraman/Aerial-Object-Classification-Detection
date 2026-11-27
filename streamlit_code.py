import os
import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# 1. Page Configuration & UI Title
st.set_page_config(
    page_title="Aerial Object Classification",
    page_icon="✈️",
    layout="centered",
)

st.title("✈️ Aerial Object Classification")
st.write("Please upload an image containing either a Bird or a Drone only")
st.write(""" ⚠️ Model Limitations :
This application is designed to classify either a Bird or a Drone. Images containing both a Bird and a Drone or Other objects such as airplanes, helicopters, animals,
  vehicles, and people are not supported. """)



# 2. Load the trained Keras model

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "best_model.keras"
)

@st.cache_resource
def load_keras_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Model not found at: {MODEL_PATH}"
        )

    return tf.keras.models.load_model(MODEL_PATH)

try:
    model = load_keras_model()
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()


# 3. File Uploader
uploaded_file = st.file_uploader(
    "Choose an image...", type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
  # Display uploaded image
  image = Image.open(uploaded_file).convert("RGB")
  st.image(image, caption="Uploaded Image", use_container_width=True)

  # 4. Preprocess Image (Resizing to 224x224 and MobileNetV2 scaling)
  img_resized = image.resize((224, 224))
  img_array = np.array(img_resized)
  img_array = np.expand_dims(img_array, axis=0)
  img_preprocessed = preprocess_input(img_array)

  # 5. Prediction Logic
  with st.spinner("Analyzing image..."):
    prediction = model.predict(img_preprocessed)[0][0]

  # Binary Sigmoid Logic (Threshold: 0.5)
  # {'bird': 0, 'drone': 1}
  if prediction >= 0.5:
    label = "Drone"
    emoji = "🚁"
    confidence = float(prediction)
  else:
    label = "Bird"
    emoji = "🐦"
    confidence = float(1.0 - prediction)

  # 6. Display Results
  st.markdown(f"### Prediction: {emoji} **{label}**")
  st.markdown(f"### Confidence: **{confidence:.2f}**")
