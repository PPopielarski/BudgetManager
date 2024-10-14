from sqlalchemy.orm import Session
from Data.ORMModels import User, Transaction, TransactionItem, TransactionParty, Tag
from Data.DataModels import User as UserSchema, Transaction as TransactionSchema, TransactionItem as TransactionItemSchema, Tag as TagSchema

# User CRUD
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserSchema):
    db_user = User(email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, db_user: UserSchema, update_data: dict):
    for key, value in update_data.items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

# Transaction CRUD
def get_transaction(db: Session, transaction_id: int):
    return db.query(Transaction).filter(Transaction.id == transaction_id).first()

def create_transaction(db: Session, transaction: TransactionSchema):
    db_transaction = Transaction(
        title=transaction.title,
        comment=transaction.comment,
        party_ID=transaction.party_ID,
        user_ID=transaction.user_ID
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def update_transaction(db: Session, db_transaction: UserSchema, update_data: dict):
    for key, value in update_data.items():
        setattr(db_transaction, key, value)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

# TransactionItem CRUD
def create_transaction_item(db: Session, item: TransactionItemSchema):
    db_item = TransactionItem(
        transaction_ID=item.transaction_ID,
        total_price=item.total_price,
        quantity=item.quantity,
        unit_ID=item.unit_ID
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Tag CRUD
def get_all_user_tags(db: Session, user_id: int):
    return db.query(Tag).filter(Tag.user_id == user_id).all()

def get_tag(db: Session, tag_id: int):
    return db.query(Tag).filter(Tag.id == tag_id).first()

def create_tag(db: Session, tag: TagSchema):
    db_tag = Tag(name=tag.name, parent_id=tag.parent_id)
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag


