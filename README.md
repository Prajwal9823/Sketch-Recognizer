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

🔗 **Download the following `.npy` class files**:
- `airplane.npy`
- `apple.npy`
- `car.npy`
- `cat.npy`
- `dog.npy`
- `star.npy`
- `umbrella.npy`
- `fish.npy`
- `sword.npy`
- `tree.npy`

📁 **Place all downloaded `.npy` files into this folder**:
data/

yaml
Copy
Edit

---

## ⚙️ Steps to Run the Project Locally

### ✅ 1. Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
Mac/Linux:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
✅ 2. Install Required Packages
bash
Copy
Edit
pip install -r requirements.txt
✅ 3. Train the Model
bash
Copy
Edit
python train_model.py
✅ 4. Run the App
bash
Copy
Edit
streamlit run app.py
Once the server starts, it will open the app in your browser with a sketch canvas and prediction output.

📁 Folder Structure
kotlin
Copy
Edit
sketch-recognizer/
├── app.py
├── train_model.py
├── model/
│   └── sketch_model.h5
├── data/
│   └── *.npy
├── requirements.txt
└── README.md
✅ Requirements
Listed in requirements.txt. Main libraries:

streamlit

tensorflow

numpy

matplotlib

Pillow

scikit-learn

🔗 Credits
Dataset: QuickDraw by Google

Frameworks: TensorFlow, Streamlit

📬 Contact
Made with ❤️ by [Your Name]
🔗 GitHub | LinkedIn

yaml
Copy
Edit

---

✅ You're all set. Just paste that into your `README.md` file.  
Let me know if you need `train_model.py`, `requirements.txt`, or deployment help next.
