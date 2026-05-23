from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os   
import streamlit as st
from langchain_core.prompts import PromptTemplate
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

model=ChatOpenAI(
    model="gpt-3.5-turbo")

st.header("Research paper summarizer")

# instead of taking a static prompt from each user , we will ask user to select a research paper, style and length of the summary.
# this will make the prompt dynamic and more user friendly, and give every user similar experience.
# we will use a prompt template to create a dynamic prompt based on user input.

paper_input=st.selectbox(
    "Select a research paper to summarize",["attention is all you need","BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
                                            
"GPT-3: Language Models are Few-Shot Learners","diffusion models beat GANs on image synthesis","DALL·E 2: Creating Images from Text"])

style_input=st.selectbox(
    "Select a style for the summary",["Beginner friendly","core","Technical","Mathematical"])

lenght_input=st.selectbox(
    "Select the length of the summary",["Short-(1-2 paragraph)","Medium- (2-4 paragrsph)","Long-(4-6 paragraph)"])

# Define the prompt template
# it takes two things , 1. template and 2. input_variables
template=PromptTemplate(
template="""
You are an expert research assistant.

Please summarize the research paper titled: "{paper_input}" using the following criteria:

Explanation Style: {style_input}  
Desired Length: {length_input}

Guidelines:
1. **Mathematical Details**
   - Include mathematical equations if they are relevant to the content.
   - Clearly explain mathematical concepts using intuitive examples or simple pseudocode where appropriate.

2. **Use of Analogies**
   - Simplify complex concepts using relatable analogies or real-world comparisons.

3. **Handling Missing Information**
   - If any detail is not available in the paper, respond with:  
     "Insufficient information available."  
   - Do **not** guess or hallucinate content.

Ensure your response is clear, structured, and easily understandable by someone with basic subject knowledge.
""",
input_variables=["paper_input","style_input","length_input"]
)

# Create the prompt using the template -filling the placeholders with the user inputs
# prompt is a string with the placeholders filled with the user inputs
prompt=template.format(
    paper_input=paper_input,
    style_input=style_input,
    length_input=lenght_input
)
# Call the model with the prompt
result=model.invoke(prompt)  # Example usage
if st.button("Generate Summary"):
    # Display the result
    st.subheader("Summary")
    st.write(result.content)  # Output the content of the response