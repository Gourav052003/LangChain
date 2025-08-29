from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
load_dotenv()

tweet_llm = ChatOpenAI()
linkedIn_llm = ChatOpenAI()
parser = StrOutputParser()

topic_prompt = PromptTemplate(
    template = "Tell me a joke about {topic}.", 
    input_variables=["topic"]
)

tweet_prompt = PromptTemplate(
    template = "Summarize the following joke in a tweet: {joke}",
    input_variables=["joke"]
)

linkedIn_prompt = PromptTemplate(
    template = "Summarize the following joke in a LinkedIn post: {joke}",
    input_variables=["joke"]
)

parallel_chain = RunnableParallel({
    "tweet": RunnableSequence(tweet_prompt, tweet_llm, parser),
    "linkedIn": RunnableSequence(linkedIn_prompt, linkedIn_llm, parser)
})

result = parallel_chain.invoke({"joke": "Why did the chicken cross the road? To get to the other side!"})

print(result)