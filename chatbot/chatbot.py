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
Nuton Listens in a loop for a request from the user
Refs:
https://chatterbot.readthedocs.io/en/stable/index.html
https://github.com/Uberi/speech_recognition#readme
http://www.cstr.ed.ac.uk/projects/festival/
"""

time_positive = ['what is the time right now', 'what is the current time', 'what is the time now', 'what’s the time',
                 'what time is it',
                 'what time is it now', 'do you know what time it is', 'could you tell me the time, please',
                 'what is the time', 'will you tell me the time',
                 'tell me the time', 'time please', 'show me the time', 'what is time', 'whats on the clock', 'clock',
                 'show me the clock', 'what is the time']

time_negative = ['what are you doing', 'what’s up', 'could you', 'do you', 'what’s', 'will you', 'tell me', 'show me',
                 'current', 'do', 'now',
                 'will', 'show', 'tell', 'me', 'could', 'what', 'whats', 'i have time', 'who', 'who is', 'hardtime',
                 'when is time', 'how is time', 'who is time']

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
            'positive': 'time_positive',
            'negative': 'time_negative'
        },
        {
            'import_path': "chatterbot.logic.MathematicalEvaluation",
        }
    ],
)# End bot

# Train the chat bot with the entire english corpus
# trainer.train('chatterbot.corpus.english')
trainer = ChatterBotCorpusTrainer(bot)  # Train bot on list data
trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations")


def nuton_speak(text):
    """
    Function that uses festival, a text to speech package to replay to the user
    :param text: text you wish to be spoke
    """
    if platform.system() == 'Darwin':
        print('Nuton: ' + str(text))
        cmd = ['say', str(text)]
        subprocess.call(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    elif platform.system() == "Windows":
        print('Not supported right now')
    else:
        print('Nuton: ' + str(text))
        subprocess.run(
            'echo "' + str(text) + '" | festival --tts',
            shell=True)


# Instances of speech Recognition
recognizer = sr.Recognizer()

# Heading
print('===================================================='
      '\n========== Nuton, Personal Assistant ==============='
      '\n====================================================\n')

# First question from bot using text to speech)
nuton_speak('Hi I am Nuton, What can I assist you with?')

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
                2. Lunch Application: 'open chrome' - this will do a look up in the applications list(hardcoded atm)
                3. Weather: 'what temperature is it in Galway' - Maybe add onto this this
            """
            response = bot.get_response("what can you do")  # Hardcoded text for testing, not using mic
            nuton_speak(response)

    except sr.UnknownValueError:
        nuton_speak('I am sorry, I could not understand that.')
    except sr.Recognizer as e:
        message = 'My speech recognition service has failed. {0}'
        nuton_speak(message.format(e))
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
