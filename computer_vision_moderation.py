import cv2
import numpy as np

# Define the path to the cascade classifier for detecting faces
face_cascade_path = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(face_cascade_path)

# Define the path to the cascade classifier for detecting objects (e.g. weapons)
object_cascade_path = 'object_cascade.xml'
object_cascade = cv2.CascadeClassifier(object_cascade_path)

# Define the path to the image to be moderated
image_path = 'image.jpg'

# Load the image and convert it to grayscale
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Detect objects (e.g. weapons) in the image
objects = object_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# If any faces or objects are detected, mark the image as inappropriate
if len(faces) > 0 or len(objects) > 0:
    # Mark the image as inappropriate by drawing a red rectangle around it
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
    for (x, y, w, h) in objects:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
        
    # Save the image to a file with a warning message
    cv2.imwrite('moderated_image.jpg', image)
    print("The uploaded image contains inappropriate content and has been moderated.")
else:
    # Save the image to a file without a warning message
    cv2.imwrite('uploaded_image.jpg', image)
    print("The uploaded image has been approved for use.")
