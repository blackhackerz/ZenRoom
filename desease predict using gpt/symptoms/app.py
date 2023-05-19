from flask import Flask, request,jsonify
from keras.models import load_model
import numpy as np
import pickle
from flask_cors import CORS
import openai
from helper.openai_api import text_complition
app = Flask(__name__)

CORS(app)
import requests
openai.api_key = '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'

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


    
if __name__ == '__main__':
    app.run()






    
       