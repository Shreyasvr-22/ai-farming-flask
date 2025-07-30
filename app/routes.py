from flask import Blueprint, request, jsonify

main = Blueprint('main', __name__)

@main.route("/")
def home():
    return jsonify({"message": "AI Farming API is running!"})

@main.route("/predict-weather", methods=["POST"])
def predict_weather():
    data = request.get_json()
    location = data.get("location", "DefaultRegion")

    dummy_output = {
        "location": location,
        "forecast": [
            {"day": "Day 1", "rainfall_mm": 10, "temperature_C": 28},
            {"day": "Day 2", "rainfall_mm": 0, "temperature_C": 31},
        ]
    }
    return jsonify(dummy_output)
