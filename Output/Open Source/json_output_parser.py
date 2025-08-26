from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser

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
parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me a name, age and city of a fictional person \n {format_instructions}",
    input_variables=[],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

# prompt = template.format()

# print(prompt)

# result = model.invoke(prompt)

# final_output = parser.parse(result.content)

#does not enforce a schema (solved by structured output parser)
chain = template | model | parser
final_output = chain.invoke({})

print(final_output)
print(type(final_output))
print(final_output['name'])