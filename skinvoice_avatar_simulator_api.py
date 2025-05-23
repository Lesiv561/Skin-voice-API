
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/avatar-simulator", methods=["POST"])
def avatar_simulator():
    data = request.get_json()
    user_id = data.get("user_id", "guest")

    # Simulated response for now
    simulated_image_url = f"https://yourdomain.com/images/{user_id}_clear_simulated.jpg"

    return jsonify({
        "user_id": user_id,
        "before_image": f"https://yourdomain.com/images/{user_id}_original.jpg",
        "simulated_clear_skin": simulated_image_url,
        "note": "Simulated preview of expected skin appearance after 7 days of care."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3004)
