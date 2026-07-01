# Chatbot Conversation Flow

```mermaid
flowchart TD
    A[Customer message] --> B[Preprocess input]
    B --> C[Detect intent]
    C --> D{Intent}
    D -->|FAQ| E[Find matching FAQ]
    D -->|Product recommendation| F[Ask preference questions]
    D -->|Unknown| G[Fallback response]
    E --> H[Generate final answer]
    F --> I[Recommend suitable product]
    G --> J[Ask user to clarify]
    H --> K[Return chatbot response]
    I --> K
    J --> K
```

## Flow Explanation

1. The customer sends a message.
2. The chatbot normalizes the message.
3. The chatbot detects a simple intent.
4. The chatbot selects the correct FAQ answer or recommendation flow.
5. The chatbot returns a clear response.
