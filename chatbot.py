def get_response(message):
    """Return a predefined reply for a supported message."""
    message = message.strip().lower()

    if message == "hello":
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "bye":
        return "Goodbye!"
    else:
        return "I don't understand. Try saying hello, asking how I am, or saying bye."


def main():
    print("Chatbot: Hello! Type 'bye' to end the chat.")

    while True:
        message = input("You: ")
        response = get_response(message)
        print(f"Chatbot: {response}")

        if message.strip().lower() == "bye":
            break


if __name__ == "__main__":
    main()