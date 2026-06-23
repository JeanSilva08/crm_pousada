from fastapi import FastAPI
from backend.app.database.database import engine, Base
from backend.app.routes import clientes
from backend.app.routes import fichas

# Garantir que os modelos sejam importados antes de criar as tabelas
from backend.app.models.cliente import Cliente
from backend.app.models.fichas import Ficha  # <-- Ajustado para 'fichas' no plural!

app = FastAPI(
    title="CRM Pousada API",
    description="Sistema de gestão de clientes e digitalização de fichas com IA",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

# Inclui as rotas na aplicação
app.include_router(clientes.router)
app.include_router(fichas.router)

@app.get("/")
def home():
    return {
        "status": "online"
    }