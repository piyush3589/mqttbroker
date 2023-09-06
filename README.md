# Mosquitto Broker 

 The purpose of this project is to simulate the behaviour of sensors, monitor their readings, and provide APIs to retrieve data based on specific criteria.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - Before installing Docker Desktop, make sure you meet the following prerequisites:

- [ ] **Operating System:** Docker Desktop is available for Windows and macOS. Ensure your system is running a supported version.

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
  - [Setup Instructions](#setup-instructions)
- [Services](#services)
  - [Service 1: MQTT Publisher](#service-1-mqtt-publisher)
  - [Service 2: MQTT Subscriber](#service-2-mqtt-subscriber)
  - [Service 3: FastAPI Application](#service-3-fastapi-application)
  - [Service 4: Mosquitto](#service-4-mosquitto)
  - [Service 5: MongoDB](#service-5-mongodb)
  - [Service 6: Redis](#service-6-redis)
- [Design Choices](#design-choices)
- [Challenges and Solutions](#challenges-and-solutions)

## System Overview

Provide an overview of the project, its purpose, and how it works.

## Getting Started

Explain how to set up and run the system using Docker Compose.

### Prerequisites

List any software or dependencies that need to be installed before running the system.

### Setup Instructions

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/your-repo.git
