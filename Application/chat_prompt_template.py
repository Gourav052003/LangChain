from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage 

# chat_template = ChatPromptTemplate([
#     SystemMessage(content="You are a helpful {domain} expert."),
#     HumanMessage(content="Explain the topic of {topic}")
# ])

# chat_template = ChatPromptTemplate.from_messages([
#     ('system', "You are a helpful {domain} expert."),
#     ('human', "Explain the topic of {topic}")
# ])

chat_template = ChatPromptTemplate([
    ('system', "You are a helpful {domain} expert."),
    ('human', "Explain the topic of {topic}")
])

prompt = chat_template.invoke({
    "domain": "machine learning",
    "topic": "transformers"
})

print(prompt)