from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from Data.PostgresqlHandler import get_db
from Data import CRUD
from Data import DataModels
import os
from dotenv import load_dotenv

from passlib.context import CryptContext
import jwt

load_dotenv()
app = FastAPI()

# Ustawienia JWT
SECRET_KEY = os.getenv('JWT_SECRET_KEY')
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Inicjalizacja kontekstu haszowania
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# User endpoints
@app.post("/users/", response_model=DataModels.User)
def create_user(user: DataModels.User, db: Session = Depends(get_db)):
    return CRUD.create_user(db=db, user=user)

@app.get("/users/{user_id}", response_model=DataModels.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = CRUD.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/users/{user_id}/tags", response_model=DataModels.Tag)
def read_users_tags(user_id: int, db: Session = Depends(get_db)):
    return CRUD.get_all_user_tags(db, user_id)

@app.patch("/users/{user_id}", response_model=DataModels.User)
def patch_user(user_id: int, user: DataModels.UserUpdate, db: Session = Depends(get_db)):
    db_user = CRUD.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Zaktualizuj pola użytkownika, jeśli są dostarczone
    update_data = user.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return db_user

# Transaction endpoints
@app.post("/transactions/", response_model=DataModels.Transaction)
def create_transaction(transaction: DataModels.Transaction, db: Session = Depends(get_db)):
    return CRUD.create_transaction(db=db, transaction=transaction)

@app.get("/transactions/{transaction_id}", response_model=DataModels.Transaction)
def read_transaction(transaction_id: int, db: Session = Depends(get_db)):
    db_transaction = CRUD.get_transaction(db, transaction_id=transaction_id)
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return db_transaction

@app.patch("/transactions/{transaction_id}", response_model=DataModels.Transaction)
def patch_transaction(transaction_id: int, transaction: DataModels.TransactionUpdate, db: Session = Depends(get_db)):
    db_transaction = CRUD.get_transaction(db, transaction_id=transaction_id)
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")

    update_data = transaction.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_transaction, key, value)

    db.commit()
    db.refresh(db_transaction)
    return db_transaction

# Tag endpoints
@app.get("/tags/{tag_id}", response_model=DataModels.Tag)
def read_tag(tag_id: int, db: Session = Depends(get_db)):
    return CRUD.get_tag(db, tag_id)

@app.post("/tags/", response_model=DataModels.Tag)
def create_tag(tag: DataModels.Tag, db: Session = Depends(get_db)):
    return CRUD.create_tag(db=db, tag=tag)

@app.patch("/tags/{tag_id}", response_model=DataModels.Transaction)
def patch_tag(tag_id: int, tag: DataModels.TagUpdate, db: Session = Depends(get_db)):
    db_tag = CRUD.get_tag(db, tag_id=tag_id)
    if db_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")

    update_data = tag.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_tag, key, value)

    db.commit()
    db.refresh(db_tag)
    return db_tag

