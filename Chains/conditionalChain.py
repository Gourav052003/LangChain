from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain.schema.runnable import RunnableBranch, RunnableLambda
from pydantic import BaseModel,Field
from typing import Literal
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment:Literal['positive','negative']=Field(description="Give the sentiment of the feedback")
   
pydantic_parser = PydanticOutputParser(pydantic_object=Feedback)

prompt_1 = PromptTemplate(
    template="Classify the sentiments of the following text into positive or negative\n {feedback} \n{format_instruction}",
    input_variables=["feedback"],
    partial_variables={'format_instruction':pydantic_parser.get_format_instructions()}
)

prompt_2 = PromptTemplate(
    template="Write an appropriate repsonse to positive feedback\n {feedback}",
    input_variables=["feedback"]
)

prompt_3 = PromptTemplate(
    template="Write an appropriate repsonse to negative feedback\n {feedback}",
    input_variables=["feedback"]
)

classifier_chain = prompt_1 | model | pydantic_parser
branch_chain = RunnableBranch(
    (lambda x:x.sentiment=='positive',prompt_2|model|parser),
    (lambda x:x.sentiment=='negative',prompt_3|model|parser),
    RunnableLambda(lambda x: "Could not find sentiment") # not made a chain that's why we made runnable lambda it converts labda function to runnable then it can be used as chain
)

chain = classifier_chain | branch_chain

# result = classifier_chain.invoke({"feedback":"this is a terrible smart phone"}).sentiment

print(chain.invoke({"this is a wonderful smart phone"}))

chain.get_graph().print_ascii()