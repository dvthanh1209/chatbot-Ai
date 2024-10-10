import os
import requests
import json
from dotenv import load_dotenv

# Tải các biến môi trường từ tệp .env
load_dotenv()

# Lấy API key từ biến môi trường
api_key = os.getenv("RAPIDAPI_KEY")
url = "https://chat-gpt26.p.rapidapi.com/"


headers = {
    "Content-Type": "application/json",
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": "chat-gpt26.p.rapidapi.com"
}

def get_response_from_chatbot(user_input):
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": user_input
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        response_data = response.json()
        bot_reply = response_data["choices"][0]["message"]["content"]
        return bot_reply
    else:
        return f"Error: {response.status_code}, {response.text}"
