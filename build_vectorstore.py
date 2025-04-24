import os
import fitz  # PyMuPDF
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

DATA_FOLDER = "data"
VECTORSTORE_PATH = "vector_store"

def extract_text_from_pdfs(folder_path):
    print("[INFO] Extracting text from all PDFs in folder...")
    documents = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.pdf'):
            full_path = os.path.join(folder_path, filename)
            print(f"[INFO] Extracting from: {filename}")
            doc = fitz.open(full_path)
            text = ""
            for page in doc:
                text += page.get_text()
            documents.append(Document(page_content=text, metadata={"source": filename}))
    return documents

def create_vectorstore(docs):
    print("[INFO] Splitting text into chunks...")
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)

    print("[INFO] Loading embedding model...")
    embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

    print("[INFO] Creating and saving vector store...")
    vectordb = FAISS.from_documents(chunks, embedding)
    vectordb.save_local(VECTORSTORE_PATH)
    print(f"[SUCCESS] Vector store saved to '{VECTORSTORE_PATH}'.")

if __name__ == "__main__":
    all_docs = extract_text_from_pdfs(DATA_FOLDER)
    create_vectorstore(all_docs)
