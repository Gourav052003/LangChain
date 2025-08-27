from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate(
    template="Write a 5 interesting facts on {topic}.",
    input_variables=["topic"]
)

model = ChatOpenAI()
parser = StrOutputParser()

#LCEl (language chain expression)
chain = prompt | model | parser

chain_output = chain.invoke({"topic": "Space Exploration"})

print(chain_output)

chain.get_graph().print_ascii()  # visualize the chain graph



