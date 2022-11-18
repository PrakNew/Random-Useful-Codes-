from fastapi import FastAPI , Path
from typing import Optional
from pydantic import BaseModel


app = FastAPI()
#uvicorn FastAPI_totorial:app --reload

class Student(BaseModel):
    name : str
    age : int
    year : str

class UpdateStudent(BaseModel):
    name : Optional[str] = None
    age: Optional[int] = None
    year : Optional[str] = None

@app.get("/")
def index():
    return {'name':"prakhar newatia"}

students = {
    1:{
        "name":"shikhar newatia",
        "roll number":12345
    }
}

@app.get('/get-student/{student_id}')
def get_student(student_id : int = Path(None,description="The ID of the student you want to view",gt=0,lt=3)):
    return students[student_id]

#Query parameter

@app.get("/get-by-name") #http://127.0.0.1:8000/get-by-name?name=shikhar%20newatia 
def get_student(*, name: Optional[str] = None , id : int):
    # sourcery skip: use-next
    for student_id in students:
        if students[student_id]['name']==name:
            return students[student_id]
    return {'Data': "Not found"}


@app.post("/create-student/{student_id}")
def create_student(student_id : int , student : Student):
    if student_id in student:
        return {"Error":"Student exists"}
    
    students[student_id] = student
    return students[student_id]

@app.put('/update-student/{student_id}')
def update_student(student_id : int , student : UpdateStudent):
    if student_id not in students:
        return {"Error" : "Student does not exist"}
    
    if student.name !=None:
        students[student_id].name = student.name

    if student.age !=None:
        students[student_id].age = student.age
    
    if student.year !=None:
        students[student_id].year = student.year
    return students[student_id]


@app.delete('/delete-student/{student_id}')
def delete_student(student_id : int):
    if student_id not in students:
        return {"Error" : "Student not found"}
     
    del students[student_id]
    return {'Message' : "Student deleted successfully "}
