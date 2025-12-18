from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# 1. Load the trained model and the feature list
# We load them once when the app starts so we don't read files for every request
model = joblib.load('../models/churn_model.pkl')
model_columns = joblib.load('../models/features.pkl')

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'App is running!'})

@app.route('/predict', methods=['POST'])
def predict():
    # 2. Get JSON data from the request
    json_ = request.json
    
    # 3. Convert JSON to Pandas DataFrame
    query_df = pd.DataFrame([json_])
    
    # 4. PREPROCESSING (Exactly what we did in the notebook!)
    # Convert "Yes/No" to 1/0
    query_df.replace('No internet service', 'No', inplace=True)
    query_df.replace('No phone service', 'No', inplace=True)
    
    # Simple loop to handle binary columns
    for col in query_df.columns:
        if query_df[col].dtype == 'object':
             query_df[col].replace({'Yes': 1, 'No': 0}, inplace=True)
    
    # 5. One-Hot Encoding & Alignment
    # This turns "InternetService: Fiber" into "InternetService_Fiber: 1"
    query_df = pd.get_dummies(query_df)
    
    # CRITICAL STEP: Align columns with the training data
    # If the user input is missing columns the model expects (or has extras),
    # this fixes it by filling missing ones with 0.
    query_df = query_df.reindex(columns=model_columns, fill_value=0)
    
    # 6. Make prediction
    prediction = model.predict(query_df)
    
    # 7. Return result
    result = "Yes" if prediction[0] == 1 else "No"
    return jsonify({'churn_prediction': result})

if __name__ == '__main__':
    app.run(port=5000, debug=True)