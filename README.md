# Feature Engineering API

This is a simple API for performing feature engineering on customer data. It calculates various statistics and aggregates features for each customer based on their loan data.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the API](#running-the-api)
  - [Performing Feature Engineering](#performing-feature-engineering)
- [API Endpoints](#api-endpoints)
- [Sample Data](#sample-data)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

Follow the instructions below to get the project up and running on your local machine.

### Prerequisites

- Python 3.7 or higher
- Docker (For containerization)
- Postman or similar API testing tool (optional)

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Teokiller16e/feature-engineering-api.git

2. Install FastApi library:
   ```bash
    pip install fastapi
3. Install uvicorn library:
    ```bash
    pip install uvicorn

4. Navigate to the project directory
    ```bash
    cd feature-engineering-api
5. Install the required Python packages or feel free to change the requirements.txt file based on your versions of packages:
    ```bash
    pip install -r requirements.txt


## Usage
### Running the API
You can run the API either directly or using Docker. Choose the method that suits your needs.

### Running the API Directly

1. Ensure you are in the project directory and the virtual environment is activated (if used).

2. Start the API:
    ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload

### Running the API with Docker

1. Build the Docker container:
    ```bash
   docker build -t feature-engineering-api .

2. Run the a Docker container and map it to port 80 on your local machine.:
     ```bash
   docker run -p 80:80 feature-engineering-api
3. In case you want to stop all Docker containers or a specific container:
    ```bash
    docker ps  || docker stop container_name_or_id


## Checking API health status: 
You can perform a health status check by making a GET request to the API endpoint /health/. 
You can use tools like Postman or curl for testing.
1. Checking health status:
    ```bash
    curl http://localhost:8000/health/

## Performing Feature Engineering: 
You can perform feature engineering check by making a GET request to the API endpoint /feature_engineering/. 
You can use tools like Postman or curl for testing.
1. Feature Engineering:
    ```bash
    curl http://localhost:8000/feature_engineering/


## Sample Data
1. Sample customer data in JSON format is provided in the cvas_data.json file. 

## Technologies Used
1. Python
2. FastAPI
3. NumPY
4. Docker
