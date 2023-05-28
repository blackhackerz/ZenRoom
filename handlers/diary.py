from zenroom import app
from flask import flash, redirect, url_for, render_template, session
import datetime
#import pyrebase
from zenroom.forms import Diary
@app.route('/diary', methods=["POST", "GET"])
def diary():
    # if not session.get("name"):
    #     flash("you must be logged in", "error")
    #     return redirect(url_for("login"))
    config = {
    "apiKey": "AIzaSyAvYvSqBoQzCUDK2oloq79JhPJGTw1DIUk",
    "authDomain": "dashboard-50078.firebaseapp.com",
    "databaseURL": "https://dashboard-50078-default-rtdb.firebaseio.com",
    "projectId": "dashboard-50078",
    "storageBucket": "dashboard-50078.appspot.com",
    "messagingSenderId": "475329238769",
    "appId": "1:475329238769:web:7ccdb82a47b7c06ea27b50",
    }

#    firebase = pyrebase.initialize_app(config)
#    db = firebase.database()
    username = "shahrukh"
    forms = Diary()
    if forms.validate_on_submit():
        title = forms.title.data
        note = forms.note.data
          # Replace with the actual username
        entry_key = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Store the entry in Firebase Realtime Database
 #       db.child("Diary").child(username).push({"title": title, "note": note, "date": date})

        flash('Successfully inserted your note!', 'success')
        return redirect(url_for('diary'))

    # Retrieve diary entries from Firebase
 #   diary_data = db.child("Diary").child(username).get().val()
    diary_data='hello'
    # Convert the diary_data dictionary into a list of entries
    entries = []
    if diary_data:
        for entry_key, entry_value in diary_data.items():
            if "date" in entry_value:
                entry = {"key": entry_key, "title": entry_value["title"], "note": entry_value["note"],
                         "date": entry_value["date"]}
                entries.append(entry)

    return render_template('diary.html', form=forms, entries=entries)
