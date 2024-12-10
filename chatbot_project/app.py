# app.py

from flask import Flask, render_template, request
from chatbot import get_response
import re

app = Flask(__name__)

def format_response(response_text):
    
    sentences = re.split(r'(?<=[.!?]) +', response_text.strip())
    formatted_text = "<br>".join(sentences)
    return formatted_text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
    user_input = request.form['user_input']
    raw_response = get_response(user_input)
    formatted_response = format_response(raw_response)
    return formatted_response

if __name__ == '__main__':
    app.run(debug=True)
