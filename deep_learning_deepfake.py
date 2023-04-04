import cv2
import os

def extract_frames(video_path, output_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error opening video file")
        return
    
    os.makedirs(output_path, exist_ok=True)
    
    count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        output_file = os.path.join(output_path, f"frame_{count:05d}.jpg")
        cv2.imwrite(output_file, frame)
        count += 1
    
    cap.release()

import tensorflow as tf

def build_cnn(input_shape):
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
    model.add(tf.keras.layers.MaxPooling2D((2, 2)))
    model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(tf.keras.layers.MaxPooling2D((2, 2)))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(64, activation='relu'))
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
    return model

model = build_cnn(input_shape=(224, 224, 3))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(train_data, epochs=10, validation_data=val_data)

loss, accuracy = model.evaluate(test_data)
print(f"Test loss: {loss}")
print(f"Test accuracy: {accuracy}")

