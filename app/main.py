from fastapi import FastAPI
from pydantic import BaseModel
from app.scraper import download_pdf
from app.extractor import pdf_to_text
from app.ingest import add_documents
from app.qa import retrieve

app = FastAPI()

class IngestRequest(BaseModel):
    url: str

class QARequest(BaseModel):
    query: str

@app.post('/ingest')
def ingest(req: IngestRequest):
    path = download_pdf(req.url)
    text = pdf_to_text(path)
    # split minimally by paragraphs
    chunks = [c for c in text.split('\n\n') if len(c) > 50][:10]
    ids = [path + f"::chunk{i}" for i in range(len(chunks))]
    add_documents(chunks, ids)
    return {"status": "ok", "ingested_chunks": len(chunks)}

@app.post('/qa')
def qa(req: QARequest):
    ids = retrieve(req.query)
    return {"candidates": ids}
