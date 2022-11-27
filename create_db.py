from database import Base,engine
from models import Expenses,Incomes

Base.metadata.create_all(engine)