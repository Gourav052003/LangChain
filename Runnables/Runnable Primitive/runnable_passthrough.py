from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough
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

joke_chain = RunnableSequence(joke_prompt, llm, parser)

# runnable passthrough to pass the joke directly to the final output without any modification in input joke
parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "explanation": RunnableSequence(explain_prompt, llm, parser)
})

final_chain = RunnableSequence(joke_chain, parallel_chain)

result = final_chain.invoke({"topic": "chickens"})
print(result)