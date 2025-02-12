```mermaid
---
title: Implementation
---
classDiagram
    Payment <|-- ProductONe
    Payment <|-- ProductTwo

    namespace Payment_implementation{
        class Payment{
            <<interface>>
            +subscribe()
            +unsubscribe()
            +addCreditCard
        }
        class ProductONe{
            +String name
            +bool onSale
        }
        class ProductTwo{
            +String name
            +bool onSale
        }
    }
```