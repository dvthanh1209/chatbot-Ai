from flask import Flask, render_template, request
from src.chatbot import get_response_from_chatbot  # Đảm bảo import đúng đường dẫn

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message']
    bot_reply = get_response_from_chatbot(user_input)
    return bot_reply

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)