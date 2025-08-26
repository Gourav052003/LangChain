from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate,load_prompt
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("Research Tool")

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

# template = PromptTemplate(
#     template="Summarize the research paper '{paper}' in a {style} style with a {length} length.",
#     input_variables=["paper", "style", "length"],
#     validate_template=True,
# )

template = load_prompt('template.json')

model = ChatOpenAI()

if st.button('Summerize'):
    
    chain = template | model
    chain_result = chain.invoke({
        "paper": paper_input,
        "style": style_input,
        "length": length_input
    })
    
    st.write(chain_result.content)
    # prompt = template.invoke({
    # "paper": paper_input,
    # "style": style_input,
    # "length": length_input
    # })
    
    # result = model.invoke(prompt)
    # st.write(result.content)
    
    