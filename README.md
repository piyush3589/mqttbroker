# Mosquitto Broker 

 The purpose of this project is to simulate the behaviour of sensors, monitor their readings, and provide APIs to retrieve data based on specific criteria.

## Services Used in Docker Compose File

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

## Getting Started
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















