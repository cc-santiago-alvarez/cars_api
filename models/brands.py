from pymongo import MongoClient
import uuid
from db import get_db_connection

db = get_db_connection()

brand_schema = {
    "_id": {type: str},
    "name": {type: str, "max_length": 20},
}

brands_collection = db["brands"]

