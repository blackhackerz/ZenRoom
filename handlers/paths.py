from flask import render_template, flash, redirect, url_for,jsonify,session,request
from zenroom import app
import numpy as np
import openai
from keras.models import load_model
import pickle

@app.route("/exercise")
def exercise():
    # if not session.get("user_id"):
    #     flash("you must be logged in", "error")
    #     return redirect(url_for("login"))
    return render_template('exercise.html', title='Exercises to improve you mental health')


@app.route('/therapy')

def therapy():
    # if not session.get("user_id"):
    #     flash("you must be logged in", "error")
    #     return redirect(url_for("login"))
    return render_template('bot.html')

@app.route('/map')

def map():
    # if not session.get("user_id"):
    #     flash("you must be logged in", "error")
    #     return redirect(url_for("login"))
    return render_template('map.html')

@app.route('/user_dashboard')
def user_dashboard():
    # if not session.get("user_id"):
    #     flash("you must be logged in", "error")
    #     return redirect(url_for("login"))
    return render_template('user_dashboard.html')

@app.route('/diet')
def diet():
    # if not session.get("user_id"):
    #     flash("you must be logged in", "error")
    #     return redirect(url_for("login"))
    return render_template('diet.html')

# Load the Keras model
model = load_model('best_symptom_model.h5')
diseases_names=pickle.load(open('diseases_names.pkl','rb'))

@app.route('/predict1', methods=['POST'])
def predict():
    print(request.get_json())
    symptoms = request.get_json()['symptoms']
    symp = np.zeros(489, dtype=int)
    for i in symptoms:
        symp[i]=1
    symptoms_arr = symp.reshape(1, -1)
    probabilities = model.predict(symptoms_arr)
    predicted_class = np.argmax(probabilities, axis=-1)
    predicted_class = predicted_class.reshape(-1, 1)
    disease=diseases_names[predicted_class[0][0]]
    #predicted_class=predicted_class.tolist()
    
    print(disease)
    message="you are a helpful doctor to help the patients in their mental fitness journey, tell the treatments, causes of the desease : "+ disease + " along with safety measures , also tell some jokes to relax the user and tell the user not to worry and just be happy and relax"
    if message:
        try:
            if len(message.split()) > 80:
                raise ValueError("Input contains more than 45 words. Please try again.")
            chat = openai.Completion.create(engine="text-davinci-003",prompt=message,max_tokens=3896,temperature=0.2)
        except ValueError as e:
            print(f"Error: {e}")
    reply = chat.choices[0].text
    response_message=f"{reply}"
    print(response_message) 
    response_data = {"disease": disease, "message": response_message}
    return jsonify(response_data)
@app.route('/serious', methods=['POST',"GET"])
def serious():
    return render_template("serious.html")

@app.route('/comedy', methods=['POST',"GET"])
def comedy():
    return render_template("comedy.html")
