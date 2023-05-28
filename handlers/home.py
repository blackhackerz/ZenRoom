from zenroom import app
from flask import render_template

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', title='Guide to Mental WellBeing')