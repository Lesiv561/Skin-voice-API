
from flask import Flask, jsonify

app = Flask(__name__)

# Simulated API usage statistics
api_stats = {
    "total_requests": 2413,
    "top_conditions": {
        "acne": 915,
        "dry skin": 603,
        "eczema": 487,
        "rosacea": 218,
        "melanoma": 190
    },
    "average_response_time_ms": 210,
    "active_users": 187
}

@app.route("/developer-dashboard", methods=["GET"])
def developer_dashboard():
    return jsonify(api_stats)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3006)
