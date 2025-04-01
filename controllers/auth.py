import uuid
from flask import request
from utils import generic_response
from models.users import users_collection
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, jwt_required

bcrypt = Bcrypt()

def register_user():
    data = request.get_json()
    if not data or not all(k in data for k in ["first_name", "last_name", "email", "password"]):
        return generic_response(
            data=None, 
            status=400, 
            message="Invalid fields"
            )
    
    if users_collection.find_one({"email": data["email"]}):
        return generic_response(
            data=None, 
            status=400, 
            message="Email already registered"
            )
    
    # Hashear la contraseña
    hashed_password = bcrypt.generate_password_hash(data["password"]).decode("utf-8")
    
    user = {
        "_id": str(uuid.uuid4()),
        "first_name": data.get("first_name"),
        "last_name": data.get("last_name"),
        "email": data.get("email"),
        "password": hashed_password
    }
    
    users_collection.insert_one(user)
    user.pop("password")
    
    return generic_response(
        data=user, 
        status=201, 
        message="User registered successfully")

def login_user():
    data = request.get_json()
    if not data or not all(k in data for k in ["email", "password"]):
        return generic_response(
            data=None, 
            status=400, 
            message="Invalid fields"
            )
    
    user = users_collection.find_one({"email": data["email"]})
    if not user:
        return generic_response(
            data=None, 
            status=401, 
            message="Invalid credentials"
            )
    
    if not bcrypt.check_password_hash(user["password"], data["password"]):
        return generic_response(
            data=None, 
            status=401, 
            message="Invalid credentials"
            )
    
    # Crear un token de acceso (JWT)
    access_token = create_access_token(identity=user["_id"])
    
    return generic_response(
        data={"access_token": access_token}, 
        status=200, 
        message="Login successful"
        )
