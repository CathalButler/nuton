import platform
import subprocess
import speech_recognition as sr
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# import logging
#
# logging.basicConfig(level=logging.INFO)

"""
:Authors - Cathal Butler | Morgan Reilly
Currently main class that creates and sets up the bot Nuton
Refs:
https://chatterbot.readthedocs.io/en/stable/index.html
https://github.com/Uberi/speech_recognition#readme
http://www.cstr.ed.ac.uk/projects/festival/
"""

bot = ChatBot(
    'Nuton',
    logic_adapters=[
        {
            'import_path': 'application_adapter.ApplicationAdapter'
        }
    ],
)

# Train the chat bot with the entire english corpus
# trainer.train('chatterbot.corpus.english')
trainer = ListTrainer(bot)  # Train bot on list data
trainer.train(['open'])


def speak(text):
    """
    Function that uses festival, a text to speech package to replay to the user
    :param text: text you can to be spoke
    """
    if platform.system() == 'Darwin':
        cmd = ['say', str(text)]
        subprocess.call(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    elif platform.system() == "Windows":
        print('Not supported right now')
    else:
        subprocess.run(
            'echo "' + str(text) + '" | festival --tts',
            shell=True)


# Instances of speech Recognition
recognizer = sr.Recognizer()

# First question from bot using text to speech
speak('What would you like to do?')

while True:
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            recognizer_function = getattr(recognizer, 'recognize_google')

            audio = recognizer.listen(source)
            result = recognizer_function(audio)
            print('You said: ', result)
            responce = bot.get_response(result)

            speak(responce)

    except sr.UnknownValueError:
        speak('I am sorry, I could not understand that.')
    except sr.Recognizer as e:
        message = 'My speech recognition service has failed. {0}'
        speak(message.format(e))
    except (KeyboardInterrupt, EOFError, SystemExit):
        print('end')
        break
