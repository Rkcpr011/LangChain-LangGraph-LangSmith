from langchain_community.retrievers import WikipediaRetriever


wikiretriever=WikipediaRetriever(
    lang="en",
    top_k_results=3
)

query="geometrical history of india and pakistan?"

docs=wikiretriever.invoke(query)

for i , doc in enumerate(docs):
    print(f"\n----result{i+1}")
    print(f"conten--\n {doc.page_content}")