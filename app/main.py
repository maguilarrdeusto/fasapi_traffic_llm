from fastapi import FastAPI
from app.routes import optimize

app = FastAPI(title="Traffic LLM API", description="API para optimización de tráfico")

# Incluir rutas
app.include_router(optimize.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "API de optimización de tráfico en FastAPI"}
