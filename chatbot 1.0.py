import pywhatkit
import datetime
import openai
openai.api_key = 'API-KEY'
messages = [
    {"role": "system", "content": "You are a kind helpful assistant for assisting people for mental fitnesss and mental health."},
]

print("MEDI-BOT : HIIII   Welcome to our mental health checkup app , I'm Sofia, your personal health assistant to guide you on your wellness journey. How can I assist you today?")

def take_command():
    a=input("USER : ")
    print("MEDI-BOT : ",end="")
    return a

def runbot():
    global fact
    fact=0
    command=take_command()
    if 'play' in command:
        words_to_replace = ["play", "music",'song','play the song','hello','hi']
        for word in words_to_replace:
            command = command.replace(word,"")
        print("ok,playing the song for you on youtube")
        pywhatkit.playonyt(command)
    elif 'time' in command:
        now = datetime.datetime.now()
        day_name = now.strftime("%A")
        day_num = now.strftime("%d")
        month = now.strftime("%B")
        hour = now.strftime("%H")
        minute = now.strftime("%M")

        print("Today is "+ day_name+" "+ day_num+" "+ month + " and the time is "+  hour +  " : "+ minute)
    elif 'quit' in command or "end" in command:
        print("thankyou")
        fact=1
        return
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
        print(f"{reply}")
        messages.append({"role": "assistant", "content": reply})        

while True:
    runbot()
    if(fact==1):
        break
