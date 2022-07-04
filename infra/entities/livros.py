from infra.configs.base import Base
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
#from sqlalchemy.orm import relationship

class Livros(Base):
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True)
    id_doador = Column(Integer, ForeignKey("doadores.id"))
    titulo = Column(String, nullable=False)
    genero = Column(String, nullable=True)
    status = Column(Boolean, nullable=False)
    #id_doador = relationship("Doadores", backref="doadores", lazy="subquery")

    def __repr__(self):
        return f"Livro [titulo={self.titulo}, genero={self.genero}, disponível={self.status}]"
