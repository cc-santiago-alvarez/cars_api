import logging
from datetime import datetime, timezone
from flask import Flask, request
from flask_cors import CORS
from db import get_db_connection
from controllers.cars import get_cars, create_car, get_car_details
from controllers.brands import get_brands, create_brand
from utils import registerError

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
logging.basicConfig(level=logging.INFO)
db = get_db_connection()
registerError(app)

@app.before_request
def log_requests():
    if request.path == "/api/v1/get_cars":
        log_time = datetime.now(timezone.utc).isoformat()
        logging.info(
            f"sisas mi log {log_time} - {request.remote_addr} - {request.method} {request.path}"
        )

@app.route('/')
def home():
    return "Hellow, world!"

@app.route('/api/v1/get_cars', methods=['GET'])
def handle_get_cars():
    return get_cars()

@app.route('/api/v1/get_cars/car_details', methods=['GET'])
def handle_get_car_details():
    return get_car_details()

@app.route('/api/v1/get_brands', methods=['GET'])
def handle_get_brands():
    return get_brands()

@app.route('/api/v1/create_car', methods=['POST'])
def handle_create_car():
    return create_car()

@app.route('/api/v1/create_brand', methods=['POST'])
def handle_create_brand():
    return create_brand()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8020)