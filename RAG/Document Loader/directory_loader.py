from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader

# Loader for PDFs
pdf_loader = DirectoryLoader(
    path="documents",
    glob="**/*.pdf",
    loader_cls=PyPDFLoader
)

# Loader for TXT files
txt_loader = DirectoryLoader(
    path="documents",
    glob="**/*.txt",
    loader_cls=TextLoader
)

pdf_content = pdf_loader.lazy_load()

# Load both
txt_content =  txt_loader.load()

for doc in pdf_content:
    print(doc)

print(txt_content)
# print(f"Loaded {len(docs)} documents")
# print(docs[0].page_content[:300])  # preview first 300 chars
# print(docs[0].metadata)

# docs = loader.lazy_load()
# docs = loader.load()

# for doc in docs:
#     print(doc)
# print(docs)