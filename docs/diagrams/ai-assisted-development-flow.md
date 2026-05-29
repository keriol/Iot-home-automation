# AI Assisted Development Flow

```mermaid
flowchart LR

    User[Project Owner]
    Model[Project Model]
    AI[ChatGPT]
    Design[Architecture Decisions]
    Code[Implementation]
    Validation[Testing and Validation]
    Docs[Documentation]

    User --> AI
    AI --> Model
    Model --> Design
    Design --> Code
    Code --> Validation
    Validation --> Docs
    Docs --> Model
```
