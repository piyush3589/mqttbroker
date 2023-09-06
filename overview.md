
## Overview of Services Used in Docker Compose File

This project includes several Dockerized services to support different functionalities:

### 1. MongoDB Service (`mongodb-service`)

- **Description:** MongoDB is a NoSQL database used to store sensor data.
- **Docker Image:** Official MongoDB image (latest).
- **Ports:** Exposes port 27017 for MongoDB connections.
- **Volume:** Persists MongoDB data in `./mongodb-data`.
- **Configuration:** Uses a custom MongoDB configuration file located at `./mongodb-config/mongod.conf`.
- **Authentication:** No authentication is enabled.

### 2. Mosquitto Broker (`mosquitto-broker`)

- **Description:** Mosquitto is an MQTT broker for lightweight messaging.
- **Docker Image:** toke/mosquitto.
- **Ports:** Exposes MQTT port 1883 and WebSocket port 9001.

### 3. Redis (`redis`)

- **Description:** Redis is an in-memory data store used for caching.
- **Docker Image:** Official Redis image (latest).
- **Ports:** Exposes Redis port 6379.

### 4. Publisher (`publisher`)

- **Description:** The publisher service sends sensor data to the MQTT broker.
- **Build Context:** Uses Dockerfile.publisher for building.
- **Depends On:** Depends on Mosquitto broker and Subscriber for initialization.
- 
### 5. Subscriber (`subscriber`)

- **Description:** The subscriber service receives sensor data from the MQTT broker and stores it in MongoDB.
- **Build Context:** Uses Dockerfile.subscriber for building.
- **Depends On:** Depends on Mosquitto broker and MongoDB service for initialization.

### 6. FastAPI App (`fastapi-app`)

- **Description:** The FastAPI application provides RESTful APIs for accessing sensor data stored in MongoDB.
- **Build Context:** Uses Dockerfile.fastapi for building.
- **Depends On:** Depends on MongoDB service for initialization.
- **Ports:** Exposes FastAPI on port 8000.