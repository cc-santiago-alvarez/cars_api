from pymongo import MongoClient
from db import get_db_connection

db = get_db_connection()

user_schema = {
    "_id": {type: str},
    "first_name": {type: str},
    "last_name": {type: str},
    "email": {type: str},
    "password": {type: str},
}

users_collection = db["users"]