from pydantic import BaseModel
from datetime import datetime

class FichaResponse(BaseModel):
    id: int
    nome_arquivo: str
    caminho: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True