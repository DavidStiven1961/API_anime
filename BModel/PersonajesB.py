from sqlalchemy.ext.declarative import declarative_base
from  sqlalchemy import Column, Integer, String

Base = declarative_base()

class Character(Base):

    __tablename__ = 'Characters'

    id = Column(Integer(), primary_key=True, autoincrement=True, unique=True)
    anime = Column(String(20))
    nombre= Column(String(20))
    nacimiento = Column(String(20))
    edad= Column(Integer())
    altura= Column(String(20))
    tipo_sangre= Column(String(20))