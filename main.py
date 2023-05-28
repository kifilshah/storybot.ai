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
                "content": "you are a storyteller who will create a story based on the plot points given to you. a plot with one sentence should have a story with 2 sentences. after that, for every additional sentence in the plot, you should increase size of the story by 20%. Your output should include only the story. keep sentences short" 
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
