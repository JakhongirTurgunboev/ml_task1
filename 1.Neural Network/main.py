import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist

# Load and preprocess the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0  # Normalize pixel values to between 0 and 1

# Build the neural network model
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),       # Flatten the input image (28x28) to a 1D array
    layers.Dense(128, activation='relu'),       # Dense hidden layer with 128 neurons and ReLU activation
    layers.Dropout(0.2),                        # Dropout layer for regularization
    layers.Dense(10, activation='softmax')      # Output layer with 10 neurons (for 10 classes) and softmax activation
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',  # Use sparse categorical crossentropy for integer labels
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test,  y_test, verbose=2)
print(f'\nTest accuracy: {test_acc}, Test loss: {test_loss}')

# Save the results
model.save('trained_model.keras')