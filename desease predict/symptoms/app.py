from flask import Flask, request,jsonify
from keras.models import load_model
import numpy as np
import pickle
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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
    response_data = {"disease": disease}
    print(disease)
    return jsonify(response_data)


    
if __name__ == '__main__':
    app.run(port=5001)
