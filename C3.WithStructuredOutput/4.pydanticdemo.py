from pydantic import BaseModel , EmailStr ,Field
from typing import Optional

# Pydantic is a data validation and settings management library for Python, which uses Python type annotations.
# It allows you to define data models with type annotations and provides validation, serialization, and parsing capabilities.
# field  can  take description, default value, and validation constraints.
class student(BaseModel):
    name: str
    age: Optional[int]=None  # age is optional, if not provided it will be None
    grade: str
    email:EmailStr
    cgpa:float= Field(default=0.0, ge=0.0, le=10.0 , description="this is value of Students end semester exam.")  # cgpa should be between 0.0 and 10.0

new_student ={"name":"rk",
              "age": "20", #type coercion will happen, so no need to worry about type mismatch.
              # "age": 20, # this will also work, but we are passing string
              "grade": "A",
              "email": "rk@gmail.com",
              "cgpa": 9.5}  # cgpa is optional, default value will be used if not provided
student=student(**new_student)

print(student)

# type of student is <class 'pydantic.main.Student'>
print(type(student))


# converting student into json
student_json = student.model_dump_json()
print(student_json)  

# converting student into dictionary
student_dict = student.model_dump()  
print(student_dict)


# use of Model_dump_json and Model_dump
# 1. `model_dump_json()` converts the Pydantic model instance into a JSON
#    string representation, which can be useful for serialization or sending data over a network.
# 2. `model_dump()` converts the Pydantic model instance into a Python dictionary
#    representation, which can be useful for further processing or manipulation in Python.

