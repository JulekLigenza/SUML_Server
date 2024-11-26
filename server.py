from flask import Flask, request, jsonify
import pandas as pd
from pycaret.regression import load_model

# Load the model
try:
    model = load_model("model")  # Load the pipeline and model
    print("Transformation Pipeline and Model Successfully Loaded")
except Exception as e:
    print(f"Error loading model: {e}")
    raise e

# Initialize Flask app
app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()
        print(f"Received data: {data}")  # Log the received data

        # Convert the input data into a DataFrame
        df = pd.DataFrame([data])

        # Ensure preprocessor exists in the pipeline
        if hasattr(model, "preprocessor"):
            print("Applying preprocessor...")
            df = model.preprocessor.transform(df)

        # Perform prediction
        predictions = model.predict(df)
        return jsonify({"predictions": predictions.tolist()})
    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
