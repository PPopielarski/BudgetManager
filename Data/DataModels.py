from pydantic import BaseModel, EmailStr
from typing import Optional, List, Dict

class _UserBase(BaseModel):
    id: int

    class Config:
        from_attributes = True

class User(_UserBase):
    name: str
    email: EmailStr

class UserUpdate(_UserBase):
    name: Optional[str]
    email: Optional[EmailStr]

class _TransactionItemBase(BaseModel):
    id: int

    class Config:
        from_attributes = True

class TransactionItem(_TransactionItemBase):
    transaction_ID: int
    total_price: int #one unit is 0.01 of currency (e.g. 1 eurocent, 1 grosz etc.)
    quantity: float
    unit_ID: int

class TransactionItemUpdate(_TransactionItemBase):
    transaction_ID: Optional[int]
    total_price: Optional[int] # one unit is 0.01 of currency (e.g. 1 eurocent, 1 grosz etc.)
    quantity: Optional[float]
    unit_ID: Optional[int]

class _TransactionBase(BaseModel):
    id: int

    class Config:
        from_attributes = True

class Transaction(_TransactionBase):
    title: str
    comment: Optional[str]
    party_ID: Optional[int]
    user_ID: int
    items: List[TransactionItem]

class TransactionUpdate(_TransactionBase):
    title: Optional[str]
    comment: Optional[str]
    party_ID: Optional[int]
    items: Optional[List[TransactionItem]]

class _TransactionPartyBase(BaseModel):
    id: int

    class Config:
        from_attributes = True

class TransactionParty(_TransactionPartyBase):
    name: str

class TransactionPartyUpdate(_TransactionPartyBase):
    name: Optional[str]

class _TagBase(BaseModel):
    id: int
    user_id: int

    class Config:
        from_attributes = True

class Tag(_TagBase):
    name: str
    parent_id: Optional[int]

class TagUpdate(_TagBase):
    name: Optional[str]
    parent_id: Optional[int]

class TagCollection(BaseModel):
    user_id: User
    tags: Dict[Tag, List[Tag]]