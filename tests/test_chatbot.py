from chatbot import detect_intent, build_response_payload


def test_detect_shipping_intent():
    assert detect_intent("How much is the shipping fee?") == "shipping_fee"


def test_detect_return_intent():
    assert detect_intent("Can I return this product?") == "return_policy"


def test_detect_store_hours_intent():
    assert detect_intent("What time does the store open?") == "store_hours"


def test_detect_product_recommendation_intent():
    assert detect_intent("Can you recommend a product?") == "product_recommendation"


def test_build_response_payload():
    payload = build_response_payload("How much is the shipping fee?")
    assert payload["detectedIntent"] == "shipping_fee"
    assert "Shipping fee" in payload["answer"]
