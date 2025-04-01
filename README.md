# Cars API

REST API for vehicle and brand management, built with Flask and MongoDB.

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

1. Clone the repository
2. Create a virtual environment:

   **Windows:**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

   **Linux/Mac:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   If activation fails, try:
   ```bash
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

### Vehicles
- `GET /api/v1/get_cars` - List vehicles with basic filters (paginated)
- `GET /api/v1/get_cars/car_details` - Advanced search with multiple filters
- `POST /api/v1/create_car` - Create new vehicle

### Brands
- `GET /api/v1/get_brands` - List brands
- `POST /api/v1/create_brand` - Create new brand

## 🔧 Usage with Postman

### Filters & Pagination (Query Parameters)
| Parameter    | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| `brand`      | Filter by brand name (e.g., Toyota)                                         |
| `model`      | Filter by car model (only in `/car_details`, e.g., Corolla)                 |
| `price`      | Filter by exact price (e.g., 25000)                                         |
| `kilometers` | Filter by exact mileage (e.g., 15000)                                       |
| `page`       | Page number for pagination (e.g., 2)                                        |
| `limit`      | Results per page (e.g., 10)                                                 |

**Multi-filter Example:**
```
GET http://localhost:8020/api/v1/get_cars/car_details?brand=Toyota&model=Corolla&page=1&limit=5
```

### GET Example (Paginated Vehicles):
```
GET http://localhost:8020/api/v1/get_cars?page=1&limit=5&brand=Ford
```

### POST Example (Create Brand):
```json
{
    "name": "Toyota"
}
```

## 🐧 cURL Usage

### List Vehicles with Filters:
```bash
curl -X GET "http://localhost:8020/api/v1/get_cars/car_details?brand=Toyota&model=Corolla&price=25000&page=1&limit=5"
```

### List Brands:
```bash
curl -X GET "http://localhost:8020/api/v1/get_brands"
```

### Create Vehicle:
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

API returns standardized responses:
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
2. Ensure internet access if using MongoDB Atlas
3. Validate credentials

### Filters Not Working
- Use exact parameter names (case-sensitive)
- For partial matches use wildcards: `brand=Toyo*`
- Numeric values without quotes

### Missing Dependencies
```bash
pip freeze > requirements.txt  # Regenerate if needed
pip install -r requirements.txt --force-reinstall
```

## 📄 Additional Notes
- Filters can be combined as needed
- Pagination is optional (omit `page`/`limit` to get all results)
- Brand UUIDs are obtained from the `get_brands` endpoint
- CORS enabled for all domains
