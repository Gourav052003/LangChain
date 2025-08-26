from pydantic import BaseModel,EmailStr, Field
from typing import Optional

# class Student(BaseModel):
#     name: str
    
class Student(BaseModel):
    name: str = "Unknown"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0.0, lt=10.0, default=5, description="A decimal value representing thte score of student")  # cgpa must be between 0.0 and 10.0
    
    
# new_student = {}
# new_student = {"name": 32} # This will raise a validation error
# new_student = {"name": "John Doe", "age": '21'}  # type coercion will convert '21' to 21 
# new_student = {"name": "John Doe", "age": 'dfgdf'} # This will raise a validation error
# new_student = {"name": "John Doe", "age": 21}
# new_student = {"name": "John Doe", "age": 21, "email": "abc"} # This will raise a email validation error
# new_student = {"name": "John Doe", "age": 21, "email": "abc@gmail.com"}
new_student = {"name": "John Doe", "age": 21, "email": "abc@gmail.com", "cgpa": 9.2}

student = Student(**new_student)

print(student)
# print(student.name)
print(type(student)) # <class '__main__.Student'> a pydantic object
print(student.age)
student_dict = dict(student) # {'name': 'John Doe', 'age': 21, 'email': 'abc@Gmil.com', 'cgpa': 9.2}
print(student_dict['age'])

student_json = student.model_dump_json()
print(student_json) # {"name": "John Doe", "age": 21, 
