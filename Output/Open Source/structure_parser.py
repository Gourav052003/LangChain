from langchain_openai import ChatOpenAI
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

schema = [
    ResponseSchema(name="name", description="name of the person"),
    ResponseSchema(name="age", description="age of the person"),
    ResponseSchema(name="city", description="city of the person"),
]

# cannot do data validatition like pydantic
parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Give me a name, age and city of a fictional person \n {format_instructions}",
    input_variables=[],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

chain = template | model | parser
final_output = chain.invoke({})
print(final_output)
print(type(final_output))