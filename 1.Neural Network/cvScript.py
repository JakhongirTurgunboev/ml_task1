import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load the pre-trained model
model = load_model('trained_model.keras')

# Open a connection to the laptop camera (you can change the argument to 0, 1, etc., based on your camera index)
cap = cv2.VideoCapture(0)

while True:
    # Capture video frame-by-frame
    ret, frame = cap.read()

    # Preprocess the frame for prediction
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resized_frame = cv2.resize(gray_frame, (28, 28))
    normalized_frame = resized_frame / 255.0
    input_data = np.reshape(normalized_frame, (1, 28, 28))

    # Make a prediction using the pre-trained model
    prediction = model.predict(input_data)
    predicted_class = np.argmax(prediction)

    # Display the frame with the predicted class
    cv2.putText(frame, f'Predicted Number: {predicted_class}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Number Recognition', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
