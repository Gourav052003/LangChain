# convert python function to runnable amd use it with other runnables
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnablePassthrough, RunnableBranch
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI()
parser = StrOutputParser()

def word_count(text: str) -> int:
    return len(text.split(" "))

report_prompt = PromptTemplate(
    template = "write a detailed report on {topic}.",
    input_variables=["topic"]
)

summary_prompt = PromptTemplate(
    template = "Summarize the following report: {report}",
    input_variables=["report"]
)


report_chain = RunnableSequence(report_prompt, llm, parser)
branch_chain = RunnableBranch(
    (lambda x: word_count(x) > 200, RunnableSequence(summary_prompt, llm, parser)),
    RunnablePassthrough()  # default case
)



final_chain = RunnableSequence(report_chain, branch_chain)

result = final_chain.invoke({"topic": "chickens"})
print(result)