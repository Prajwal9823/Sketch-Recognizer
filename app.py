import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
from streamlit_drawable_canvas import st_canvas


# Load model
model = load_model("model/sketch_model.h5")
classes = ['cat', 'dog', 'fish', 'sword', 'apple', 'car', 'tree', 'airplane', 'star', 'umbrella']

st.set_page_config(page_title="Sketch Recognizer", layout="centered")
st.title("🎨 Sketch Recognizer")
st.markdown("Draw or upload a sketch (28x28 grayscale) and let AI guess it!")

# Sidebar option
input_mode = st.radio("Choose Input Method:", ['🖌️ Draw Sketch', '📤 Upload Image'])

img_array = None

if input_mode == '🖌️ Draw Sketch':
    canvas_result = st_canvas(
        fill_color="#000000",  # Black strokes
        stroke_width=10,
        stroke_color="#FFFFFF",  # White background
        background_color="#000000",
        height=280,
        width=280,
        drawing_mode="freedraw",
        key="canvas",
    )

    if canvas_result.image_data is not None:
        image = Image.fromarray((canvas_result.image_data[:, :, 0]).astype(np.uint8))  # Grayscale
        image = image.resize((28, 28))
        img_array = np.invert(np.array(image)) / 255.0
        img_array = img_array.reshape(1, 28, 28, 1)

elif input_mode == '📤 Upload Image':
    uploaded_file = st.file_uploader("Upload a 28x28 sketch", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('L')  # Convert to grayscale
        image = ImageOps.invert(image)  # Invert: background black
        image = image.resize((28, 28))
        img_array = np.array(image) / 255.0
        img_array = img_array.reshape(1, 28, 28, 1)
        st.image(image.resize((140,140)), caption="Uploaded Sketch", width=140)

# Prediction
if img_array is not None:
    pred = model.predict(img_array)
    st.success(f"Prediction: **{classes[np.argmax(pred)]}**")
    st.bar_chart(pred[0])
