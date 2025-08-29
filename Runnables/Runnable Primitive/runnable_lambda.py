# convert python function to runnable amd use it with other runnables
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI()
parser = StrOutputParser()

def word_count(text: str) -> int:
    return len(text.split(" "))

joke_prompt = PromptTemplate(
    template = "Tell me a joke about {topic}.",
    input_variables=["topic"]
)


joke_chain = RunnableSequence(joke_prompt, llm, parser)

parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "word_count": RunnableLambda(word_count)
    # "word_count": RunnableLambda(lambda text: len(text.split(" ")))  # using lambda function
})

final_chain = RunnableSequence(joke_chain, parallel_chain)

result = final_chain.invoke({"topic": "chickens"})
print(result)