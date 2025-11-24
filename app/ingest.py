from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from pathlib import Path
from typing import List

EMBED_MODEL = SentenceTransformer('all-MiniLM-L6-v2')
INDEX_DIR = Path('./data/index')
INDEX_DIR.mkdir(parents=True, exist_ok=True)

index = None
ids = []

def embed_texts(texts: List[str]) -> np.ndarray:
    return EMBED_MODEL.encode(texts, convert_to_numpy=True)

def create_or_load_index(d: int):
    global index
    if (INDEX_DIR / 'index.faiss').exists():
        index = faiss.read_index(str(INDEX_DIR / 'index.faiss'))
    else:
        index = faiss.IndexFlatL2(d)
    return index

def add_documents(doc_texts: List[str], doc_ids: List[str]):
    vecs = embed_texts(doc_texts)
    d = vecs.shape[1]
    create_or_load_index(d)
    index.add(vecs)
    faiss.write_index(index, str(INDEX_DIR / 'index.faiss'))
    # minimal persistence for ids
    with open(INDEX_DIR / 'ids.txt', 'a') as f:
        for _id in doc_ids:
            f.write(_id + "\n")

if __name__ == '__main__':
    add_documents(["hello world"], ["doc1"])
