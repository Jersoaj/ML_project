from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the trained model
with open("rf_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html", prediction=None)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get user inputs
        ram = float(request.form["ram"])
        screen = float(request.form["screen"])
        battery = float(request.form["battery"])

        # Create input array
        input_data = np.array([[ram, screen, battery]])
        
        # Predict
        prediction = model.predict(input_data)[0]

        return render_template("index.html", prediction=f"Predicted Price: ${prediction:.2f}")

    except Exception as e:
        return render_template("index.html", prediction=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)