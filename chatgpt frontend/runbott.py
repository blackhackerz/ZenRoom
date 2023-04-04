from flask import Flask, jsonify,request,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('bot.html')


@app.route('/runbott')
def runbot():
    return "HELLO DOSTON"

if __name__ == '__main__':
    app.run(debug=True)
