from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

class Person(BaseModel):
    name: str = Field(description="The person's name")
    age: int = Field(gt=18,description="The person's age")
    city: str = Field(description="The city where the person lives")    
    
parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate a random person with name, age and city of a fictional {place} \n {format_instructions}",
    input_variables=["place"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# prompt = template.invoke({"place": "INDIA"}) 

chain = template | model | parser
result = chain.invoke({"place": "INDIA"})
print(result)  # Person(name='...', age=..., city='...') 