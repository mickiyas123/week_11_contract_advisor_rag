from fastapi import FastAPI, HTTPException
from langchain.vectorstores.cassandra import Cassandra
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import AstraDB
from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter
from typing import Dict

import os
from PyPDF2 import PdfReader
from dotenv import load_dotenv
from fastapi.responses import JSONResponse

app = FastAPI()

# Load environment variables
current_directory = os.getcwd()
env_path = os.path.abspath(os.path.join(current_directory, '..', '..', '.env'))
load_dotenv(env_path)

# OpenAI configuration
llm = OpenAI(openai_api_key=OPENAI_API_KEY)
embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

# AstraDB configuration
astra_vector_store = AstraDB(
    embedding=embedding,
    collection_name="test",
    token=ASTRA_DB_APPLICATION_TOKEN,
    api_endpoint=ASTRA_DB_API_ENDPOINT,
)

# Text splitting
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=800,
    chunk_overlap=200,
    length_function=len,
)

# Add texts to AstraDB
pdf_path = 'Raptor Contract.docx.pdf'
pdfReader = PdfReader(pdf_path)
raw_text = ''
for i, page in enumerate(pdfReader.pages):
    content = page.extract_text()
    if content:
        raw_text += content
texts = text_splitter.split_text(raw_text)
astra_vector_store.add_texts(texts[:50])

# Create VectorStoreIndexWrapper
astra_vector_index = VectorStoreIndexWrapper(vectorstore=astra_vector_store)

# FastAPI endpoint
@app.post("/generate_answer")
async def generate_answer(data: Dict[str, str]):
    question = data.get("question")
    if not question:
        raise HTTPException(status_code=400, detail="Question not provided")

    answer = astra_vector_index.query(question, llm=llm).strip()
    return JSONResponse(content={"answer": answer})
