# Python Comments Application

This is a basic Python application that allows users to add comments. The application has been built using Docker and can be easily deployed using Docker Compose.

## Features

- Add and view comments
- Persistent storage using a database

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

Follow these steps to get the application up and running:

### 1. Clone the Repository

```bash
git clone https://github.com/tbpcoder/comments-application.git
cd comments-application
```

### 2. Build and Push the Docker Image

The Docker image for this application has already been built and pushed to Docker Hub. You can pull it directly from Docker Hub using Docker Compose.

### 3. Run the Application

Use Docker Compose to run the application:

```bash
docker-compose up
```

This command will pull the Docker image from Docker Hub and start the application.

### 4. Access the Application

Once the containers are up and running, you can access the application in your web browser at `http://localhost:5000`.
