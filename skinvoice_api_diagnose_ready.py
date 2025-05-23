
from flask import Flask, request, jsonify
from PIL import Image
import io
import base64
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load trained .h5 model
model = load_model("skin_diagnosis_model.h5")

# Labels used in the trained model
label_map = ['akiec', 'bcc', 'bkl', 'df', 'nv', 'mel', 'vasc']

def decode_image(base64_str):
    image_data = base64.b64decode(base64_str)
    image = Image.open(io.BytesIO(image_data)).resize((128, 128)).convert("RGB")
    return np.array(image) / 255.0

@app.route("/diagnose", methods=["POST"])
def diagnose():
    data = request.get_json()
    image = decode_image(data["image"])
    img_array = np.expand_dims(image, axis=0)

    prediction = model.predict(img_array)[0]
    top_idx = np.argmax(prediction)
    confidence = float(prediction[top_idx])
    condition = label_map[top_idx]

    # Simple severity scale
    severity = "Mild"
    if confidence > 0.85:
        severity = "Moderate"
    if confidence > 0.95:
        severity = "Severe"

    return jsonify({
        "condition": condition,
        "confidence": round(confidence, 2),
        "severity": severity
    })

@app.route("/top-predictions", methods=["POST"])
def top_predictions():
    data = request.get_json()
    image = decode_image(data["image"])
    img_array = np.expand_dims(image, axis=0)

    prediction = model.predict(img_array)[0]
    sorted_indices = prediction.argsort()[::-1][:3]

    top_preds = []
    for idx in sorted_indices:
        top_preds.append({
            "condition": label_map[idx],
            "confidence": round(float(prediction[idx]), 2)
        })

    return jsonify({"predictions": top_preds})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
