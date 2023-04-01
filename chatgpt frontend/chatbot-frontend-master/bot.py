from flask import Flask, render_template, request
import pywhatkit
import datetime
import openai
import json
from flask import jsonify

app = Flask(__name__)

openai.api_key = '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'

messages = [
    {"role": "system", "content": "You are a kind helpful assistant for assisting people for mental fitnesss and mental health."},
]



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def handle_form_submission():
    command = request.form['user_input']
    messages.append({"role": "user", "content": command})
    reply = ''

    if 'play' in command:
        words_to_replace = ["play", "music",'song','play the song','hello','hi']
        for word in words_to_replace:
            command = command.replace(word,"")
        reply = "ok, playing the song for you on YouTube"
        pywhatkit.playonyt(command)

    elif 'time' in command:
        now = datetime.datetime.now()
        day_name = now.strftime("%A")
        day_num = now.strftime("%d")
        month = now.strftime("%B")
        hour = now.strftime("%H")
        minute = now.strftime("%M")
        reply = f"Today is {day_name} {day_num} {month} and the time is {hour}:{minute}"

    elif 'quit' in command or 'end' in command:
        reply = "Thank you. Goodbye!"
        messages.append({"role": "assistant", "content": reply})
        return render_template('index.html', messages=messages)

    else:
        try:
            if len(command.split()) > 45:
                raise ValueError("Input contains more than 45 words. Please try again.")
            chat = openai.Completion.create(model="text-davinci-002", prompt=f"{messages[-1]['content']} Assistant: ", max_tokens=360)
            reply = chat.choices[0].text
        except ValueError as e:
            reply = f"Error: {e}"

    messages.append({"role": "assistant", "content": reply})
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)



