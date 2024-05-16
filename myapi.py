import fastapi
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


#1. PATH PARAMETER
#parameters are added either by path or query
students = {
    1:{
       "name": "John",
       "age": 17,
       "year": "Year 12"
       }
}
#google.com/get-student: we will get all the student details
#google.com/get-student/1: we will get student with id:1

#The BaseModel class in Pydantic is the base class for defining data models. 
#This is needed for post methods
class Student(BaseModel):
    name: str
    age: int
    year: str
    
#2. QUERY PARAMETER
#google.com/results?search=Python: The query parameter is search=Python
#search=Python: key=value

#PUT METHOD
class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


#MY FIRST API
#create an endpoint
#localhost/delete-user: delete-user is the end point

#GET: Get an information
#POST: Create something new
#PUT: Update data
#DELETE: Remove/delete something

@app.get("/") #home: google.com
def index(): #we can name it anything
    return {"name": "First Data"}

#we normally have to return JSON data
#app is the variabla name 

#path parameters
@app.get("/get-student/{student_id}")  #{}: variable 
def get_student(student_id: int= Path(..., description= "The ID of the student you want to view", gt=0)):  #gt= 0: the ID should be greater than 0
    return students[student_id]
# Path(None): will bring empty data

#...: you indicate to FastAPI that this parameter is required, and the client must provide it

#description: description of the path parameter

#gt and ge: These parameters set the minimum value for the path parameter. gt stands for "greater than", and ge stands for "greater than or equal to".

#lt and le: These parameters set the maximum value for the path parameter. lt stands for "less than", and le stands for "less than or equal to".

#regex: This parameter allows you to specify a regular expression pattern that the path parameter must match.


#query parameters
@app.get("/get-by-name")
def get_student(name: str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
        
    return {"Data": "Not found"}
    
    
#combining both path and query 
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the student you want to view", gt=0),
                name: str = Query(None, description="The name of the student")):
    if name is not None:
        # If name is provided as a query parameter, search by name
        for id, student in students.items():
            if student["name"] == name:
                return student
        return {"Data": "Student with name '{}' not found".format(name)}
    else:
        # If name is not provided, return student by ID
        if student_id in students:
            return students[student_id]
        else:
            return {"Data": "Student with ID '{}' not found".format(student_id)}
        
        
#post method
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student : Student):
    #This parameter represents the student data sent in the request body. It's expected to conform to the Student model, which likely contains fields such as name, age, year.
    if student_id in students:
        return {"Error": "Student exists"}
    
    #adds new students
    students[student_id] = student
    return students[student_id]

#put method
@app.put("/update-students/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist."}
    
    if student.name is not None:
        students[student_id].name = student.name
        
    if student.age is not None:
        students[student_id].age = student.age
    
    if student.year is not None:
        students[student_id].year = student.year
        
    return students[student_id]

#delete method
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return{"Error": "Student does not exist"}
    
    del students[student_id]
    return{"Message": "Student deleted sucesssfully."}

