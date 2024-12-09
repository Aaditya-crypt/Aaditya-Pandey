import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import os

app = Flask(__name__)
CORS(app)

# Load the model once during app startup
MODEL_PATH = 'D:/CollegeProjects/sybitcoin/BitcoinpredictionUI/prophet_model.pkl'

def load_model():
    """Load the trained model from the specified path."""
    try:
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
        return model
    except Exception as e:
        print(f"Error loading the model: {e}")
        return None

# Load the model at app startup
model = load_model()
if not model:
    raise Exception("Model loading failed! Cannot proceed without the model.")


@app.route('/predict', methods=['POST'])
def predict():
    """Handle prediction request with JSON data."""
    data = request.get_json()  # Retrieve the data sent from JavaScript

    # Validate the presence of the 'Date' field
    if 'Date' not in data:
        return jsonify({'error': 'Missing "Date" in the request data'}), 400
    
    print(f"Received Date: {data['Date']}")
    date_input = data['Date']
    # Make predictions using the Prophet model
    try:
        # Generate future dataframe and predict
        future = model.make_future_dataframe(periods=365)
        forecast = model.predict(future)
        
        # Extract the last predicted price
        predicted_price = forecast[forecast['ds'] == date_input]['yhat'].item()
        predicted_price = round(predicted_price, 4)
        # Prepare and send the JSON response
        response = {'predictedPrice': predicted_price}
        return jsonify(response), 200

    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({'error': 'An error occurred during prediction', 'details': str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
