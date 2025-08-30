from langchain_community.document_loaders import WebBaseLoader

urls = ["https://www.freespiritualebooks.com/autobiography-of-a-yogi.html","https://indivyoga.com/5-spiritual-books-that-changed-my-life/"]
docs = WebBaseLoader(urls).load()

print(docs)