from sqlalchemy import Column, Integer, String, Date
from backend.app.database.database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(150), nullable=False)
    cpf = Column(String(14), nullable=True)
    rg = Column(String(12), nullable=True)
    endereco = Column(String(255), nullable=True)
    cidade = Column(String(100), nullable=True)
    estado = Column(String(50), nullable=True)
    cep = Column(String(9), nullable=True)
    telefone = Column(String(20), unique=True, nullable=True)
    email = Column(String(150), nullable=True)
    profissao = Column(String(100), nullable=True)
    placa_carro = Column(String(100), nullable=True)
    chale = Column(String(50), nullable=True)
    data_checkin = Column(Date, nullable=True)
    data_checkout = Column(Date, nullable=True)
    passaporte = Column(String(50), nullable=True)