import json

import pymongo
from bson import ObjectId
from fastapi import FastAPI, HTTPException, Query
from bson.json_util import dumps, loads
from pymongo import MongoClient, DESCENDING
from starlette.responses import JSONResponse


# This class is useful when you're working with MongoDB ObjectId objects and want to ensure they are serialized as strings in JSON.
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super().default(obj)


custom_json_encoder = CustomJSONEncoder()
# Create a FastAPI app
app = FastAPI()

# MongoDB's connection settings
host = "unique-mongodb"  # MongoDB container's IP
port = 27017  # Default MongoDB port
target_db = "sensor_data"  # database name

# Establish a connection to MongoDB
try:
    # Establish a connection to MongoDB
    client = pymongo.MongoClient(
        f"mongodb://{host}:{port}")
    db = client[target_db]
    sensor_humidity_collection = db["sensor_humidity"]
    sensor_temperature_collection = db["sensor_temperature"]

    # Check if the connection is successful
    if db.command("ping")["ok"] == 1.0:
        print("Successfully connected to MongoDB.")
    else:
        print("Failed to connect to MongoDB.")  # Replace with the name of your collection
except Exception as e:
    print(f"An error occurred: {str(e)}")


@app.get("/sensor_readings/")
async def get_sensor_readings(
        start_range: str = Query(..., description="Start timestamp in ISO format (e.g., '2023-09-01T00:00:00')"),
        end_range: str = Query(..., description="End timestamp in ISO format (e.g., '2023-09-05T00:00:00')"),
):
    # Query the MongoDB collections based on the timestamp range
    sensor_humidity_data = sensor_humidity_collection.find({
        "timestamp": {"$gte": start_range, "$lte": end_range}
    })

    sensor_temperature_data = sensor_temperature_collection.find({
        "timestamp": {"$gte": start_range, "$lte": end_range}
    })

    # Convert query results to lists of dictionaries
    humidity_readings = [reading for reading in sensor_humidity_data]
    temperature_readings = [reading for reading in sensor_temperature_data]

    for reading in humidity_readings:
        reading["_id"] = str(reading["_id"])
    for reading in temperature_readings:
        reading["_id"] = str(reading["_id"])

    # Return the sensor readings as JSON
    response_data = {
        "sensor_temperature": temperature_readings,
        "sensor_humidity": humidity_readings,
    }

    return response_data


@app.get("/last_ten_sensor_readings")
async def get_last_ten_sensor_readings(
        sensor_type: str = Query(..., description="Sensor type (e.g., 'temperature' or 'humidity')")
):
    # Query the MongoDB collections to get the last ten readings for the specified sensor
    humidity_readings = sensor_humidity_collection.find(
        {"sensor_type": sensor_type}
    ).sort("timestamp", DESCENDING).limit(10)

    temperature_readings = sensor_temperature_collection.find(
        {"sensor_type": sensor_type}
    ).sort("timestamp", DESCENDING).limit(10)

    # Convert query results to lists of dictionaries
    humidity_data = [{"_id": str(reading["_id"]), "value": reading["value"], "timestamp": reading["timestamp"]} for
                     reading in humidity_readings]
    temperature_data = [{"_id": str(reading["_id"]), "value": reading["value"], "timestamp": reading["timestamp"]} for
                        reading in temperature_readings]

    # Check if any readings were found for the specified sensor
    if not humidity_data and not temperature_data:
        raise HTTPException(status_code=404, detail="No readings found for the specified sensor.")

    # Return the sensor readings as JSON
    response_data = {
        "sensor_temperature": temperature_data,
        "sensor_humidity": humidity_data,
    }

    return response_data
