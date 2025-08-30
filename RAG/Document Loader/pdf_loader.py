from langchain_community.document_loaders import PyPDFLoader #best for text pdf and there are other PDF loaders for image pdfs

loader = PyPDFLoader('autobiography-of-a-yogi.pdf')
docs = loader.load()
print(docs[0].page_content)
print(docs[0].metadata)
print(len(docs))