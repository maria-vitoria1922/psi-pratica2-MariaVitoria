from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Session 

engine = create_engine("sqlite:///biblioteca.db")

class Base(DeclarativeBase):
    pass

def criar_banco():
    import models
    Base.metadata.create_all(bind=engine)


def nova_sessao():
    return Session(bind=engine)



if __name__ == "__main__":
    criar_banco()