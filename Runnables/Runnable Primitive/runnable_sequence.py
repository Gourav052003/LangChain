from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI()
parser = StrOutputParser()

joke_prompt = PromptTemplate(
    template = "Tell me a joke about {topic}.",
    input_variables=["topic"]
)

explain_prompt = PromptTemplate(
    template = "Explain the joke: {joke}",
    input_variables=["joke"]
)

chain = RunnableSequence(joke_prompt, llm, parser, explain_prompt, llm, parser)
result = chain.invoke({"topic": "chickens"})
print(result)