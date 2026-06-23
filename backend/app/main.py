from fastapi import FastAPI
from backend.app.database.database import Base, engine
from backend.app.models import cliente
from backend.app.routes import clientes  # <-- Importa as rotas

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Inclui as rotas do cliente na aplicação
app.include_router(clientes.router)

@app.get("/")
def home():
    return {
        "status": "online"
    }