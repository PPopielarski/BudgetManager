from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from Data.PostgresqlHandler import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)

    transactions = relationship("Transaction", back_populates="user")

class TransactionItemUnit(Base):
    __tablename__ = "transaction_item_unit"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    abbreviation = Column(String, unique=True)


class TransactionItem(Base):
    __tablename__ = "transaction_items"
    id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(Integer, ForeignKey("transactions.id"))
    total_price = Column(Integer)
    quantity = Column(Float)
    unit = Column(Integer, ForeignKey("transaction_units.id"))

    transaction = relationship("Transaction", back_populates="items")


class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    comment = Column(String)
    party_id = Column(Integer, ForeignKey("transaction_parties.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="transactions")
    items = relationship("TransactionItem", back_populates="transaction")

class TransactionParty(Base):
    __tablename__ = "transaction_parties"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    parent_id = Column(Integer, ForeignKey("tags.id"))
