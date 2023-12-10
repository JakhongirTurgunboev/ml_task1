# ML Task

3 Tasks covering neural network, databases and api integration

## Table of Contents

- [Overview](#overview)
  - [Neural network](#neural network)
  - [Working with Database](#working with database)
  - [Google API integration](#google api integration)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [License](#license)

## Overview

  There are three folders in the repository. Namely:<br>
  1.Neural Network<br>
  2.Working with database<br>
  3.Google API Integration
  
### Neural Network
Loading and Preprocessing Data:

The MNIST dataset consists of 28x28 grayscale images of handwritten digits (0 through 9). The mnist.load_data() function is used to load the dataset, and pixel values are normalized to the range [0, 1] by dividing by 255.
Neural Network Architecture:

The neural network consists of three layers:
Flatten layer: Converts the 28x28 input images into a 1D array.
Dense layer (hidden layer): 128 neurons with ReLU activation function.
Dropout layer: Helps prevent overfitting by randomly setting a fraction of input units to 0 during training.
Dense layer (output layer): 10 neurons with softmax activation for classification into 10 classes (digits 0-9).
Compilation:

The model is compiled with the Adam optimizer, sparse categorical crossentropy loss function (suitable for integer labels), and accuracy as the evaluation metric.
Training:

The model is trained on the training data for 5 epochs. The validation_data parameter is used to evaluate the model on the test set after each epoch.
Evaluation:

Finally, the model is evaluated on the test set, and accuracy and loss metrics are printed.
Parameter Choices:

Activation Function: ReLU is used for hidden layers, and softmax for the output layer. ReLU is a standard choice for hidden layers, and softmax is suitable for multi-class classification problems.
Optimizer: Adam is a popular optimizer known for its efficiency and good performance.
Loss Function: Sparse categorical crossentropy is chosen for integer-encoded labels.
Dropout: A dropout rate of 0.2 is used to prevent overfitting.
Feel free to adjust these parameters based on your specific requirements and experiment with different architectures for further optimization.

### Working with a database
Database of choice: SQLite database<br>
There are 4 files in the '2. Working with database' folder.
'rawSQL.db' and 'ormDatabase.db' for sqlite database.
'rawSQLDatabase.py' and 'ormDatabase.py' for working with respective database files.
Two different ways of working with databases are shown. 
One is pure SQL way, another one using ORM for database, sqlalchemy is used in this case.
It helps to keep the code in pythonic way

SQLite is chosen because it is lightweight, since the project is designed to work with
CRUD databases only, it is proper choice. But when scaling the project,migrating the database to PostgreSQL or another database which can support
high-load and concurrency is recommended.

### Google API Integration

## Getting Started

Explain how to set up and run your project. Include instructions for installing dependencies and running the application.

### Prerequisites

List any software or tools that users need to have installed before they can use your project.

### Installation

Provide step-by-step instructions for installing your project.

```bash
# Example installation commands
git clone https://github.com/your-username/your-project.git
cd your-project
npm install
```

## Usage

## Features

## License
MIT License
