from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# what we are doing---> finding embedding vectors of each lines , them finiding cosine similarity of all the lines, then we will use standard deviation for  breakpoint. if similarity is more than standard deviation ,for consecutive sentenses (amount=1) , it will break
text_splitter_semantic=SemanticChunker(
    OpenAIEmbeddings(),breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1
)

text="""The farmer wakes up at 5 AM every day, carefully tending to his fields, checking the soil and watering his crops by hand. He relies heavily on seasonal rain and hopes for a good harvest. the IPL starting early, he makes sure he finishes early to catch the evening matches, especially to watch MS Dhoni’s comeback in yellow.

The rain poured nonstop for hours, soaking the muddy streets and creating large puddles all around the village. Children made paper boats and screamed with laughter. everyone gathered to watch a rerun of Shah Rukh Khan’s famous movie where he runs through the rain in slow motion.
 """

docs=text_splitter_semantic.create_documents([text])

print(len(docs))
print(docs)