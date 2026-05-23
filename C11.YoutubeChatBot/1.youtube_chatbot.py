from langchain_openai import ChatOpenAI ,OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from youtube_transcript_api import YouTubeTranscriptApi , TranscriptsDisabled
import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
# step1 doc load , split and embed , store it in fiass
video_id="Gfr50f6ZBvo"
try:
   ytube_api = YouTubeTranscriptApi()
   fetched_transcripts=ytube_api.fetch(video_id , languages=["en","hindi"])
   transcript="".join(chunk.text for chunk in fetched_transcripts)
#    print(transcript)
   print(fetched_transcripts[-1]) #last transcript
   print(len(fetched_transcripts))
   print(transcript)
except TranscriptsDisabled:
   print("no captions available for this video")  


# chunking
splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
chunks=splitter.create_documents(transcript)


# embedding
embedding=OpenAIEmbeddings()
vstore=FAISS.from_documents(chunks,embedding)


# # retriever formation
retriever=vstore.as_retriever(search_kwargs={"k":4})
# result=retriever.invoke("what is the deep mind?")
# print(result)




# augmentation
llm=ChatOpenAI()
prompt=PromptTemplate(
   template="""you are a helpful assistant.
   Answer  the question only from the provided  transcript context.
   If the context is insufficient , please make a polite and professional , reply saying I do not have knowledge.
 
   Context---->\n {context}
   question ----> \n {question}
    """,
    input_variables=["context","question"]
)
question="is the topic Aliens disccused in video? if yes please explain it"
retrieved_docs=retriever.invoke(question)


# final full context
context_text="\n\n".join(doc.page_content for doc in retrieved_docs)


# final prompt
final_prompt=prompt.invoke({"context":context_text , "question":question})


# step4 Response generation
answer=llm.invoke(final_prompt)
print(answer.content)


# # building a chain for this
from langchain_core.runnables import RunnableParallel,RunnableSequence , RunnablePassthrough , RunnableLambda
from langchain_core.output_parsers import StrOutputParser


def format_docs(retrieved_docs):
   context_text="\n\n".join(docs.page_content for docs in retrieved_docs)
   return context_text


parallel_chain=RunnableParallel({
   "context":retriever|RunnableLambda(format_docs),
   "question":RunnablePassthrough()
})
parallel_chain.invoke("who is Demis")


parser=StrOutputParser()


main_chain=parallel_chain |prompt| llm |parser
main_chain.invoke("can you summarize the video?")




