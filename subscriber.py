import sys

import paho.mqtt.client as mqtt
import json

import pymongo
import redis
from bson import json_util
from pymongo import MongoClient

# MQTT broker settings
mqtt_broker_host = "unique-mosquitto"
mqtt_broker_port = 1883

# MongoDB Settings
host = "unique-mongodb"
port = 27017
target_db = "sensor_data"

# Redis settings
redis_host = "unique-redis"
redis_port = 6379
redis_db = 0

redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)


def on_message(client, userdata, msg):
    payload = json.loads(msg.payload)
    print("Received:", payload)

    # Determine the collection name based on the sensor type
    sensor_type = payload.get("sensor_type", "unknown")
    collection_name = f"sensor_{sensor_type}"

    mongo_client = pymongo.MongoClient(
        f"mongodb://{host}:{port}")

    try:
        db = mongo_client[target_db]
        collection = db[collection_name]
        # Insert the payload into MongoDB collection
        collection.insert_one(payload)
        # Store the first 10 readings in a Redis list
        readings_list = "sensor_readings"
        serialized_payload = json.dumps(payload, default=json_util.default)
        redis_client.lpush(readings_list, serialized_payload)
        redis_client.ltrim(readings_list, 0, 9)
    except Exception as e:
        print(e)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        client.subscribe("sensors/sensor1")  # subscribing to  publisher topic
        client.subscribe("sensors/sensor2")  # subscribing to  publisher topic
    else:
        print("Failed to connect to MQTT broker")


client = mqtt.Client()
client.connect(mqtt_broker_host, mqtt_broker_port, 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
