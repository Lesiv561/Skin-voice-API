
from flask import Flask, request, jsonify

app = Flask(__name__)

product_map = {
    "acne": [
        {
            "brand": "CeraVe",
            "name": "Acne Foaming Cream Cleanser",
            "link": "https://www.amazon.com/dp/B07RSZSYNC",
            "price": "$12.99"
        },
        {
            "brand": "The Ordinary",
            "name": "Niacinamide 10% + Zinc",
            "link": "https://theordinary.com/en-us/niacinamide-10-zinc-1-100896.html",
            "price": "$7.90"
        }
    ],
    "dry skin": [
        {
            "brand": "Aveeno",
            "name": "Daily Moisturizing Lotion",
            "link": "https://www.amazon.com/dp/B001459IEE",
            "price": "$8.99"
        },
        {
            "brand": "CeraVe",
            "name": "Moisturizing Cream",
            "link": "https://www.amazon.com/dp/B001V9SXXU",
            "price": "$16.89"
        }
    ],
    "eczema": [
        {
            "brand": "Eucerin",
            "name": "Eczema Relief Cream",
            "link": "https://www.amazon.com/dp/B00DEXA0UY",
            "price": "$9.48"
        },
        {
            "brand": "Vanicream",
            "name": "Moisturizing Skin Cream",
            "link": "https://www.amazon.com/dp/B000GCL2B8",
            "price": "$13.99"
        }
    ]
}

@app.route("/product-matcher", methods=["POST"])
def product_matcher():
    data = request.get_json()
    condition = data.get("condition", "").lower()

    matched = product_map.get(condition, [])
    return jsonify({"products": matched})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3002)
