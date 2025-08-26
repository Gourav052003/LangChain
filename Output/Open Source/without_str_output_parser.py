from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
import os

load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
# )

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature = 0.5,
        max_length = 1000,
    )
)

model = ChatHuggingFace(llm=llm)

# 1st prompt -> detailed report

template_1 =PromptTemplate(
    template="Write a 5 line detailed report on {topic}.",
    input_variables=["topic"]
)


# 2nd prompt -> summary of the report

template_2 =PromptTemplate(
    template="Write a concise 2 line summary of the following report: {report}",
    input_variables=["report"]
)

# prompt_1 = template_1.format(topic="Artificial Intelligence")
prompt_1 = template_1.invoke({"topic": "Artificial Intelligence"})

detailed_report = model.invoke(prompt_1)
print(detailed_report)
# prompt_2 = template_2.format(report=detailed_report)
prompt_2 = template_2.invoke({"report": detailed_report.content})

summary = model.invoke(prompt_2)

print(summary.content)

