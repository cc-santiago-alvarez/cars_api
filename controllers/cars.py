from flask import request, jsonify
import uuid
from utils import generic_response
from models.cars import cars_collection
from models.brands import brands_collection


def pagination():
    page = request.args.get('page')
    limit = request.args.get('limit')
        
    if page is not None or limit is not None:
        page = int(page) if page is not None else 1
        limit = int(limit) if limit is not None else 10
        skip = (page - 1) * limit
        return skip, limit
    return None

def get_cars():
    try:        
        query = {}
        
        brand_name_filter = request.args.get('brand')
        if brand_name_filter:
            brand = brands_collection.find_one({"name": {"$regex": brand_name_filter, "$options": "i"}})
            if brand:
                query["brandId"] = brand["_id"]
            else:
                query["brandId"] = None
        
        pag = pagination()
        if pag:
            skip, limit = pag
            cars_cursor = cars_collection.find(query).skip(skip).limit(limit)
        else:
            cars_cursor = cars_collection.find(query)
        
        cars = list(cars_cursor)
        
        for car in cars:
            if "_id" in car:
                car["_id"] = str(car["_id"])
            if "brandId" in car:
                car["brandId"] = str(car["brandId"])

        return generic_response(
            data = cars,
            status = 200,
            message = "OK"
        )
    except Exception as e:
      print("Error:", str(e))
      return generic_response(
            data=None,
            status=500,
            message="Error retrieving cars"
      )
      
def get_car_details():
    try:
        query = {}
        
        model_filter = request.args.get('model')
        if model_filter:
            regex_pattern = model_filter.replace(" ", "[ _]")
            query["model"] = {"$regex": regex_pattern, "$options": "i"}
            
        price_filter = request.args.get('price')
        if price_filter:
            try:
                query["price"] = float(price_filter)
            except ValueError:
                pass
  
        kilometers_filter = request.args.get('kilometers')
        if kilometers_filter:
            try:
                query["kilometers"] = int(kilometers_filter)
            except ValueError:
                pass
            
        brand_name_filter = request.args.get('brand')
        if brand_name_filter:
            brand = brands_collection.find_one({"name": {"$regex": brand_name_filter, "$options": "i"}})
            if brand:
                query["brandId"] = brand["_id"]
            else:
                query["brandId"] = None
                    
        
        pag = pagination()
        if pag:
            skip, limit = pag
            cars_cursor = cars_collection.find(query).skip(skip).limit(limit)
        else:
            cars_cursor = cars_collection.find(query)
        
        cars = list(cars_cursor)
        
        for car in cars:
            if "_id" in car:
                car["_id"] = str(car["_id"])
            if "brandId" in car:
                car["brandId"] = str(car["brandId"])
      
        return generic_response(
            data=cars,
            status=200,
            message="OK"
        )
    except Exception as e:
        print("Error:", str(e))
        return generic_response(
            data=None,
            status=500,
            message="Error retrieving cars"
        )

def create_car():
    try:
        data = request.get_json()
    
        if not data or not all(key in data for key in ["model", "price", "kilometers", "brandId"]):
            return generic_response(
                data=None,
                status=400,
                message="Invalid fields"
            )
    
        brand_id = data.get("brandId")
        brand = brands_collection.find_one({"_id": brand_id})
        if not brand:
            return generic_response(
                data=None,
                status=400,
                message="Brand not found"
            ) 
        
        car = {
            "_id": str(uuid.uuid4()),
            "model": data.get("model"),
            "description": data.get("description"),
            "price": data.get("price"),
            "kilometers": data.get("kilometers"),
            "brandId": brand_id
        }
    
        cars_collection.insert_one(car)
        car.pop("_id", None)
    
        return generic_response(
            data = car,
            status = 200,
            message = "OK"
        )
    except Exception as e:
      print("Error:", str(e))
      return generic_response(
            data=None,
            status=500,
            message="Error retrieving cars"
      )


