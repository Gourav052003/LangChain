from langchain.text_splitter import RecursiveCharacterTextSplitter,Language

text = """

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}
    
    def is_passing(self, passing_grade=50):
        return self.grade >= passing_grade

#example usage

student1 = Student("Alice", 14, "8th")
print(student1.get_details())

if student1.is_passing(40):
    print(f"{student1.name} is passing.")
else:
    print(f"{student1.name} is not passing.")
    
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, # can also be done with markdown language.MARKDOWN
    chunk_size=330,
    chunk_overlap=0,
)

chunks = splitter.split_text(text)
print(chunks)
print(len(chunks))
print(chunks[0])