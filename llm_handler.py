from PyPDF2 import PdfReader
from langchain.chains import RetrievalQA
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF file."""
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def create_qa_chain(text):
    """Create a QA chain with the processed text."""
    # Split text into chunks
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    texts = text_splitter.split_text(text)
    
    # Create embeddings and vector store
    embeddings = OpenAIEmbeddings(
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )
    vectorstore = FAISS.from_texts(texts, embeddings)
    
    # Create QA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=OpenAI(
            temperature=0.2,
            openai_api_key=os.getenv("OPENAI_API_KEY")
        ),
        chain_type="stuff",
        retriever=vectorstore.as_retriever(),
        return_source_documents=False
    )
    
    return qa_chain

def get_prompt_result(pdf_path, query):
    """Process PDF and return answer to query."""
    try:
        # Extract text from PDF
        text = extract_text_from_pdf(pdf_path)
        
        # Create QA chain
        qa_chain = create_qa_chain(text)
        
        # Get response
        response = qa_chain({"query": query})
        
        return response['result']
        
    except Exception as e:
        raise Exception(f"Error processing query: {str(e)}")