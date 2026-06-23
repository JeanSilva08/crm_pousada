from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.database.database import get_db  # <-- Importando do lugar certo agora!
from backend.app.models.cliente import Cliente
from backend.app.schemas.cliente import ClienteCreate

router = APIRouter()


@router.post("/clientes")
def criar_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    # O '**' desempacota automaticamente todos os campos da ficha (nome, cpf, chale, datas...)
    novo_cliente = Cliente(**cliente.model_dump())
    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)
    return novo_cliente

@router.get("/clientes")
def listar_clientes(db: Session = Depends(get_db)):
    return db.query(Cliente).all()