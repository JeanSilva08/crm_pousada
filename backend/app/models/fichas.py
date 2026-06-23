from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone
from backend.app.database.database import Base


class Ficha(Base):
    __tablename__ = "fichas"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    nome_arquivo = Column(
        String,
        nullable=False
    )

    caminho = Column(
        String,
        nullable=False
    )

    # PENDENTE, PROCESSADO, ERRO
    status = Column(
        String,
        default="PENDENTE"
    )

    created_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc)
    )