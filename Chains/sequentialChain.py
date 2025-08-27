from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()

# 1st prompt -> detailed report
template_1 =PromptTemplate(
    template="Write a 5 line detailed report on {topic}.",
    input_variables=["topic"]
)

template_2 = PromptTemplate(
    template="Write a concise summary of the following report: {report}",
    input_variables=["report"]
)

chain = template_1 | model | parser | template_2 | model | parser   

chain_output = chain.invoke({"topic": "Artificial Intelligence"})   

print(chain_output)

chain.get_graph().print_ascii()  # visualize the chain graph
