from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from typing import TypedDict , Annotated ,Optional

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

Model= ChatOpenAI()

# providing the data fortmat and with_structured_output method calling before invoking the model.
# we have used Annotated to add metadata to the TypedDict fields, this will help LLm not to halucinate during generating the output.
# basically this will help to provide more context to the model about the fields.
# use of Optional: Optional is used to indicate that the field may or may not be present in the output.
class review(TypedDict):
    Key_themes:Annotated[list[str], "Key themes or topics discussed in the review"]
    Summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "The sentiment of the review, e.g., positive, negative, neutral"]
    pros:Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons:Annotated[Optional[list[str]], "Write down all the cons inside a list"]


structured_model=Model.with_structured_output(review)    

# now instead of callinf model and invoking we will invoke the structured_model.
response = structured_model.invoke(""""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don’t use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful

Cons:
Bulky and heavy—not great for one-handed use
Bloatware still exists in One UI
Expensive compared to competitors"
""")  # Example usage

# print(response)  # Output the response from the LLM

print(type(response))  # Output the type of the response

print("summary is:",response["Summary"])  # Output the summary from the response
print("sentiment is:",response["sentiment"])  # Output the sentiment from the response
print("key themes are:",response["Key_themes"])  # Output the key themes from the response
print("pros are:",response["pros"])  # Output the pros from the response    
print("cons are:",response["cons"])  # Output the cons from the response


# how it works:
# 1. We define a TypedDict called `review` that specifies the structure of the output we expect from the model.
# 2. We create a structured model using `with_structured_output` method, passing the `review` TypedDict.
# 3. We invoke the structured model with a text input.
# 4. The model processes the input and returns a response that matches the structure defined in the `review` TypedDict.
# 5. We can access the structured output using the keys defined in the TypedDict.
