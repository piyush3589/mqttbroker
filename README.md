# Mosquitto Broker 

 ## Project Overview

**Purpose:** This project aims to simulate the behavior of sensors, monitor their readings, and provide APIs to retrieve sensor data based on specific criteria. It incorporates several technologies and services to achieve its objectives.

### Key Components

1. **MQTT Broker Setup:**
   - Deploys a Mosquitto MQTT broker using Docker to facilitate communication between sensor emulators and subscribers.

2. **MQTT Publisher:**
   - Implements a Python MQTT client responsible for emulating sensor readings.
   - Publishes sensor data to MQTT topics such as sensors/temperature and sensors/humidity.
   - Payload structure: `{ "sensor_id": "unique_sensor_id", "value": "<reading_value>", "timestamp": "ISO8601_formatted_date_time" }`.

3. **MQTT Subscriber:**
   - Develops a Python MQTT subscriber to capture and store incoming MQTT messages.
   - Stores the received data in a MongoDB collection for further analysis.

4. **Data Storage:**
   - Utilizes Docker to set up a MongoDB instance, which acts as the central data repository.
   - Saves the incoming MQTT sensor readings in the MongoDB database.

5. **In-Memory Data Management:**
   - Implements Redis using Docker to manage the latest ten sensor readings in-memory.
   - Provides a fast and efficient way to access recent sensor data.

6. **FastAPI Endpoint:**
   - Designs a FastAPI-based API with endpoints to interact with the collected sensor data.
   - Includes functionality to retrieve sensor readings within a specified time range and access the last ten readings for a specific sensor.

### Goals and Benefits

- Simulate Sensor Behavior: The project replicates sensor behavior, allowing users to generate and monitor sensor readings for testing and analysis.

- Data Storage and Retrieval: Sensor data is stored in MongoDB, offering a scalable and robust solution for long-term data storage.
  
- Real-time Access: Redis enables real-time access to the latest sensor readings, providing rapid insights into current conditions.

- FastAPI API: The FastAPI-based API offers a user-friendly interface to interact with the sensor data, making it easy to retrieve and analyze information.

This project combines the power of MQTT, MongoDB, Redis, and FastAPI to create a comprehensive system for simulating and managing sensor data, making it valuable for various applications requiring data analysis and monitoring.




 
![Include](design_choices.md)















