def chatbot():
    print("Hello! I am your friendly customer service bot.")
    print("How can I help you today? (Type 'quit' to end the chat)")

    while True:
        user_input = input("You: ").lower()

       
        if 'hello' in user_input or 'hi' in user_input:
            print("Chatbot: Hello! How can I assist you today?")
        elif 'available' in user_input or 'product' in user_input:
            print("Chatbot: Our products are available for order. What stationary product are you interested in?")
        elif 'Toys' in user_input or 'pen' in user_input:
            print("Chatbot: YES!!! We have it")
        elif 'hours' in user_input or 'time' in user_input:
            print("Chatbot: We are available from Monday to Friday. 9am to 9pm")
        elif 'quit' in user_input:
            print("Chatbot: Thank you for chatting! Have a great day!")
            break
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you ask something else?")

if __name__ == "__main__":
    chatbot()
