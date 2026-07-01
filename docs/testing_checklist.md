# Testing Checklist

| Test Case | Input | Expected Intent | Expected Result |
|---|---|---|---|
| Shipping fee | How much is the shipping fee? | `shipping_fee` | Bot returns shipping-related answer |
| Return policy | Can I return this product? | `return_policy` | Bot returns return policy answer |
| Store hours | What time does the store open? | `store_hours` | Bot returns store hours answer |
| Product recommendation | Can you recommend a product? | `product_recommendation` | Bot asks for product need, budget, and category |
| Unknown question | Can you help me? | `unknown` | Bot asks for clarification |
| Exit command | exit | N/A | Program stops |
