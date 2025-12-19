from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel
from db.session import engine
from contextlib import asynccontextmanager

from api.v1.router import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    from db.session import engine
    from sqlmodel import SQLModel

    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(
    lifespan=lifespan,
    title="RAG Backend - 100% Local and Free",
    description="Retrieval-Augmented Generation system using FastAPI, Qdrant, Ollama and Embeddings",
    version="1.0.0"
)


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas API profesionales
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "RAG Backend running successfully!"}


