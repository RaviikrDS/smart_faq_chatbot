from fastapi import FastAPI
from pydantic import BaseModel
from langchain_community.vectorstores import FAISS
import pickle

app = FastAPI()

# Load FAISS index
with open("vector_store/faiss_index.pkl", "rb") as f:
    db = pickle.load(f)

retriever = db.as_retriever()

# Define input format
class Query(BaseModel):
    question: str

# Query endpoint
@app.post("/query")
def get_answer(query: Query):
    docs = retriever.get_relevant_documents(query.question)
    if docs:
        return {"answer": docs[0].page_content}
    else:
        return {"answer": "Sorry, I couldn't find an answer to that question."}
