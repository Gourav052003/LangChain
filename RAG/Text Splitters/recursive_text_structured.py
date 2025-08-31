from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """In the early years of my life, I was blessed with a loving family and a nurturing environment that fostered my growth and development. My parents, both of whom were deeply spiritual individuals, instilled in me the values of compassion, kindness, and a strong sense of purpose. From a young age, I was encouraged to explore the world around me, to ask questions, and to seek out knowledge wherever it could be found.

This early foundation laid the groundwork for my lifelong journey of self-discovery and spiritual exploration. As I grew older, I found myself drawn to the teachings of various spiritual traditions, seeking to understand the deeper truths that underlie our existence. This quest for knowledge ultimately led me to study under several renowned spiritual masters, each of whom imparted valuable wisdom and guidance that would shape my path.
"""

splitter = RecursiveCharacterTextSplitter(  

    chunk_size=100,
    chunk_overlap=20,
    separators=["\n\n", "\n", " ", ""] #para -> sentence -> word -> characters
)

#chunkviz.up.railway.app

chunks = splitter.split_text(text)

print(chunks)
print(len(chunks))


