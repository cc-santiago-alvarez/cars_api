from pymongo import MongoClient
import uuid
from db import get_db_connection

db = get_db_connection()

car_schema = {
    "_id": {type: str},
    "model": {type: str, "max_length": 30},
    "description": {type: str, "max_length": 100},
    "price": {type: float},
    "kilometers": {type: int},
    "brandId": {type: str}
}

cars_collection = db["cars"]

