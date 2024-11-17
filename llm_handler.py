from PyPDF2 import PdfReader
from langchain.chains import QAChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Function to create the QAChain
def create_qa_chain():
    llm = OpenAI(api_key=OPENAI_API_KEY, temperature=0.2)
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="Context: {context}\n\nQuestion: {question}\nAnswer:",
    )
    return QAChain(llm=llm, prompt=prompt)

# Function to process PDF and query
def get_prompt_result(pdf_file, query):
    try:
        # Extract text from the PDF
        pdf_text = extract_text_from_pdf(pdf_file)

        # Initialize QAChain
        qa_chain = create_qa_chain()

        # Run the query and get the result
        result = qa_chain.run(context=pdf_text, question=query)
        return result
    except Exception as e:
        raise RuntimeError(f"Error processing query: {str(e)}")
