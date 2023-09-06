import uuid
from datetime import datetime

import paho.mqtt.client as mqtt
import json
import time
import random

# MQTT broker settings
mqtt_broker_host = "unique-mosquitto"
mqtt_broker_port = 1883

client = mqtt.Client()
client.connect(mqtt_broker_host, mqtt_broker_port, 60)

while True:
    sensor1_id = "sensor1"
    sensor1_value = random.uniform(0, 100)
    sensor1_timestamp = datetime.now().isoformat()

    sensor1_payload = {
        "sensor_id": sensor1_id,
        "sensor_type": "temperature",
        "value": sensor1_value,
        "timestamp": sensor1_timestamp
    }

    sensor1_topic = "sensors/sensor1"
    client.publish(sensor1_topic, json.dumps(sensor1_payload))
    print("Published Sensor 1 (Temperature):", sensor1_payload)

    sensor2_id = "sensor2"
    sensor2_value = random.uniform(40, 80)
    sensor2_timestamp = datetime.now().isoformat()

    sensor2_payload = {
        "sensor_id": sensor2_id,
        "sensor_type": "humidity",
        "value": sensor2_value,
        "timestamp": sensor2_timestamp
    }

    sensor2_topic = "sensors/sensor2"
    client.publish(sensor2_topic, json.dumps(sensor2_payload))
    print("Published Sensor 2 (Humidity):", sensor2_payload)
    time.sleep(40)
