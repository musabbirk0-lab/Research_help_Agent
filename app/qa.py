import numpy as np
from app.ingest import EMBED_MODEL, create_or_load_index

def retrieve(query: str, k=3):
    vec = EMBED_MODEL.encode([query], convert_to_numpy=True)
    index = create_or_load_index(vec.shape[1])
    D, I = index.search(vec, k)
    return I[0].tolist()
