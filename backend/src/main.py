from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="FlowTask API",
    version="1.0.0",
    description="API de Orquestração de Tarefas com FastAPI e Clean Architecture"
)

# Configurando CORS para aceitar requisições do Nuxt (localhost:3000 por padrão)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "FlowTask API rodando com sucesso!"}