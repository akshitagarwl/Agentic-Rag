from fastapi import FastAPI

app = FastAPI(title="Agentic RAG API", version="1.0.0")

@app.get("/health")
async def health_check():
    return {
        "status": "healthy", 
        "message": "Agentic RAG API is running perfectly!"
    }