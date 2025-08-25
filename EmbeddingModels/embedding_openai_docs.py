from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)
documents = [
    "Delhi is the capital of India",
    "Paris is the capital of France",  
    "Tokyo is the capital of Japan",
    "Canberra is the capital of Australia",
    "Ottawa is the capital of Canada",
]

result = embedding.embed_documents(documents)

print(result)

