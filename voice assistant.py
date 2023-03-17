import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import openai
openai.api_key = 'API-KEY'
messages = [
    {"role": "system", "content": "You are a kind helpful assistant for assisting people for mental fitnesss and mental health."},
]
listener = sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 130)
engine.say("")
engine.say("   HIIII  ")
# Welcome to our mental health checkup app , I'm Sofia, your personal health assistant to guide you on your wellness journey. How can I assist you today?
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

# Get a list of all available audio devices
audio_devices = sr.Microphone.list_microphone_names()


def take_command():
    # Initialize the recognizer instance
    listener = sr.Recognizer()

    # Set the audio device index to use the default microphone
    device_index = sr.Microphone(device_index=None).device_index

    with sr.Microphone(device_index=device_index) as source:
        print("listening...")
        listener.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        voice = listener.listen(source)
        try:
            # Transcribe the audio to text
            result = listener.recognize_google(voice, show_all=True)
            transcript = result['alternative'][0]['transcript']
            print("Final sentence:", transcript)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            transcript = "quit"
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            transcript = "quit"
        except:
            return "quit"
    return transcript

def runbot():
    command=take_command()
    if 'play' in command:
        words_to_replace = ["play", "music",'song','play the song','hello','hi']
        for word in words_to_replace:
            command = command.replace(word,"")
        talk(f"ok,playing the song for you on youtube")
        pywhatkit.playonyt(command)
    elif 'time' in command:
        now = datetime.datetime.now()
        day_name = now.strftime("%A")
        day_num = now.strftime("%d")
        month = now.strftime("%B")
        hour = now.strftime("%H")
        minute = now.strftime("%M")

        talk("Today is"+ day_name+ day_num+ month + "and the time is"+  hour+  ":"+ minute)
    elif 'quit' in command:
        print("so sorry,pardon")
    else:
        message = command
        if message:
            try:
                # Split the message into words and check if it has more than 20 words
                if len(message.split()) > 45:
                    raise ValueError("Input contains more than 45 words. Please try again.")
                messages.append({"role": "user", "content": message})
                chat = openai.Completion.create(
                    model="text-davinci-002", prompt=f"{messages[-1]['content']} Assistant: ", max_tokens=220
                )
            except ValueError as e:
                print(f"Error: {e}")
        reply = chat.choices[0].text
        print(f"HEALTH-BOT: {reply}")
        talk(reply)
        messages.append({"role": "assistant", "content": reply})        

while True:
    runbot()
    
