```mermaid
erDiagram
    USER {
        int UserID PK
        string Email 
        string HashedPassword
    }

    TRANSACTION {
        int Id PK
        string Title
        String Comment
        int PartyID FK
        int UserID FK
    }

    TRANSACTIONPARTY {
        int Id PK
        string Name
    }

    TAG {
        int Id PK
        int ParentId FK
        string Name
        int UserID
    }

    TRANSACTIONITEM {
        int Id PK
        int TransactionID FK
        string Name
        int TotalAmount
        int TotalPrice
    }
    
    TransactionUnits {
        int Id PK
        string Name
        string Abbreviation
    }

    TRANSACTIONITEM_TO_TAG {
        int TransactionItem_ID FK
        int Tag_ID FK
    }

    USER ||--o{ TRANSACTION : "user has many transactions"
    TRANSACTION ||--o{ TRANSACTIONITEM : "1 to many"
    TRANSACTION ||--o{ TRANSACTIONPARTY : "belongs to"
    TRANSACTIONITEM ||--o{ TRANSACTIONITEM_TO_TAG : "mapped to tags"
    TAG ||--o{ TAG : "self-referencing parent"
    TRANSACTIONITEM_TO_TAG ||--o{ TAG : "one item has 0 to many tags"
    USER ||--o{ TAG : "one user creates many tags"
    TransactionUnits ||--o{ TRANSACTIONITEM : "transacion item has one unit"