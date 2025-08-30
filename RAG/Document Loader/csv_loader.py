from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='fmnist_small.csv', encoding='utf-8')
docs = loader.load()
print(docs[0])
print(len(docs))