from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader #best for text pdf and there are other PDF loaders for image pdfs

# text = """In the early years of my life, I was blessed with a loving family and a nurturing environment that fostered my growth and development. My parents, both of whom were deeply spiritual individuals, instilled in me the values of compassion, kindness, and a strong sense of purpose. From a young age, I was encouraged to explore the world around me, to ask questions, and to seek out knowledge wherever it could be found.
# """

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20, #for context pass on 10-20 percent is good number, more overlpap more chunks less chunks less ccontext
    separator=""
)

loader = PyPDFLoader('autobiography-of-a-yogi.pdf')
docs = loader.load()

# chunks = splitter.split_text(text) # for text only
chunks = splitter.split_documents(docs) # for documents with metadata # each page is splited into chunks

print(chunks)
print(len(docs))
print(len(chunks))

print(chunks[0]) # each chunk in itself is document with metadata for pdf