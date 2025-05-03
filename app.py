from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model and vectorizer
model = pickle.load(open('model/fake_job_model.pkl', 'rb'))
vectorizer = pickle.load(open('model/vectorizer.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get job description from the form
    job_desc = request.form['job_description']

    # Vectorize the input
    vector_input = vectorizer.transform([job_desc])

    # Predict and get confidence score
    prediction_value = model.predict(vector_input)[0]
    confidence = np.max(model.predict_proba(vector_input)) * 100

    # Convert prediction to label
    prediction = "Fake" if prediction_value == 1 else "Real"

    # Return result page
    return render_template('result.html', prediction=prediction, confidence=round(confidence, 2))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
