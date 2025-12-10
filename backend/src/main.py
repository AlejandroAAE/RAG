from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routes
from src.auth.routes import router as auth_router
from src.rag.router import router as rag_router


app = FastAPI(
    title="RAG Backend - 100% Local and Free",
    description="Retrieval-Augmented Generation system using FastAPI, Qdrant, Ollama and Embeddings",
    version="1.0.0"
)

# CORS (opcional, pero profesional)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers (de momento solo están definidos los archivos)
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(rag_router, prefix="/rag", tags=["RAG"])


@app.get("/", tags=["Root"])
async def root():
    return {"message": "RAG Backend running successfully!"}
