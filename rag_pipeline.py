import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from vector_handler import process_uploaded_pdf  

# Load environment variables from .env
load_dotenv()

# Ensure GROQ_API_KEY is set
if not os.getenv("GROQ_API_KEY"):
    raise ValueError("GROQ_API_KEY environment variable not set. Please set it in your .env file.")

# Initialize the LLM model (GROQ API key is automatically used from env)
llm_model = ChatGroq(model_name="llama3-70b-8192")  # Recommended model; change if needed

# Prompt template
custom_prompt_template = """
Use the pieces of information provided in the context to answer the user's question.
If you don't know the answer, just say that you don't know. Don't try to make up an answer. 
Only provide information found in the context.

Question: {question}
Context: {context}

Answer:
"""

# Function to get an answer using the model and prompt
def answer_query(documents, model, query):
    context = '\n\n'.join([doc.page_content for doc in documents])
    prompt = ChatPromptTemplate.from_template(custom_prompt_template)
    
    # Create the chain with output parsing
    chain = prompt | model | StrOutputParser()
    
    return chain.invoke({'question': query, 'context': context})
