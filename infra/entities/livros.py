from infra.configs.base import Base
from sqlalchemy import Column, String, Integer
#from sqlalchemy.orm import relationship

class Livros(Base):
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True)
    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    #atores = relationship("Atores", backref="atores", lazy="subquery")

    def __repr__(self):
        return f"Livro [titulo={self.titulo}, genero={self.genero}]"
