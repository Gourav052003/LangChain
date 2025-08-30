from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI()
prompt = PromptTemplate(
    template="Write a poem for the following topic: {text}",
    input_variables=["text"],
)
parser = StrOutputParser()
loader = TextLoader('knowledge.txt', encoding='utf8')
docs = loader.load()

def load_text(file_path):
    text = TextLoader(file_path, encoding='utf8').load()[0].page_content
    return text

text_runnable = RunnableLambda(load_text)

chain = text_runnable | prompt | llm | parser
print(chain.invoke("knowledge.txt"))
# print(chain.invoke({"text": docs[0].page_content}))

# print(docs[0].page_content)
# print(docs[0].metadata)
# print(type(docs))
# print(type(docs[0]))
# print(len(docs))