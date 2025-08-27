from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate       
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

model_1 = ChatOpenAI()
model_2 = ChatOpenAI()
parser = StrOutputParser()


prompt_1 = PromptTemplate(
    template = "Generate shor tand simple notes on {text}",    
    input_variables = ["text"]
)

prompt_2 = PromptTemplate(
    template = "Create a quiz with 3 questions from the following notes: {text}",
    input_variables = ["text"]
)

prompt_3 = PromptTemplate(  
    template="Merge the following notes and quiz into a single text:\nNotes: {notes}\nQuiz: {quiz}",
    input_variables=["notes", "quiz"]
)

parallel_chain = RunnableParallel({
    'notes': prompt_1 | model_1 | parser,
    'quiz': prompt_2 | model_2 | parser
})

merged_chain = prompt_3 | model_1 | parser

chain = parallel_chain | merged_chain

text = """
In mathematics, the Taylor series or Taylor expansion of a function is an infinite sum of terms that are expressed in terms of the function's derivatives at a single point. For most common functions, the function and the sum of its Taylor series are equal near this point. Taylor series are named after Brook Taylor, who introduced them in 1715. A Taylor series is also called a Maclaurin series when 0 is the point where the derivatives are considered, after Colin Maclaurin, who made extensive use of this special case of Taylor series in the 18th century.

The partial sum formed by the first n + 1 terms of a Taylor series is a polynomial of degree n that is called the nth Taylor polynomial of the function. Taylor polynomials are approximations of a function, which become generally more accurate as n increases. Taylor's theorem gives quantitative estimates on the error introduced by the use of such approximations. If the Taylor series of a function is convergent, its sum is the limit of the infinite sequence of the Taylor polynomials. A function may differ from the sum of its Taylor series, even if its Taylor series is convergent. A function is analytic at a point x if it is equal to the sum of its Taylor series in some open interval (or open disk in the complex plane) containing x. This implies that the function is analytic at every point of the interval (or disk).
 
"""

chain_output = chain.invoke({"text": text})

print(chain_output)
chain.get_graph().print_ascii()


