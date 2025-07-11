import numpy as np
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split

# Load data
# New list of classes
classes = ['cat', 'dog', 'fish', 'sword', 'apple', 'car', 'tree', 'airplane', 'star', 'umbrella']
X, y = [], []

for idx, name in enumerate(classes):
    data = np.load(f'data/{name}.npy')[:5000]  # Use first 5000 samples
    X.append(data)
    y.append(np.full(len(data), idx))

X = np.concatenate(X)
y = np.concatenate(y)

# Normalize & reshape
X = X / 255.0
X = X.reshape(-1, 28, 28, 1)
y = to_categorical(y)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# CNN Model
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    MaxPooling2D(2,2),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(len(classes), activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=5, validation_data=(X_test, y_test))

model.save('model/sketch_model.h5')
