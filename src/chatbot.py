import os
import requests
import json
from dotenv import load_dotenv

# Tải các biến môi trường từ tệp .env
load_dotenv()

# Lấy API key từ biến môi trường
api_key = os.getenv("RAPIDAPI_KEY")  # Đảm bảo biến môi trường được thiết lập
url = "https://chat-gpt26.p.rapidapi.com/completions"  # Cập nhật lại endpoint chính xác

# Kiểm tra xem API key đã được thiết lập hay chưa
if not api_key:
    raise ValueError("API key is missing. Please set the RAPIDAPI_KEY environment variable.")

headers = {
    "Content-Type": "application/json",
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": "chat-gpt26.p.rapidapi.com"
}

def get_response_from_chatbot(user_input):
    payload = {
        "model": "gpt-3.5-turbo",  # Model bạn đang sử dụng
        "messages": [
            {
                "role": "user",
                "content": user_input
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # In toàn bộ phản hồi từ API để giúp gỡ lỗi
    print(response.status_code)
    print(response.text)

    if response.status_code == 200:
        response_data = response.json()
        bot_reply = response_data["choices"][0]["message"]["content"]
        return bot_reply
    else:
        return f"Error: {response.status_code} {response.text}"
