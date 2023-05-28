from flask import Flask, request,jsonify
from keras.models import load_model
import numpy as np
import pickle
from flask_cors import CORS
import requests

wikipedia = Flask(__name__)
CORS(wikipedia)

@wikipedia.route('/wiki',methods=['POST'])
def wiki():
    endpoint = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",#"prop": "extracts" specifies that the response should include the text extracts from the page(s) requested.
        "exintro": True,#
        "explaintext": True,
    }

    
    # Defining the disease that we  want to search for
    #disease =request.get_json()['disease_name']
    disease = request.json['disease_name']

    # Adding the disease name to the query parameters
    params["titles"] = disease

    # Sending the request and get the response in  json form (we re not converting it to json)
    response1 = requests.get(endpoint, params=params).json()
     
    # Check if the page exists in the wikipedia API
    if '-1' in response1['query']['pages']:
        additional_response = {"additional": "Additional data about this disease cannot be retrieved."}
        return jsonify(additional_response), 404

    # Extracting the text of the first page (the only page available)
    pages = response1["query"]["pages"]
    page_id = next(iter(pages))
    if "extract" not in pages[page_id]:
        additional_response = {"additional": "Additional data about this disease cannot be retrieved."}
        return jsonify(additional_response), 404
    text = pages[page_id]["extract"]

    # Extracting the text of the first page(the only page available)
    pages = response1["query"]["pages"]
    page_id = next(iter(pages))#we are using next(iter()) because we dont know which page number will come 
    text = pages[page_id]["extract"]
    description = []
    for line in text.split("."):
        if line.strip():
            description.append(line.strip())

    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "titles": disease,
        "exsectionformat": "wiki",
        "explaintext": 1,
        "exsectiontree": 1
    }

    response2 = requests.get(endpoint, params=params)

    # Check if the request was successful
    if response2.status_code == 200:
        pages = response2.json()["query"]["pages"]
        page = list(pages.values())[0]
        extract = page["extract"]
        start_index = extract.find("Treatment")
        end_index = extract.find("Prevention")
        treatment_first_two_lines = extract[start_index:end_index].split('.')[:2]
    
    #Combining the output
    additional = description + treatment_first_two_lines
    additional_response = {"additional": additional}
    return jsonify(additional_response)

if __name__ == '__main__':
    wikipedia.run(port=5003) 

# from flask import Flask, request,jsonify
# from keras.models import load_model
# import numpy as np
# from flask_cors import CORS
# import requests

# wikipedia = Flask(__name__)
# CORS(wikipedia)

# @wikipedia.route('/chatbot',methods=['POST'])
# def wiki():
#     endpoint = "https://en.wikipedia.org/w/api.php"
#     params = {
#         "action": "query",
#         "format": "json",
#         "prop": "extracts",#"prop": "extracts" specifies that the response should include the text extracts from the page(s) requested.
#         "exintro": True,#Tells that the responce should include intro only
#         "explaintext": True,
#     }

#     # Defining the disease that we  want to search for
#     response=request.get_json()
#     disease=response['queryResult']['parameters']['Disease-name']

#     # Adding the disease name to the query parameters
#     params["titles"] = disease

#     # Sending the request and get the response in  json form (we re not converting it to json)
#     response1 = requests.get(endpoint, params=params).json()

#     # Check if the page exists in the wikipedia API
#     if '-1' in response1['query']['pages']:
#         additional_response = {"additional": "Additional data about this disease cannot be retrieved."}
#         return jsonify(additional_response), 404
    
#     # Extracting the text of the first page (the only page available)
#     pages = response1["query"]["pages"]
#     page_id = next(iter(pages))
#     if "extract" not in pages[page_id]:
#         additional_response = {"additional": "Additional data about this disease cannot be retrieved."}
#         return jsonify(additional_response), 404
#     text = pages[page_id]["extract"]
#     description = []
#     for line in text.split("."):
#         if line.strip():
#             description.append(line.strip())
    
#     # additional_response = {"additional": description}
#     # return jsonify(additional_response)

#     #+++++++++++++1st response completed++++++++++++++++++++++++++++++
#     params = {
#         "action": "query",
#         "format": "json",
#         "prop": "extracts",
#         "titles": disease,
#         "exsectionformat": "wiki",
#         "explaintext": 1,
#         "exsectiontree": 1
#     }

#     response2 = requests.get(endpoint, params=params)

#     if response2.status_code == 200:
#         pages = response2.json()["query"]["pages"]
#         page = list(pages.values())[0]
#         extract = page["extract"]
#         start_index = extract.find("Treatment")
#         end_index = extract.find("Prevention")
#         treatment_first_two_lines = extract[start_index:end_index].split('.')[:2]

#      #Combining the output
#     additional = description + treatment_first_two_lines
#     additional_response = {"1st": additional}
#     return jsonify(additional_response)
    

# if __name__ == '__main__':
#     wikipedia.run(port=5007)