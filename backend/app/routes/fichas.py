import os
import uuid
from typing import List  # <-- Adicionado para a listagem
from shutil import copyfileobj
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session

from backend.app.database.database import get_db
from backend.app.models.fichas import Ficha
from backend.app.schemas.fichas import FichaResponse

router = APIRouter(prefix="/fichas", tags=["Fichas"])

# Garante que a pasta uploads/ exista na raiz do projeto
UPLOAD_DIR = os.path.join(os.getcwd(), "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload", response_model=FichaResponse, status_code=201)
def upload_ficha(file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Valida se o arquivo enviado é uma imagem suportada
    extensao = os.path.splitext(file.filename)[1].lower()
    if extensao not in [".jpg", ".jpeg", ".png"]:
        raise HTTPException(
            status_code=400,
            detail="Apenas arquivos JPG, JPEG ou PNG são suportados."
        )

    # Gera um nome único com UUID para evitar sobrescrever arquivos com o mesmo nome
    id_unico = uuid.uuid4().hex
    novo_nome_arquivo = f"{id_unico}_{file.filename}"
    caminho_completo = os.path.join(UPLOAD_DIR, novo_nome_arquivo)

    # Salva a imagem fisicamente no seu HD/SSD
    try:
        with open(caminho_completo, "wb") as buffer:
            copyfileobj(file.file, buffer)
    except Exception:
        raise HTTPException(status_code=500, detail="Falha ao salvar o arquivo no servidor.")

    # Registra a ficha no banco de dados com status PENDENTE
    nova_ficha = Ficha(
        nome_arquivo=novo_nome_arquivo,
        caminho=caminho_completo,
        status="PENDENTE"
    )

    db.add(nova_ficha)
    db.commit()
    db.refresh(nova_ficha)

    return nova_ficha


# 📄 NOVA ROTA: Listar todas as fichas enviadas (Bom para a dashboard)
@router.get("/", response_model=List[FichaResponse])
def listar_fichas(db: Session = Depends(get_db)):
    return db.query(Ficha).all()


# 🔍 NOVA ROTA: Buscar os detalhes de uma única ficha pelo ID
@router.get("/{ficha_id}", response_model=FichaResponse)
def obter_ficha_por_id(ficha_id: int, db: Session = Depends(get_db)):
    ficha = db.query(Ficha).filter(Ficha.id == ficha_id).first()
    if not ficha:
        raise HTTPException(status_code=404, detail="Ficha não encontrada.")
    return ficha