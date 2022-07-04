from infra.configs.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Doadores(Base):
    __tablename__ = "doadores"

    id = Column(Integer, primary_key=True)
    id_cliente = Column(Integer, ForeignKey("clientes.id"))
    livros = relationship("Livros", backref="livros", lazy="subquery")
    def __repr__(self):
        return f"Doadores [id={self.id}, id_cliente={self.id_cliente}]"