

# Project e-Delta Personnel Management API

This is a FastAPI-based server script designed for **Project e-Delta** to manage personnel information and their access levels to SAP resources. The API allows you to create, retrieve, update, and delete personnel records.

---

## Features

- **Create Personnel**: Add new personnel with details such as name, email, role, and SAP access level.
- **Retrieve Personnel**: Fetch all personnel records or a specific record by email.
- **Update Personnel**: Modify existing personnel records.
- **Delete Personnel**: Remove personnel records by email.
- **In-Memory Storage**: Stores personnel data in memory (replace with a database for production use).

---

## Prerequisites

Before running the API, ensure you have the following installed:

- Python 3.7 or higher
- `pip` (Python package manager)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/project-e-delta.git
   cd project-e-delta
   ```

2. Install the required dependencies:
   ```bash
   pip install fastapi uvicorn
   ```

---

## Running the API

1. Start the server using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

2. The API will be available at:
   ```
   http://127.0.0.1:8000
   ```

3. Access the interactive API documentation (Swagger UI) at:
   ```
   http://127.0.0.1:8000/docs
   ```

---

## API Endpoints

### 1. **Root Endpoint**
- **GET `/`**
  - Returns a welcome message.
  - Example response:
    ```json
    {
      "message": "Welcome to Project e-Delta Personnel Management API"
    }
    ```

### 2. **Create Personnel**
- **POST `/personnel/`**
  - Adds a new personnel record.
  - Request body:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com",
      "role": "Developer",
      "sap_access_level": "Read"
    }
    ```
  - Example response:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com",
      "role": "Developer",
      "sap_access_level": "Read"
    }
    ```

### 3. **Get All Personnel**
- **GET `/personnel/`**
  - Retrieves all personnel records.
  - Example response:
    ```json
    [
      {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "role": "Developer",
        "sap_access_level": "Read"
      }
    ]
    ```

### 4. **Get Personnel by Email**
- **GET `/personnel/{email}`**
  - Retrieves a specific personnel record by email.
  - Example response:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com",
      "role": "Developer",
      "sap_access_level": "Read"
    }
    ```

### 5. **Update Personnel**
- **PUT `/personnel/{email}`**
  - Updates an existing personnel record by email.
  - Request body:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com",
      "role": "Senior Developer",
      "sap_access_level": "Write"
    }
    ```
  - Example response:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com",
      "role": "Senior Developer",
      "sap_access_level": "Write"
    }
    ```

### 6. **Delete Personnel**
- **DELETE `/personnel/{email}`**
  - Deletes a personnel record by email.
  - Example response:
    ```json
    {
      "message": "Personnel deleted successfully"
    }
    ```

---

## Example Requests

### Using `curl`

1. **Create Personnel**:
   ```bash
   curl -X POST "http://127.0.0.1:8000/personnel/" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com", "role": "Developer", "sap_access_level": "Read"}'
   ```

2. **Get All Personnel**:
   ```bash
   curl -X GET "http://127.0.0.1:8000/personnel/"
   ```

3. **Get Personnel by Email**:
   ```bash
   curl -X GET "http://127.0.0.1:8000/personnel/john.doe@example.com"
   ```

4. **Update Personnel**:
   ```bash
   curl -X PUT "http://127.0.0.1:8000/personnel/john.doe@example.com" -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john.doe@example.com", "role": "Senior Developer", "sap_access_level": "Write"}'
   ```

5. **Delete Personnel**:
   ```bash
   curl -X DELETE "http://127.0.0.1:8000/personnel/john.doe@example.com"
   ```

---

