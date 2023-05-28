# from flask import Flask, render_template, request, jsonify

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/ask', methods=['POST'])
# def ask():
#     message = request.form['message']
#     # Instead of sending a request to OpenAI API, we return a hardcoded response
#     response = 'this is the response'
#     return jsonify({'response' : response})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080)

from flask import Flask, render_template, request, jsonify
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY") #ensure you have this in your replit secrets

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    message = request.form['message']
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )
    response = chat['choices'][0]['message']['content']
    return jsonify({'response' : response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
