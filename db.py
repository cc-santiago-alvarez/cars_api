from pymongo import MongoClient
from bson import errors

def get_db_connection():
    try:
        client = MongoClient(
            "mongodb+srv://salvarsa:sisas1234@carsapi.hq7i7mu.mongodb.net/",
            tls=True,
            tlsAllowInvalidCertificates=True,
            uuidRepresentation="standard"
        )
        print(" 🤖 db connected... ")
        return client.database
    except errors.ConnectionFailure as e:
        raise ConnectionError(f"Error de conexión: {str(e)}")
