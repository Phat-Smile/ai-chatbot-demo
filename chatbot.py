import json
from pathlib import Path
from typing import Dict, List


FAQItem = Dict[str, str]


def load_faq_data(file_path: str = "sample_faq.json") -> List[FAQItem]:
    """Load FAQ data from a JSON file."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"FAQ file not found: {file_path}")

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("FAQ data must be a list of objects.")

    return data


def normalize_message(user_message: str) -> str:
    """Normalize user message for simple intent detection."""
    return user_message.strip().lower()


def detect_intent(user_message: str) -> str:
    """Detect a simple intent from a customer message."""
    message = normalize_message(user_message)

    if any(keyword in message for keyword in ["shipping", "delivery", "ship", "deliver"]):
        return "shipping_fee"

    if any(keyword in message for keyword in ["return", "refund", "exchange"]):
        return "return_policy"

    if any(keyword in message for keyword in ["open", "hour", "time", "close"]):
        return "store_hours"

    if any(keyword in message for keyword in ["recommend", "suggest", "suitable", "need a product"]):
        return "product_recommendation"

    if any(keyword in message for keyword in ["order", "tracking", "status"]):
        return "order_support"

    if any(keyword in message for keyword in ["product", "price", "information", "info"]):
        return "product_information"

    return "unknown"


def find_answer(intent: str, faq_data: List[FAQItem]) -> str:
    """Find an FAQ answer by intent."""
    for item in faq_data:
        if item.get("intent") == intent:
            return item.get("answer", "")

    return (
        "I am not sure about that yet. Could you provide more details "
        "so I can help you better?"
    )


def build_product_recommendation_reply() -> str:
    """Return a starter reply for product recommendation flow."""
    return (
        "I can help recommend a product. Please share your product need, "
        "budget, and preferred category so I can suggest a suitable option."
    )


def chatbot_reply(user_message: str, faq_file_path: str = "sample_faq.json") -> str:
    """Generate a chatbot reply for a user message."""
    faq_data = load_faq_data(faq_file_path)
    intent = detect_intent(user_message)

    if intent == "product_recommendation":
        return build_product_recommendation_reply()

    return find_answer(intent, faq_data)


def build_response_payload(user_message: str, faq_file_path: str = "sample_faq.json") -> Dict[str, str]:
    """Return a structured chatbot response payload."""
    intent = detect_intent(user_message)
    answer = chatbot_reply(user_message, faq_file_path)

    return {
        "userMessage": user_message,
        "detectedIntent": intent,
        "answer": answer,
    }
