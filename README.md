# 🖌️ Sketch Recognizer

A deep learning-based Sketch Recognizer built using a Convolutional Neural Network (CNN) and trained on Google's QuickDraw dataset. This app lets you draw a sketch on a canvas and predicts the object using a trained model. Includes a dropdown filter to limit prediction scope to specific classes.

---

## 🚀 Features

- Built with TensorFlow/Keras and Streamlit
- Real-time sketch prediction using a drawable canvas
- Dropdown filter to restrict prediction scope
- Lightweight CNN model optimized for fast inference

---

## 📦 Dataset

This project uses a subset of the [QuickDraw Dataset by Google](https://quickdraw.withgoogle.com/data).

🔗 **Download individual class `.npy` files** from:
- [QuickDraw Dataset (official site)](https://quickdraw.withgoogle.com/data)
- download desired  airplane,apple,car,cat,dog,start,umbrella,fish,sword,tree classes

📁 **Place all downloaded `.npy` files in this directory:**
data/
---
## ⚙️ Steps to Run the Project Locally

### ✅ 1. Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate

✅ 2. Install Required Packages
```bash
pip install -r requirements.txt

✅ 3. Train the Model
```bash
python train_model.py

