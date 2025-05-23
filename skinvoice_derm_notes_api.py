
from flask import Flask, request, jsonify

app = Flask(__name__)

note_templates = {
    "acne": "Moderate comedonal acne observed on the forehead and cheeks. Recommend gentle exfoliation and anti-inflammatory skincare products.",
    "eczema": "Mild to moderate eczema with dry, scaly patches noted. Recommend moisturizers with ceramides and avoidance of known irritants.",
    "rosacea": "Persistent facial redness concentrated in the T-zone. Symmetrical presentation suggests rosacea. Recommend topical anti-inflammatories.",
    "dry skin": "Diffuse dryness with flaking observed. No signs of infection. Recommend increased hydration and barrier-restoring products.",
    "melanoma": "Irregularly shaped lesion with variable pigmentation. Urgent referral to a dermatologist is recommended for biopsy."
}

@app.route("/derm-notes", methods=["POST"])
def derm_notes():
    data = request.get_json()
    condition = data.get("condition", "").lower()

    notes = note_templates.get(condition, "Visual pattern shows signs of irritation. Recommend monitoring and using gentle skincare products.")

    return jsonify({
        "condition": condition,
        "notes": notes
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3005)
