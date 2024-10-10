from chatbot import get_response_from_chatbot

if __name__ == "__main__":
    print("Chatbot AI đã sẵn sàng. Nhập 'exit' để thoát.")
    while True:
        user_input = input("Bạn: ")
        if user_input.lower() == "exit":
            break
        bot_reply = get_response_from_chatbot(user_input)
        print("Chatbot:", bot_reply)
