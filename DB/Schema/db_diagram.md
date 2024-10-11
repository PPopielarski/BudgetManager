```mermaid
classDiagram
    class Tag {
        int id
        int parent_id
        string name
    }
    
    class CasfFlowItem_to_Tag {
        int CashFlowItem_ID
        int Tag_ID
    }
    
    class CasfFlowItem {
        int id
        int CashFlowID
        string Name
        int TotalAmount
        int TotalPrice
        int CasfFlowItem_to_TagID
    }

    class CashFlow {
        int id
        string name
        int PartyID
    }

    class Party {
        int PartyID
        string Name
    }

    Tag "1" --> "*" Tag : "is parent"
    Tag "*" --> "*" CasfFlowItem_to_Tag
    CasfFlowItem_to_Tag "*" <-- "*" CasfFlowItem
    CasfFlowItem "8" <-- "*" CasfFlowItem