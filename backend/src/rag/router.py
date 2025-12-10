from fastapi import APIRouter, UploadFile, File, HTTPException
from src.rag.qdrant_service import QdrantRAG
from src.rag.llm_service import ask_llm
from src.utils.pdf_loader import load_pdf_text


router = APIRouter()

rag = QdrantRAG()


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """Sube un PDF o TXT y lo indexa en Qdrant."""
    if file.filename.endswith(".txt"):
        text = (await file.read()).decode("utf-8")

    elif file.filename.endswith(".pdf"):
        text = load_pdf_text(await file.read())

    else:
        raise HTTPException(status_code=400, detail="Invalid file type")

    # Podríamos dividir en chunks, pero para este MVP lo guardamos directo
    rag.add_document(text)

    return {"message": "Document indexed successfully"}


@router.post("/query")
async def query_rag(prompt: str):
    """Busca contexto en Qdrant y pregunta al modelo local."""
    results = rag.search(prompt)

    context = "\n".join(results)

    final_prompt = f"""
    You are a helpful assistant. Use ONLY the following context to answer.

    CONTEXT:
    {context}

    QUESTION:
    {prompt}

    Answer using the information provided above.
    """

    response = ask_llm(final_prompt)

    return {
        "query": prompt,
        "context_used": results,
        "response": response
    }
