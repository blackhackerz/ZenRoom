from zenroom import app
from flask import Flask, render_template, request, redirect, jsonify, flash, url_for, session
#import pyrebase
from datetime import datetime


# Configure Firebase
config = {
    "apiKey": "AIzaSyAvYvSqBoQzCUDK2oloq79JhPJGTw1DIUk",
    "authDomain": "dashboard-50078.firebaseapp.com",
    "databaseURL": "https://dashboard-50078-default-rtdb.firebaseio.com",
    "projectId": "dashboard-50078",
    "storageBucket": "dashboard-50078.appspot.com",
    "messagingSenderId": "475329238769",
    "appId": "1:475329238769:web:7ccdb82a47b7c06ea27b50",
    }

#firebase = pyrebase.initialize_app(config)
#db = firebase.database()

@app.route('/community', methods=["POST", "GET"])
def community():
    # if not session.get('user_id'):
    #     flash("you must be logged in", "error")
    #     return redirect(url_for("login"))
    if request.method == "POST":
        section = request.form['section']
        messages = get_section_messages(section)
        return jsonify(messages=messages)
    else:
        sections = ['discussion_forum', 'creative_corner', 'wellness_tips', 'selfcare_challenges', 'inspiration_corner']
        return render_template('community.html', sections=sections)

def get_section_messages(section):
    #messages = db.child(section).get().val()
    #message_list = list(messages.values()) if messages else []
    message_list="hello"
    return message_list

@app.route('/section', methods=["POST", "GET"])
def section():
    if request.method == "POST":
        section = request.args.get('section')
        username='sharukhali'
        message = request.form['message']
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
 #       db.child(section).push({
   #         "username": username,
  #          "message": message,
 #           "timestamp": timestamp
 #       })
        messages = get_section_messages(section)
        return jsonify(messages=messages)
    else:
        section = request.args.get('section')
        messages = get_section_messages(section)
        return jsonify(messages=messages)
