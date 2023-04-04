import cv2

# Define the color range for the car
lower_color = (0, 0, 100)
upper_color = (50, 50, 255)

# Load the video stream from the camera
cap = cv2.VideoCapture(0)

# Initialize the video writer to save the output
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# Loop over the frames in the video stream
while True:
    # Read a frame from the video stream
    ret, frame = cap.read()
    
    # Convert the frame to the HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Create a mask based on the color range
    mask = cv2.inRange(hsv, lower_color, upper_color)
    
    # Find contours in the mask
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Loop over the contours and find the one with the largest area
    max_contour = None
    max_area = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            max_contour = contour
    
    # If a contour was found, draw a bounding box around it and track the car
    if max_contour is not None:
        x, y, w, h = cv2.boundingRect(max_contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # Track the car using its position and other information
        
    # Write the frame to the output video
    out.write(frame)
    
    # Show the frame
    cv2.imshow('frame', frame)
    
    # Exit if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the resources
cap.release()
out.release()
cv2.destroyAllWindows()

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the data
data = pd.read_csv('race_data.csv')

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data.drop('lap_time', axis=1), data['lap_time'], test_size=0.2)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict the lap time for the next lap
next_lap = model.predict(X_test.iloc[-1].values.reshape(1,-1))

print(f"Predicted lap time: {next_lap}")
