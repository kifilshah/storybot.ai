from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def chat():
    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'POST':
        prompt = request.form['prompt']
        response = {'choices': [{'message': {'content': 'This is the response'}}]}
        return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)