from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
load_dotenv()
import os


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

parser=StrOutputParser()

template1= PromptTemplate(
    template="Generate A Important Notes as a specialist Teacher for the following  text \n {Text}.",
    input_variables=["Text"]
)

template2= PromptTemplate(
    template="Generate Quiz of 3 Very very important Question from the   {Text}.",
    input_variables=["Text"]
)

template3= PromptTemplate(
    template="merge the provided notes and quiz into a single document \n Notes --->{notes} \n and quize---> {quiz}.",
    input_variables=["notes","quiz"]
)

# What RunnableParellel takes as Input?
# it takes a dictionary having both or all branches of parallel chain as key value pair.
# 
parallel_chain=RunnableParallel(
    { "notes": template1 | model | parser,
     "quiz":template2 | model | parser
    }
)

Text="""Support vector machines (SVMs) are powerful yet flexible supervised machine learning algorithm which is used for both classification and regression. But generally, they are used in classification problems. In 1960s, SVMs were first introduced but later they got refined in 1990 also. SVMs have their unique way of implementation as compared to other machine learning algorithms. Now a days, they are extremely popular because of their ability to handle multiple continuous and categorical variables.
Working of SVM
The goal of SVM is to find a hyperplane that separates the data points into different classes. A hyperplane is a line in 2D space, a plane in 3D space, or a higher-dimensional surface in n-dimensional space. The hyperplane is chosen in such a way that it maximizes the margin, which is the distance between the hyperplane and the closest data points of each class. The closest data points are called the support vectors.

The distance between the hyperplane and a data point "x" can be calculated using the formula 

distance = (w . x + b) / ||w|| 
where "w" is the weight vector, "b" is the bias term, and "||w||" is the Euclidean norm of the weight vector. The weight vector "w" is perpendicular to the hyperplane and determines its orientation, while the bias term "b" determines its position.

The optimal hyperplane is found by solving an optimization problem, which is to maximize the margin subject to the constraint that all data points are correctly classified. In other words, we want to find the hyperplane that maximizes the margin between the two classes while ensuring that no data point is misclassified. This is a convex optimization problem that can be solved using quadratic programming.

If the data points are not linearly separable, we can use a technique called kernel trick to map the data points into a higher-dimensional space where they become separable. The kernel function computes the inner product between the mapped data points without computing the mapping itself. This allows us to work with the datapoints in the higherdimensional space without incurring the computational cost of mapping them."""

merge_chain= template3 | model | parser

final_chain=parallel_chain | merge_chain

result=final_chain.invoke({"Text":Text})



print(result)  # Output the response from the LLM


final_chain.get_graph().print_ascii() # Visualize the chain grap