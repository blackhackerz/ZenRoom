from flask import render_template, jsonify, request, flash, redirect, url_for
from zenroom import app, db
from zenroom.forms import Diary
from zenroom.structures import Diarydb

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', title='Guide to Mental WellBeing')

global data

@app.route("/exercise")
def exercise():
    return render_template('exercise.html', title='Exercises to improve you mental health')

@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/diary', methods=["POST", "GET"])
def diary():
    forms = Diary()
    if forms.validate_on_submit():
        userdata  =  Diarydb(title= forms.title.data, text= forms.note.data, user="test1")
        db.session.add(userdata)
        db.session.commit()
        print(forms.title.data)
        flash('Success fully inserted your note!!', 'success')
        return redirect(url_for('diary'))
    diary_data = db.session.query(Diarydb).filter(Diarydb.user =="test1").all()
    print(forms.title.data)
    return render_template('diary.html', form=forms, entries=diary_data)