from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model='gpt-4')
result = model.invoke("Who is the best: Elon Musk or Jeff Bezos?")
print(result)