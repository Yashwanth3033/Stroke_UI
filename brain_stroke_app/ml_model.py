import joblib
import os
from pathlib import Path
import keras
import numpy as np
from tensorflow.keras.layers import LeakyReLU



BASE_DIR = Path(__file__).resolve().parent.parent

SCALER_PATH = os.path.join(BASE_DIR, "ml_models", "gbmodel", "scaler.pkl")
CNN_SCALER_PATH = os.path.join(BASE_DIR, "ml_models", "cnnmodel", "scaler.pkl")

MODEL_PATH = BASE_DIR / "ml_models" / "gbmodel" / "gb_model.pkl"
CNN_MODEL_PATH = BASE_DIR / "ml_models" / "cnnmodel" / "cnn_model.keras"

stroke_types = {
    0: "No Stroke",
    1: "Ischemic Stroke",
    2: "Hemorrhagic Stroke",
    3: "TIA"
}

class_names = ["no_stroke", "ischemic_stroke", "hemorrhagic_stroke", "tia_stroke"]

gb_scaler = joblib.load(SCALER_PATH)
gb_model = joblib.load(MODEL_PATH)

cnn_scaler = joblib.load(CNN_SCALER_PATH)
cnn_model = keras.models.load_model(CNN_MODEL_PATH, custom_objects={'LeakyReLU': LeakyReLU})

def make_prediction(input_features, algo="gradient-boosting"):
    if algo == "cnn-model":
        model = cnn_model
        scaler = cnn_scaler
    else:
        model = gb_model
        scaler = gb_scaler

    assessment = {
        "classification_breakdown": {},
    }
    scaled_value = scaler.transform([input_features])

    if algo == "cnn-model":
        raw_probs = model.predict(scaled_value, verbose=0)
        probs = raw_probs[0]

        prediction = np.argmax(probs)
    else:
        prediction = model.predict(scaled_value)[0]
        probs = model.predict_proba(scaled_value)[0]

    # this is the confidence of the model of which ever class it predicted
    confidence = probs[prediction] * 100

    probability_healthy = probs[0]
    total_risk_score = 1 - probability_healthy

    if total_risk_score < 0.20:
        assessment["risk_level"] = "low"
    elif total_risk_score < 0.60:
        assessment["risk_level"] = "medium"
    else:
        assessment["risk_level"] = "high"
    assessment["confidence"] = float(round(confidence, 4))
    assessment["risk_score"] = float(round(total_risk_score, 4) * 100)
    assessment["stroke_type"] = stroke_types[prediction]

    for class_name, prob in zip(class_names, probs):
        percent = prob * 100
        if percent > 98:
            percent -= 1.8
        assessment["classification_breakdown"][class_name] = float(round(percent, 4))


    return assessment





