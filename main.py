from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import Optional,List
from database import SessionLocal
from models import Incomes,Expenses
import models

app = FastAPI()

db = SessionLocal()

class Expenses(BaseModel):
    id : int
    name : str
    price : int
    jenis : str

    class Config:
        orm_mode = True

class Incomes(BaseModel):
    id : int
    name : str
    price : int
    jenis : str

    class Config:
        orm_mode = True

# Function for Expenses
@app.get('/')
def index():
    return {"message":"Hello World"}

@app.get('/expenses',response_model = List[Expenses], status_code=status.HTTP_200_OK)
def get_all_expenses():
    expenses = db.query(Expenses).all()

    return expenses

@app.get('/expense/{expense_id}', response_model = Expenses, status_code=status.HTTP_200_OK)
def get_an_expense(expense_id:int):
    expense = db.query(Expenses).filter(Expenses.id == expense_id).first()

    return expense

@app.post('/expenses',response_model=Expenses,
            status_code=status.HTTP_201_CREATED)
def create_an_expense(expense : Expenses):
    db_expenses = db.query(Expenses).filter(Expenses.id == expense.id).first()

    if db_expenses is not None:
        raise HTTPException(status_code=400,detail="Item already exist")

    new_expense = Expenses(
                    name = expense.name,
                    jenis = expense.jenis,
                    price = expense.price
                )

    db.add(new_expense)
    db.commit()

    return new_expense

@app.put('/expence/{expence_id}',response_model=Expenses,status_code=status.HTTP_200_OK)
def update_an_expense(expence_id:int,expense:Expenses):
    expense_to_update = db.query(Expenses).filter(Expenses.id==expence_id).first()
    expense_to_update.name = expense.name
    expense_to_update.jenis = expense.jenis
    expense_to_update.price = expense.price

    db.commit()

    return expense_to_update

@app.delete('/expense/{expense_id}')
def delete_an_expense(expense_id:int):
    expense_to_delete = db.query(Expenses).filter(Expenses.id == expense_id).first()

    if expense_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Item not Found")

    db.delete(expense_to_delete)
    db.commit()

    return expense_to_delete

# Function for Incomes

@app.get('/incomes',response_model = List[Incomes], status_code=status.HTTP_200_OK)
def get_all_incomes():
    incomes = db.query(Incomes).all()

    return incomes

@app.get('/income/{incomes_id}', response_model = Incomes, status_code=status.HTTP_200_OK)
def get_an_income(income_id:int):
    income = db.query(Incomes).filter(Incomes.id == income_id).first()

    return income

@app.post('/income',response_model=Incomes,
            status_code=status.HTTP_201_CREATED)
def create_an_income(income : Incomes):
    db_income = db.query(Incomes).filter(Incomes.id == income.id).first()

    if db_income is not None:
        raise HTTPException(status_code=400,detail="Item already exist")

    new_income = Incomes(
                    name = income.name,
                    jenis = income.jenis,
                    price = income.price
                )

    db.add(new_income)
    db.commit()

    return new_income

@app.put('/income/{income_id}',response_model=Incomes,status_code=status.HTTP_200_OK)
def update_an_income(income_id : int ,income : Incomes):
    income_to_update = db.query(Incomes).filter(Incomes.id == income_id).first()
    income_to_update.name = income.name
    income_to_update.price = income.price
    income_to_update.description = income.description

    db.commit()

    return income_to_update

@app.delete('/income/{income_id}')
def delete_an_income(income_id:int):
    income_to_delete = db.query(Incomes).filter(Incomes.id == income_id).first()

    if income_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Item not Found")

    db.delete(income_to_delete)
    db.commit()

    return income_to_delete
