from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, sessionmaker 

from database import Base

sessao_base = sessionmaker(engine)

class Autor(Base):
    __tablename__ = "Autor"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] 
    pais: Mapped[str]
   
   livros: Mapped[List["Livro"]] = relationship("Livro", back_populates="autor")

class Livro(Base):
    __tablename__ = "Livro"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] 
    ano: Mapped[str]
    autor_id: Mapped[int] = mapped_column(ForeignKey('autores.id'))
    autor: Mapped["Autor"] = relationship("Autor", back_populates="livros")

