from flask import Flask, jsonify,request
import pywhatkit
import datetime
import openai

openai.api_key = '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'

messages = [
    {"role": "system", "content": "You are a kind helpful assistant for assisting people for mental fitnesss and mental health."},
]

app = Flask(__name__)

@app.route('/runbot')
def runbot():
    global fact
    fact = 0
    command = take_command()
    if 'play' in command:
        words_to_replace = ["play", "music",'song','play the song','hello','hi']
        for word in words_to_replace:
            command = command.replace(word,"")
        output = {"result": "ok,playing the song for you on youtube"}
        pywhatkit.playonyt(command)
    elif 'time' in command:
        now = datetime.datetime.now()
        day_name = now.strftime("%A")
        day_num = now.strftime("%d")
        month = now.strftime("%B")
        hour = now.strftime("%H")
        minute = now.strftime("%M")

        output = {"result": f"Today is {day_name} {day_num} {month} and the time is {hour}:{minute}"}
    elif 'quit' in command or "end" in command:
        output = {"result": "thankyou"}
        fact = 1
        return jsonify(output)
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
                output = {"error": str(e)}
                return jsonify(output)
        reply = chat.choices[0].text
        output = {"result": reply}
        messages.append({"role": "assistant", "content": reply})
        
    return jsonify(output)
    
@app.route('/runbot')
def take_command():
    a = input("USER : ")
    print("MEDI-BOT : ", end="")
    return a

if __name__ == '__main__':
    app.run(debug=True)
