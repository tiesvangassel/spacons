from flask import Flask, render_template_string, jsonify
import random
import string
Flask
gunicorn


app = Flask(bimbambaap)

sentences = [
    "Iets brandbaars",
    "Voetbalspelers",
    "Iets wat in je zak past",
    "Iets wat je kan zien",
    "Persoon uit Bussum"
]

letter_shown = False
random_letter = None

@app.route('/')
def index():
    global letter_shown, random_letter
    return render_template_string('''
        <html>
        <head>
            <title>Random Generator</title>
            <style>
                body {background-color: black; color: white; text-align: center; font-family: Arial, sans-serif;}
                #start-button {border-radius: 50%; background-color: green; color: white; padding: 20px; font-size: 20px; border: none; cursor: pointer;}
                #result {margin-top: 20px; font-size: 24px;}
            </style>
        </head>
        <body>
            <h1>Random Generator Spel</h1>
            <button id="start-button" onclick="getResult()">Start</button>
            <div id="result"></div>

            <script>
                function getResult() {
                    fetch('/get_result')
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('result').innerText = data.result;
                    });
                }
            </script>
        </body>
        </html>
    ''')

@app.route('/get_result')
def get_result():
    global letter_shown, random_letter
    if not letter_shown:
        random_letter = random.choice(string.ascii_uppercase)
        letter_shown = True
        return jsonify(result=f"Begin met de letter: {random_letter}")
    else:
        random_sentence = random.choice(sentences)
        return jsonify(result=random_sentence)

if __name__ == '__main__':
    app.run(debug=True)
