from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()

model = ChatAnthropic(model='claude-3.5-sonnet-20241022')
result = model.invoke("Who is best Elon Musk or Jeff Bezos?")   

print(result)
