from flask import request, jsonify
import uuid
from utils import generic_response
from models.brands import brands_collection

def get_brands():
    try:
      brands = list(brands_collection.find())
      return generic_response(
          data = brands,
          status = 200,
          message = "OK"
      )
    except Exception as e:
      print("Error:", str(e))
      
      
def create_brand():
    data = request.get_json()
    
    if not data or "name" not in data:
        return generic_response(
            data=None,
            status=400,
            message="Invalid fields"
        )
        
    brand = {
        "_id": str(uuid.uuid4()),
        "name": data.get("name"),
    }
    
    brands_collection.insert_one(brand)
    brand.pop("_id", None)
    
    return generic_response(
          data = brand,
          status = 201,
          message = "OK"
    )