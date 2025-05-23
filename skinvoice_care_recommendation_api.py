
from flask import Flask, request, jsonify

app = Flask(__name__)

care_map = {
    "eczema": {
        "product_type": "Fragrance-free moisturizer",
        "ingredients": ["colloidal oatmeal", "ceramides"],
        "lifestyle_tip": "Avoid hot showers and use a humidifier in dry climates."
    },
    "dry skin": {
        "product_type": "Hydrating cream",
        "ingredients": ["hyaluronic acid", "glycerin"],
        "lifestyle_tip": "Drink more water and apply moisturizer after bathing."
    },
    "acne": {
        "product_type": "Gentle exfoliating cleanser",
        "ingredients": ["salicylic acid", "niacinamide"],
        "lifestyle_tip": "Avoid picking and use non-comedogenic products."
    },
    "rosacea": {
        "product_type": "Soothing gel",
        "ingredients": ["azelaic acid", "green tea extract"],
        "lifestyle_tip": "Avoid spicy foods and manage stress."
    },
    "melanoma": {
        "product_type": "N/A",
        "ingredients": [],
        "lifestyle_tip": "See a licensed dermatologist immediately."
    }
}

@app.route("/care-recommendation", methods=["POST"])
def care_recommendation():
    data = request.get_json()
    condition = data.get("condition", "").lower()

    recommendation = care_map.get(condition, {
        "product_type": "Gentle moisturizer",
        "ingredients": ["ceramides", "aloe vera"],
        "lifestyle_tip": "Protect skin from harsh elements and stay hydrated."
    })

    return jsonify(recommendation)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001)
