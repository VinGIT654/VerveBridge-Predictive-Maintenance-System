# VerveBridge-Predictive-Maintenance-System
"Predictive Maintenance System using Flask, trained on key operational features to predict equipment failures. Includes model training, feature scaling, and a web interface for user input and prediction display."

# Predictive Maintenance System

## Overview
The Predictive Maintenance System is designed to predict potential equipment failures using machine learning. It uses a trained RandomForest model to predict failures based on input features like air temperature, process temperature, rotational speed, torque, and tool wear.

## Project Structure
- **machine_failure_prediction.py.ipynb**: Jupyter notebook for training and testing the machine learning model.
- **predictive_maintenance_model.pkl**: Serialized model file used for predictions.
- **predictive_maintenance.csv**: Dataset containing the features and target variables for training the model.
- **app.py**: Flask web application that provides a user interface for entering input features and getting predictions.
- **templates/index.html**: HTML template for the web application's front end.


Key Files:
machine_failure_prediction.py.ipynb: Contains the code for data preprocessing, model training, and evaluation. This notebook demonstrates the process of building and validating the machine learning model used in the application.

predictive_maintenance_model.pkl: A serialized version of the trained RandomForest model. This file is loaded in the Flask application to make predictions based on user input.

predictive_maintenance.csv: The dataset used to train the machine learning model. It includes features such as air temperature, process temperature, rotational speed, torque, tool wear, and the failure type.

app.py: The main script for the Flask application. It handles routing, form submissions, and prediction logic. The application takes user input, preprocesses it, and uses the loaded model to make predictions.

templates/index.html: The HTML template for the front-end user interface. It allows users to input the required features and submit them for prediction.

Installation and Setup
Prerequisites
Python 3.x
Pip (Python package installer)


Step-by-Step Guide

Clone the Repository

git clone https://github.com/VerveBridge/Predictive-Maintenance-System.git
cd Predictive-Maintenance-System


Create a Virtual Environment (Optional but recommended)
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`


Install Required Dependencies
pip install -r requirements.txt

Run the Flask Application
python app.py


Access the Application
Open your web browser and navigate to http://127.0.0.1:5000/


Usage
Input Features:
Air temperature [K]: The temperature of the air in Kelvin.
Process temperature [K]: The temperature of the process in Kelvin.
Rotational speed [rpm]: The rotational speed of the equipment in revolutions per minute.
Torque [Nm]: The torque applied to the equipment in Newton-meters.
Tool wear [min]: The wear on the tool in minutes.
Making a Prediction
Input the required features in the form provided on the web page.
Click the "Predict" button.
The application will return a prediction indicating whether there is a potential failure (No Failure, Power Failure, or Tool Wear Failure).
Sample Input:
Air temperature [K]: 298.9
Process temperature [K]: 309.1
Rotational speed [rpm]: 1383
Torque [Nm]: 54.9
Tool wear [min]: 145
Model Training
The model was trained using the predictive_maintenance.csv dataset. The RandomForestClassifier was chosen due to its robustness and ability to handle complex datasets. The training process involved:

Data Preprocessing: Cleaning and transforming the data, including handling missing values and encoding categorical variables.
Feature Engineering: Creating additional features to improve model performance.
Model Evaluation: Assessing model accuracy and fine-tuning parameters to achieve optimal performance.
The final model was saved as predictive_maintenance_model.pkl and is loaded in the Flask application for predictions.

Technologies Used
Python: Core programming language.
Flask: Web framework used to build the application.
Scikit-learn: Machine learning library used to train the RandomForest model.
Pandas: Data manipulation and analysis library.
HTML/CSS: Front-end design for the web application.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request for review


Contact
For any inquiries, please contact [ vinuthanaik550@gmail.com ].



License
This project is licensed under the MIT License


This README file provides comprehensive information about the project, including a clear overview, detailed instructions on setting up and running the application, and technical insights into the machine learning model used. It also includes sections on contributing, licensing, and contacting the project maintainers. Feel free to adjust the content to match your specific project requirements and contact details.

