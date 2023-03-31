from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']='PL8974IBLYGV89JK'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
db=SQLAlchemy(app)

# entries = []
entries = [{"title":"hello",
            "date":"xyz",
            "text":"abc",
            "user":"kash"
            },
            {"title":"hel",
            "date":"xyz",
            "text":"abc",
            "user":"kas"
            },
            {"title":"he44",
            "date":"xyz",
            "text":"abc",
            "user":"kash"
            }]
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add_entry():
    if request.method == "POST":
        title = request.form["title"]
        date = request.form["date"]
        text = request.form["entry"]
        entries.append({"title": title, "date": date, "text": text})
        print(entries)
        return redirect("/add?success=true")
    else:
        success = request.args.get("success")
        return render_template("add.html", success=success)

# @app.route("/view")
# def view_entries():
#     return render_template("view.html", entries=entries)

@app.route("/test")
def view_entries():
    return render_template("test.html", entries=entries)

if __name__ == "__main__":
    app.run(debug=True)
