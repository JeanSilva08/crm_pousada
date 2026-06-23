from pydantic import BaseModel
from datetime import date

class ClienteCreate(BaseModel):
    nome: str
    cpf: str | None = None
    rg: str | None = None
    endereco: str | None = None
    cidade: str | None = None
    estado: str | None = None
    cep: str | None = None
    telefone: str | None = None
    email: str | None = None
    profissao: str | None = None
    placa_carro: str | None = None
    chale: str | None = None
    data_checkin: date | None = None
    data_checkout: date | None = None
    passaporte: str | None = None