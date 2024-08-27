from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the LightGBM model
model = joblib.load('model/lightgbm_model.pkl')


def preprocess_input(data):
    df = pd.DataFrame([data])
    # Apply feature engineering
    df["Vehicle_Age"] = df["Vehicle_Age"].astype('category').cat.rename_categories({
        "1-2 Year": 1,
        "< 1 Year": 0,
        "> 2 Years": 2
    }).astype('int8')

    df['Gender'] = (df['Gender'] == 'Male').astype(np.uint8)
    df['Vehicle_Damage'] = (df['Vehicle_Damage'] == 'Yes').astype(np.uint8)

    df['Annual_Premium_Insurance'] = df['Previously_Insured'].astype(str) + df['Annual_Premium'].astype(str)
    df['Annual_Premium_Insurance'] = pd.factorize(df['Annual_Premium_Insurance'])[0] + 1

    df['Vehicle_Age_Insurance'] = df['Previously_Insured'].astype(str) + df['Vehicle_Age'].astype(str)
    df['Vehicle_Age_Insurance'] = pd.factorize(df['Vehicle_Age_Insurance'])[0] + 1

    return df

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = {
            'Gender': request.form['Gender'],
            'Age': int(request.form['Age']),
            'Driving_License': int(request.form['Driving_License']),
            'Region_Code': float(request.form['Region_Code']),
            'Previously_Insured': int(request.form['Previously_Insured']),
            'Vehicle_Age': request.form['Vehicle_Age'],
            'Vehicle_Damage': request.form['Vehicle_Damage'],
            'Annual_Premium': float(request.form['Annual_Premium']),
            'Policy_Sales_Channel': float(request.form['Policy_Sales_Channel']),
            'Vintage': int(request.form['Vintage'])
        }

        df_input = preprocess_input(input_data)

        # Make prediction
        prediction = model.predict(df_input)
        response = "Yes" if prediction[0] == 1 else "No"

        return render_template('result.html', prediction=response)
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
