from database import Base
from sqlalchemy import String,Integer,Column,Text

class Expenses(Base):
    __tablename__="Expenses"
    id = Column(Integer, primary_key = True)
    name = Column(Text)
    jenis = Column(Text)
    price = Column(Integer, nullable = False)

class Incomes(Base):
    __tablename__="Incomes"
    id = Column(Integer, primary_key = True)
    name = Column(Text)
    jenis = Column(Text)
    price = Column(Integer, nullable = False)