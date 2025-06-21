import pandas as pd
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document
import os
import pickle

# Load FAQ from CSV
df = pd.read_csv("faq.csv")

# Convert rows to LangChain documents
docs = [
    Document(page_content=row["Answer"], metadata={"question": row["Question"]})
    for _, row in df.iterrows()
]

# Create embeddings using Hugging Face (free model)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Create FAISS index
db = FAISS.from_documents(docs, embeddings)

# Save the index
os.makedirs("vector_store", exist_ok=True)
with open("vector_store/faiss_index.pkl", "wb") as f:
    pickle.dump(db, f)

print("✅ FAISS index created at vector_store/faiss_index.pkl")
