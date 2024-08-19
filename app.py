from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained model and scaler
with open('predictive_maintenance_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

# Define the features used for prediction
features = ['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract data from the request
        data = {
            'Air temperature [K]': float(request.form['air_temperature']),
            'Process temperature [K]': float(request.form['process_temperature']),
            'Rotational speed [rpm]': float(request.form['rotational_speed']),
            'Torque [Nm]': float(request.form['torque']),
            'Tool wear [min]': float(request.form['tool_wear'])
        }

        # Convert data to DataFrame
        df = pd.DataFrame([data])
        
        # Scale features
        X_scaled = scaler.transform(df[features])
        
        # Predict
        prediction = model.predict(X_scaled)
        
        # Convert prediction back to original label
        result = {0: 'No Failure', 1: 'Power Failure', 2: 'Tool Wear Failure'}[prediction[0]]
        
        return jsonify({'prediction': result})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)



