from infra.configs.base import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class Clientes(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False)
    doadores = relationship("Doadores", backref="doadores", lazy="subquery")
    #doadores = relationship("Doadores", backref="doadores", lazy="subquery")
    def __repr__(self):
        return f"Cliente [nome={self.nome}, email={self.email}]"
