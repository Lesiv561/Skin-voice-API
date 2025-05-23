
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory tracking storage (for demo)
user_tracking_data = {}

@app.route("/healing-tracker", methods=["POST"])
def healing_tracker():
    data = request.get_json()
    user_id = data.get("user_id")
    condition = data.get("condition")
    confidence = float(data.get("confidence", 0.0))

    if not user_id or not condition:
        return jsonify({"error": "Missing user_id or condition"}), 400

    history = user_tracking_data.get(user_id, [])

    trend = "First Scan"
    if history:
        last_entry = history[-1]
        if confidence > last_entry["confidence"]:
            trend = "Improved"
        elif confidence < last_entry["confidence"]:
            trend = "Worsening"
        else:
            trend = "No Change"

    # Store current scan
    history.append({
        "condition": condition,
        "confidence": confidence
    })
    user_tracking_data[user_id] = history

    return jsonify({
        "user_id": user_id,
        "current_condition": condition,
        "trend": trend,
        "history": history[-5:]  # Return last 5 entries
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3003)
