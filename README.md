# Cars API

REST API for managing cars and brands, built with Flask and MongoDB.

## 🚀 Project Structure

```
cars_api/
├── app.py
├── db.py
├── requirements.txt
├── utils.py
├── controllers/
│   ├── brands.py
│   └── cars.py
└── models/
    ├── brands.py
    └── cars.py
```

## 📋 Prerequisites

- Python 3.8+
- pip
- MongoDB access (local or remote)
- Postman or similar API testing tool

## ⚙️ Installation

1. Clone repository
2. Create virtual environment:
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   . .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🖥️ Run the Server

```bash
python app.py
```
Server will start at `http://0.0.0.0:8020`

## 📡 API Endpoints

### Cars
- `GET /api/v1/get_cars` - List cars (pagination supported)
- `GET /api/v1/get_cars/car_details` - Advanced search
- `POST /api/v1/create_car` - Create new car

### Brands
- `GET /api/v1/get_brands` - List brands
- `POST /api/v1/create_brand` - Create new brand

## 🔧 Using Postman

### GET Example (List Cars)
```
GET http://localhost:8020/api/v1/get_cars?page=1&limit=5
```

### POST Example (Create Brand):
```json
{
    "name": "Toyota"
}
```

## 🐧 Using cURL

### List Brands:
```bash
curl -X GET "http://localhost:8020/api/v1/get_brands"
```

### Create Car:
```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
    "model": "Corolla",
    "price": 25000,
    "kilometers": 15000,
    "brandId": "BRAND_UUID"
}' \
http://localhost:8020/api/v1/create_car
```

## 🚨 Error Handling

Standardized responses:
```json
{
    "data": null,
    "status": 400,
    "message": "Invalid fields"
}
```

Common status codes:
- 400: Invalid fields
- 404: Resource not found
- 500: Internal error

## 🛠️ Troubleshooting

### MongoDB Connection Issues
1. Verify connection string in `db.py`
2. Check internet access if using MongoDB Atlas
3. Validate credentials

### Missing Dependencies
```bash
pip freeze > requirements.txt  # Regenerate if needed
pip install -r requirements.txt --force-reinstall
```

### Port Conflicts
```bash
# Linux/Mac
sudo lsof -i :8020
kill -9 <PID>

# Windows
netstat -ano | findstr :8020
taskkill /PID <PID> /F
```

## 📄 Additional Notes
- Data stored using UUID format
- CORS enabled for all domains
- Access logs in console for `/api/v1/get_cars`
```