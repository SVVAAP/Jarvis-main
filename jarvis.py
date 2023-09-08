import speech_recognition as sr
import openai

from elevenlabslib import *

openai.api_key = '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'

elevenLabsAPIKey = '7319cb8848205aadc27c604c47222390'

r = sr.Recognizer()
mic = sr.Microphone()
user = ElevenLabsUser(elevenLabsAPIKey)

voices = user.get_voices_by_name("Jarvis")
# Check if any voices with the name "Jarvis" were found
if len(voices) > 0:
    # Access the first voice (index 0)
    voice = voices[0]
else:
    # Handle the case where no voices with the name "Jarvis" were found
    print("No voices with the name 'Jarvis' found.")
    # You can choose to exit or take appropriate action here.


conversation = [
        {"role": "system", "content": "Your name is Jarvis and your purpose is to be Adam's AI assistant"},
    ]


while True:
    with mic as source:
        r.adjust_for_ambient_noise(source) #Can set the duration with duration keyword
        print("talk")
        audio = r.listen(source)

    word = r.recognize_google(audio)

    if "draw" in word:
        i = word.find("draw")
        i += 5
        response = openai.Image.create(
            prompt=word[i:],
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        print(word[i:])
        print(image_url)

    else:
        conversation.append({"role": "user", "content": word})

        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
        )

        message = response["choices"][0]["message"]["content"]
        conversation.append({"role": "assistant", "content": message})
        # print(message)
        voice.generate_and_play_audio(message, playInBackground=False)
