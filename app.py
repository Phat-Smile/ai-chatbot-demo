from chatbot import build_response_payload


def main() -> None:
    print("AI Chatbot Demo")
    print("Type 'exit' to stop.")
    print()

    while True:
        message = input("User: ").strip()

        if message.lower() == "exit":
            print("Bot: Goodbye.")
            break

        if not message:
            print("Bot: Please enter a question so I can help you.")
            continue

        payload = build_response_payload(message)
        print(f"Intent: {payload['detectedIntent']}")
        print(f"Bot: {payload['answer']}")
        print()


if __name__ == "__main__":
    main()
