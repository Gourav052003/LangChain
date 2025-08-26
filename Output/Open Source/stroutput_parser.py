from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
import os

load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
# )

# llm = HuggingFacePipeline.from_model_id(
#     model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation",
#     pipeline_kwargs=dict(
#         temperature = 0.5,
#         max_length = 1000,
#     )
# )

model = ChatOpenAI()

# 1st prompt -> detailed report

template_1 =PromptTemplate(
    template="Write a 5 line detailed report on {topic}.",
    input_variables=["topic"]
)


# 2nd prompt -> summary of the report

template_2 =PromptTemplate(
    template="Write a concise {count} line summary of the following report: {report}",
    input_variables=["report","count"]
)

parser = StrOutputParser()

# Chain 1: Generate detailed report
report_chain = template_1 | model | parser

# Get the report
report = report_chain.invoke({"topic": "Artificial Intelligence"})

# Chain 2: Summarize the report
summary_chain = template_2 | model | parser

# Get the summary
summary = summary_chain.invoke({"report": report, "count": 2})

print(summary)