import logging
import platform
import subprocess

import speech_recognition as sr
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

logging.basicConfig(level=logging.ERROR)

"""
:Authors - Cathal Butler | Morgan Reilly
Currently main class that creates and sets up the bot Nuton
Refs:
https://chatterbot.readthedocs.io/en/stable/index.html
https://github.com/Uberi/speech_recognition#readme
http://www.cstr.ed.ac.uk/projects/festival/
"""

bot = ChatBot(
    'Nuton',  # Bot name
    storage_adapter='chatterbot.storage.SQLStorageAdapter',  # Storage config
    logic_adapters=[
        {
            # Custom logic adapter for weather requests
            'import_path': 'weather_adapter.WeatherAdapter',
            'default_response': 'I am sorry, but I do not understand.'
        },
        {
            # Custom logic adapter for opening applications
            'import_path': 'application_adapter.ApplicationAdapter',
            'default_response': 'I am sorry, but I do not understand.'

        },
        {
            # Custom logic adapter for opening applications
            'import_path': 'helper_adapter.HelperAdapter',
            'default_response': 'I am sorry, but I do not understand.'
        },
        {
            # Imported Time logic adapter
            'import_path': 'chatterbot.logic.TimeLogicAdapter',
            # 'positive': 'time_positive',
            # 'negative': 'time_negative'
        },
        {
            'import_path': "chatterbot.logic.MathematicalEvaluation",
        }
    ],
)

# Train the chat bot with the entire english corpus
# trainer.train('chatterbot.corpus.english')
trainer = ChatterBotCorpusTrainer(bot)  # Train bot on list data
trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations")


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

# First question from bot using text to speech)
speak('Hi I am Nuton, What can I assist you with?')

while True:
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            recognizer_function = getattr(recognizer, 'recognize_google')

            # audio = recognizer.listen(source)
            # result = recognizer_function(audio)
            # print('You said: ', result)
            # msg_statement = Statement(text="open chrome")

            """
            Supported questions so far:
                1. Maths : 'What is four plus four?'
                2. Lunch Application: 'open chrome' - this will do a look up in the applications list(hardcode atm)
                3. Weather: 'what temperature is it in Galway' - Maybe add onto this this
            """
            response = bot.get_response("What can you do")  # Hardcoded text for testing, not using mic

            speak(response)

    except sr.UnknownValueError:
        speak('I am sorry, I could not understand that.')
    except sr.Recognizer as e:
        message = 'My speech recognition service has failed. {0}'
        speak(message.format(e))
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
