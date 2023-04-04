from flask import Flask, jsonify,request,render_template
import pywhatkit
import datetime
import openai
openai.api_key = 'API KEY'
messages = [
    {"role": "system", "content": "You are a kind helpful assistant for assisting people for mental fitnesss and mental health."},
]

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('bot.html')

@app.route('/runbott', methods=['POST'])
def runbott():
    message = request.form['message']
    global fact
    fact=0
    command=message
    if 'play' in command:
        words_to_replace = ["play", "music",'song','play the song','hello','hi']
        for word in words_to_replace:
            command = command.replace(word,"")
        response_message="ok,playing the song for you on youtube"
        pywhatkit.playonyt(command)
        return jsonify(response_message)
        
    elif 'time' in command:
        now = datetime.datetime.now()
        day_name = now.strftime("%A")
        day_num = now.strftime("%d")
        month = now.strftime("%B")
        hour = now.strftime("%H")
        minute = now.strftime("%M")
        response_message = "Today is " + day_name + " " + day_num + " " + month + " and the time is " + hour + ":" + minute

        return jsonify(response_message)
    elif 'quit' in command or "end" in command:
        response_message="Thankyou"
        return jsonify(response_message)
    else:
        message = command
        if message:
            try:
                # Split the message into words and check if it has more than 20 words
                if len(message.split()) > 45:
                    raise ValueError("Input contains more than 45 words. Please try again.")
                messages.append({"role": "user", "content": message})
                chat = openai.Completion.create(
                    model="text-davinci-002", prompt=f"{messages[-1]['content']} Assistant: ", max_tokens=360
                )
            except ValueError as e:
                print(f"Error: {e}")
        reply = chat.choices[0].text
        response_message=f"{reply}"
        messages.append({"role": "assistant", "content": reply}) 
        return jsonify(response_message)
if __name__ == '__main__':
    app.run(debug=True)       