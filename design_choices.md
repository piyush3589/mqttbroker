Insight into the Design Choices and Rationale

In this section, we provide a deeper understanding of the design decisions that shaped our project's architecture and the reasoning behind them. These decisions were instrumental in achieving the project's goals efficiently and effectively.
Choice of MQTT for Communication

One of the foundational choices in our project was the adoption of MQTT (Message Queuing Telemetry Transport) as the communication protocol for simulating sensor behavior. The rationale behind this choice includes:

    Lightweight and Efficient: MQTT is known for its lightweight nature, making it ideal for IoT applications where resources are often limited. It minimizes bandwidth usage and reduces the processing burden on both sensors and the broker.

    Publish-Subscribe Model: MQTT's publish-subscribe model allows sensors to publish readings to specific topics, enabling a flexible and scalable communication paradigm. Subscribers can selectively receive data based on their interests.

Docker Containerization

We containerized critical services such as Mosquitto, MongoDB, and Redis using Docker. This choice was guided by the following considerations:

    Portability: Docker containers provide a consistent environment across different systems, ensuring that our project can be easily deployed and run on various platforms without compatibility issues.

    Scalability: Containers allow us to scale individual components independently, facilitating efficient resource allocation as our system grows.

MongoDB for Data Storage

MongoDB was chosen as our primary data storage solution due to its suitability for handling sensor data:

    Schema-less Design: MongoDB's flexible schema-less design aligns well with the dynamic and JSON-like structure of sensor payloads. This flexibility accommodates varying sensor types and data formats.

    Scalability: MongoDB's scalability features prepare our system for future data growth, ensuring that it can manage an expanding volume of sensor readings.

Redis for Real-time Data Management

We integrated Redis to manage the latest sensor readings in-memory, enhancing real-time access:

    Low Latency: Redis's in-memory database architecture ensures low-latency access to frequently requested data. This allows users to obtain real-time insights without imposing a heavy load on the primary data store (MongoDB).

FastAPI for API Development

The selection of FastAPI for building the API layer was motivated by several factors:

    Efficiency: FastAPI's asynchronous capabilities enable our API to handle a large number of concurrent requests efficiently, making it well-suited for real-time data retrieval.

    Automatic Documentation: FastAPI generates interactive API documentation, simplifying usage and reducing the learning curve for users.

Payload Structure for MQTT

Our choice of a specific JSON payload structure for MQTT messages is designed to provide essential information about each sensor reading. This structure ensures that data is transmitted comprehensively and consistently across the system.