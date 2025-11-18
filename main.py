"""
AmbedkarGPT - RAG-based Q&A System
Built for Kalpit Pvt Ltd AI Intern Assignment
Author: Mayank Daryani
Date: 18 November 2025

This system uses LangChain to create a Retrieval-Augmented Generation (RAG) pipeline
that answers questions based on Dr. B.R. Ambedkar's speech text.
"""

import os
import sys
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

# Configuration
SPEECH_FILE = "speech.txt"
CHROMA_DB_DIR = "./chroma_db"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "mistral"

def check_prerequisites():
    """Check if all required files and dependencies are available."""
    print(" Checking prerequisites...")
    
    # Check if speech.txt exists
    if not os.path.exists(SPEECH_FILE):
        print(f" Error: {SPEECH_FILE} not found!")
        print("Please create speech.txt with the provided text.")
        sys.exit(1)
    
    print(f" Found {SPEECH_FILE}")
    print(" All prerequisites met!\n")

def load_and_split_document():
    """Load the speech text and split it into manageable chunks."""
    print(" Loading document...")
    
    # Load the text file
    loader = TextLoader(SPEECH_FILE, encoding='utf-8')
    documents = loader.load()
    
    print(f" Loaded {len(documents)} document(s)")
    
    # Split text into chunks
    # Using smaller chunk size with overlap to maintain context
    text_splitter = CharacterTextSplitter(
        chunk_size=200,  # Smaller chunks for better retrieval
        chunk_overlap=50,  # Overlap to maintain context
        separator="\n"
    )
    
    chunks = text_splitter.split_documents(documents)
    print(f" Split into {len(chunks)} chunks\n")
    
    return chunks

def create_vector_store(chunks):
    """Create embeddings and store them in ChromaDB."""
    print(" Creating embeddings and vector store...")
    print("(This may take a moment on first run as the model downloads)")
    
    # Initialize HuggingFace embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={'device': 'cpu'},  # Use CPU for compatibility
        encode_kwargs={'normalize_embeddings': True}
    )
    print("embedding is completed")
    
    # Create or load Chroma vector store
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DB_DIR
    )


    


    
    # Persist the database
    vectorstore.persist()
    
    print(f" Vector store created with {len(chunks)} embeddings")
    print(f" Stored in {CHROMA_DB_DIR}\n")
    
    return vectorstore


    
    


def initialize_llm():
    """Initialize the Ollama LLM with Mistral model."""
    print(" Initializing Ollama LLM with Mistral 7B")
    
    try:
        llm = Ollama(
            model=LLM_MODEL,
            temperature=0.7,  # Balanced creativity
            top_p=0.9
        )
        
        # Test the LLM
        test_response = llm("Say 'Hello'")
        print(" LLM initialized successfully\n")
        
        return llm
    
    except Exception as e:
        print(f" Error initializing LLM: {e}")
        print("\nMake sure Ollama is installed and Mistral is pulled:")
        print("  1. Install: curl -fsSL https://ollama.ai/install.sh | sh")
        print("  2. Pull model: ollama pull mistral")
        print("  3. Test: ollama run mistral")
        sys.exit(1)

def create_qa_chain(vectorstore, llm):
    """Create a RetrievalQA chain combining the vector store and LLM."""
    print(" Creating RAG pipeline...")
    
    # Create retriever from vector store
    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}  # Retrieve top 3 most relevant chunks
    )
    
    # Create RetrievalQA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",  # 'stuff' means all retrieved docs are stuffed into prompt
        retriever=retriever,
        return_source_documents=True,  # Return sources for transparency
        verbose=False
    )
    
    print(" RAG pipeline ready!\n")
    
    return qa_chain

def ask_question(qa_chain, question):
    """Query the RAG system with a question."""
    print(f" Question: {question}\n")
    print(" Thinking...\n")
    
    try:
        # Get answer from the chain
        result = qa_chain({"query": question})
        
        answer = result['result']
        source_docs = result['source_documents']
        

        print("=" * 80)
        print(" ANSWER:")
        print("=" * 80)
        print(f"{answer}\n")
        

        print("=" * 80)
        print(" SOURCES (Retrieved Context):")
        print("=" * 80)
        for i, doc in enumerate(source_docs, 1):
            print(f"\nSource {i}:")
            print(f"{doc.page_content[:200]}...")
        print("=" * 80 + "\n")
        
        return answer
    
    except Exception as e:
        print(f" Error during query: {e}")
        return None

def interactive_mode(qa_chain):
    """Run the system in interactive mode for multiple questions."""
    print("\n" + "=" * 80)
    print(" AmbedkarGPT - Interactive Q&A Mode")
    print("=" * 80)
    print("Ask questions about Dr. Ambedkar's speech on caste.")
    print("Type 'quit', 'exit', or 'q' to stop.\n")
    

    while True:
        try:
            question = input("Your question: ").strip()
            
            if question.lower() in ['quit', 'exit', 'q', '']:
                print("\n Thank you for using AmbedkarGPT!")
                break
            
            print()
            ask_question(qa_chain, question)
            
        except KeyboardInterrupt:
            print("\n\n Thank you for using AmbedkarGPT!")
            break
        except Exception as e:
            print(f" Error: {e}\n")

def main():
    """Main execution flow."""
    print("\n" + "=" * 80)
    print(" AmbedkarGPT - RAG Q&A System")
    print("=" * 80 + "\n")
    
    # Step 1: Check prerequisites
    check_prerequisites()
    
    # Step 2: Load and split document
    chunks = load_and_split_document()
    
    # Step 3: Create vector store with embeddings
    vectorstore = create_vector_store(chunks)
    
    # Step 4: Initialize LLM
    llm = initialize_llm()
    
    # Step 5: Create QA chain
    qa_chain = create_qa_chain(vectorstore, llm)
    
    # Step 6: Demo questions
    print(" DEMO: Asking sample questions...\n")
    
    demo_questions = [
        "What does Ambedkar say about the shastras?",
        "What is the real remedy according to the text?",
        "How does Ambedkar compare social reform to gardening?"
    ]
    
    for question in demo_questions:
        ask_question(qa_chain, question)
        print("\n")
    
    # Step 7: Interactive mode
    interactive_mode(qa_chain)

if __name__ == "__main__":
    main()