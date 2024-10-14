import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("RAPIDAPI_KEY")

# Check if the API key is provided
if not api_key:
    raise ValueError("API key is missing. Please set the RAPIDAPI_KEY environment variable.")

# Set the API URL
url = "https://chat-gpt26.p.rapidapi.com/chat/completions"

# Headers required for the API request
headers = {
    "x-rapidapi-key": api_key,
    "x-rapidapi-host": "chat-gpt26.p.rapidapi.com",
    "Content-Type": "application/json"
}

# Function to get a response from the chatbot API
def get_response_from_chatbot(user_input):
    # Payload containing user input
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": user_input  # User's input
            }
        ]
    }

    # Send the request to the API
    print(f"Sending request to: {url}")
    response = requests.post(url, json=payload, headers=headers)

    # Log the status code and response for debugging
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

    # If the request was successful, return the chatbot's reply
    if response.status_code == 200:
        response_data = response.json()
        bot_reply = response_data["choices"][0]["message"]["content"]
        return bot_reply
    else:
        return f"Error: {response.status_code} {response.text}"
