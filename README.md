# Mosquitto Broker 

 ## Overview

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

##  Instructions for Getting Started
- Before installing Docker Desktop, make sure you meet the following prerequisites:

- **Operating System:** Docker Desktop is available for Windows and macOS. Ensure your system is running a supported version.

### Installation Steps

Follow the appropriate installation guide for your operating system:

#### Windows

1. Visit the [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/) page in the Docker documentation.

2. Download the Docker Desktop Installer for Windows from the provided link.

3. Double-click the downloaded installer file to start the installation process.

4. Follow the on-screen instructions to complete the installation. This may involve enabling virtualization, configuring Docker settings, and creating a Docker account.

5. Once the installation is complete, Docker Desktop should be up and running.

#### macOS

1. Visit the [Docker Desktop for macOS](https://docs.docker.com/desktop/install/mac-install/) page in the Docker documentation.

2. Download the Docker Desktop Installer for macOS from the provided link.

3. Double-click the downloaded installer file to open it.

4. Drag the Docker icon to the Applications folder to install Docker Desktop.

5. Launch Docker Desktop from the Applications folder.

### Verification

To verify that Docker Desktop is installed and running correctly, open a terminal or command prompt and run the following command:

```bash
docker --version
```

## Cloning the Project

Follow these steps to clone this project to your local machine:

### Prerequisites

Before you begin, ensure that you have Git installed on your computer. If Git is not already installed, you can download and install it from the [official Git website](https://git-scm.com/).

### Cloning via HTTPS

If you prefer to clone using HTTPS, use the following steps:

1. Open your terminal or command prompt.

2. Navigate to the directory where you want to store the project.

3. Run the following command to clone the repository:

   ```bash
   git clone https://github.com/piyush3589/mqttbroker.git
   ```


## Building and Running the Project

Follow these steps to build and run the project using Docker Compose:

### 1. Clone the Repository

If you haven't already, clone this repository to your local machine as described in the [Cloning the Project](#cloning-the-project) section.

### 2. Navigate to the Project Directory

Open your terminal or command prompt and navigate to the project directory. Use the `cd` command to change your working directory to where you cloned the project:

```bash
cd path/to/your/project-directory
```

Replace path/to/your/project-directory with the actual path to the project folder on your machine.
### 3. Build the Docker Container

Once you're in the project directory, use Docker Compose to build the project's containers. Run the following command:

```bash
docker-compose build
```

This command will build the Docker containers specified in the docker-compose.yml file. The build process may take some time, depending on your project's complexity.
### 4. Start the Project

After the build is complete, you can start the project with Docker Compose:

```bash
docker-compose up
```

This command will start all the services defined in the docker-compose.yml file. You should see logs indicating that your project is running.
### 5. Access the Project
All services will get started and then you can access fast api at 
```bash
http://localhost:8000
```
Here are some example API endpoints:

- **List All Sensors:**
  - URL: `/sensor_readings`
  - Method: GET
  - Description: An endpoint that allows users to fetch sensor readings by specifying a start and end    range.
  - example:http://localhost:8000/sensor_readings/?start_range=2023-09-05T00:00:00&end_range=2023-09-05T23:59:00

- **Get Sensor Readings by Type:**
  - URL: `/last_ten_sensor_readings`
  - Method: GET
  - Description: Retrieves the last ten sensor readings of a specific type (e.g., 'temperature' or 'humidity').
  - example:http://localhost:8000/last_ten_sensor_readings?sensor_type=humidity
 
![Include](external.md)















