# FastAPI Basics
1. Run the FastAPI server:

    ```bash
    uvicorn myapi:app --reload
    ```

2. Navigate to [http://localhost:8000/docs](http://localhost:8000/docs) in your browser to view the Swagger UI documentation. 

## Endpoints

### 1. Get Student by ID

- **URL**: `/get-student/{student_id}`
- **Method**: `GET`
- **Description**: Retrieve student information by ID.
- **Parameters**:
  - `student_id` (path parameter): The ID of the student to retrieve.
- **Response**:
  - Returns student information if found.
  - Returns an error message if the student ID does not exist.

### 2. Get Student by Name

- **URL**: `/get-by-name`
- **Method**: `GET`
- **Description**: Retrieve student information by name.
- **Parameters**:
  - `name` (query parameter): The name of the student to retrieve.
- **Response**:
  - Returns student information if found.
  - Returns an error message if the student name does not exist.

### 3. Create Student

- **URL**: `/create-student/{student_id}`
- **Method**: `POST`
- **Description**: Create a new student.
- **Parameters**:
  - `student_id` (path parameter): The ID of the student to create.
  - Request body: JSON object containing student details (name, age, year).
- **Response**:
  - Returns the created student information.
  - Returns an error message if the student ID already exists.

### 4. Update Student

- **URL**: `/update-students/{student_id}`
- **Method**: `PUT`
- **Description**: Update existing student information.
- **Parameters**:
  - `student_id` (path parameter): The ID of the student to update.
  - Request body: JSON object containing fields to update (name, age, year).
- **Response**:
  - Returns the updated student information.
  - Returns an error message if the student ID does not exist.

### 5. Delete Student

- **URL**: `/delete-student/{student_id}`
- **Method**: `DELETE`
- **Description**: Delete a student by ID.
- **Parameters**:
  - `student_id` (path parameter): The ID of the student to delete.
- **Response**:
  - Returns a success message if the student is deleted.
  - Returns an error message if the student ID does not exist.
