# ML Task

3 Tasks covering neural network, databases and api integration

## Table of Contents

- [Overview](#overview)
  - [Neural network](#neural network)
  - [Working with a database](#working with database)
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
  
### Neural network
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
This task's folder is '3.Google API Integration'.
This project is demonstration of working with Google API.
In this case, Google service of choice is Google Maps api.
It requires API Key, that's why API key must be provided before using the project.
IT prompts the user to enter the name of the place and provides the list of available
places that in Google Maps that match the prompt.
## Getting Started

### Prerequisites

There are no initial requirements. But note that, this project is built in Windows environment, so that
issues related to OS must be handled by the user.

### Installation

Copy the commands below to your local environment:

```bash
# Example installation commands
git clone https://github.com/JakhongirTurgunboev/ml_task.git
cd ml_task
# Create virtual environment
python -m venv venv
# Activate the virtual environment
.\venv\Scripts\activate # For windows
# Install the dependencies
pip install -r requirements.txt
```

Note that installation may take sometimes, because it installs all the dependencies of the project.
After installation, change directory to desired app directory. Like, '1.Neural Network', 
'2.Working with database' and '3.Google API Integration'.
Run the applications, in case of an issue, refer to "Usage" in documentation

## Usage
### 1. Neural Network.<br>
Inside this folder there are two scripts 'main.py' and 'cvScript.py'
'main.py'.
You can run the 'main.py' with command:
```bash
  cd '.\1.Neural Network\'
  python main.py
```
The script loads MNIST dataset from tensorflow datasets, then normalizes pixel values.
After that, it builds neural network model, compiles and trains the model. Then evaluates the model and prints the test accuracy.
Finally, it saves the model as a file named 'trained_model.keras'

This would be enough demonstration of neural networks with tensorflow dataset. But I decided to show real life example.
So after generating 'trained_model.keras' in the directory. Run the following command:
```bash
  python cvScript.py
```
cvScript will predict the number shown in the camera of the laptop, based on the trained dataset.
It is not that accurate, because provided dataset is relatively small. cvScript uses Python's cv2 library for 
object detection. cv2 library is computer vision library.
<br>

### 2. Working with a database <br>
There are two ways to work with database. One way is to query the database using raw SQL queries, 
another way is to query the database using ORM queries. 'rawSQLDatabase.py' is connected to the database
'rawSQL.db'. It supports CRUD queries with Users table. The script for ORM version is 
'ormDatabase.py' which is connected to the 'ormDatabase.db' database. This database supports CRUD queries 
to Cars table. To use the application, write the following command:
```bash
  cd '.\2.Working with database\'
  python rawSQLDatabase.py # or
  python ormDatabase.py
```

### 3. Google API Integration
To use this application:
```bash
  cd '.\3.Google API Integration\'
```
Create new file called '.env', add your Google API key to it like this:
```env
  GOOGLE_MAPS_API_KEY=your_api_key
```
Replace your api key with actual Google API key. To get your API key, visit https://console.cloud.google.com
Choose 'API & Services' -> 'Enable API and Services' -> 'Places API' follow the instructions, get your API key, then 
insert it into the '.env'. Then run the following command:
```bash
  python main.py
```
## Features
There are a number of features of each task.
1. Neural Network. It supports predicting the number based on camera input with handwritten numbers.
Apart from initially required simple neural network feature, it also includes computer vision.
2. It was required to work with a database using Python, with simple CRUD functionality, both ways of connecting 
to the database are shown. The first option is raw SQL queries, the second option is ORM (Object Relational Mapper).
3. For Google API Integration, Google Maps is chosen. It supports finding the place from Google Map's api. 


## License
MIT License
