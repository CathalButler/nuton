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

"""
Time positive / Time negative: 
Training Data for Nuton to understand
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

"""
Initialise a new ChatBot
Storage adapters provide an interface which allow Nuton to connect to data store
Logic adapters determine the logic for how Nuton selects a response to an input statement
"""
bot = ChatBot(
    'Nuton',  # Bot name
    # storage_adapter='chatterbot.storage.SQLStorageAdapter',  # Storage config (SQLite)
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',  # Storage config (MongoDB)
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
    database_uri='mongodb+srv://morgan:root@nutonstore-ldff3.mongodb.net/nutondb'
)  # End bot

"""
Bot Training
Train the chat bot with the entire english corpus
"""
# trainer.train('chatterbot.corpus.english')
trainer = ChatterBotCorpusTrainer(bot)  # Train bot on list data
trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations")


# """Instance of speech Recognition"""
# recognizer = sr.Recognizer()


def nuton_speak(text):
    """
    Function that uses espeak, a text to speech package to replay to the user
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
            'echo "' + str(text) + '" | espeak',
            shell=True)


def display_header():
    # Heading
    print('===================================================='
          '\n========== Nuton, Personal Assistant ==============='
          '\n====================================================\n')


def recognise_from_mic(recogniser, mic):
    """Recognise Input From Microphone"""
    if not isinstance(mic, sr.Microphone):
        raise TypeError("'mic' must be an instance of `Microphone`")
        # Check if Recogniser is valid type
    if not isinstance(recogniser, sr.Recognizer):
        raise TypeError("`recogniser` must be an instance of `Recogniser`")

    while True:
        with mic as source:
            recogniser.adjust_for_ambient_noise(source)  # Adjust for background noise
            audio = recogniser.listen(source)  # Listen to voice
        try:
            audio_recognised = recogniser.recognize_google(audio)
            print('You said: ', audio_recognised)

            """
            Supported questions so far:
                1. Maths : 'What is four plus four?'
                2. Lunch Application: 'open chrome' - this will do a look up in the applications list(hardcoded atm)
                3. Weather: 'what temperature is it in Galway' - Maybe add onto this this
            """
            # response = bot.get_response("")  # Hardcoded text for testing, not using mic
            # nuton_speak(response)
        except Exception as e:
            print(e)
            print(f'ERROR: Could not recognise audio\nPlease check input and try agian...\n{e}')
        except sr.Recognizer as e:
            message = 'My speech recognition service has failed. {0}'
            nuton_speak(message.format(e))
        except (KeyboardInterrupt, EOFError, SystemExit):
            break


def console_input():
    """Testing database with console input"""
    while True:
        try:
            user_input = input()
            bot_response = bot.get_response(user_input)
            print(bot_response)
        # Press ctrl-c or ctrl-d on the keyboard to exit
        except (KeyboardInterrupt, EOFError, SystemExit):
            break


def main():
    """Main Method"""
    display_header()

    recogniser = sr.Recognizer()  # Import the Speech Recogniser
    microphone = sr.Microphone()  # Use Microphone

    recognise_from_mic(recogniser, microphone)

    # First question from bot using text to speech)
    # nuton_speak('Hi I am Nuton, What can I assist you with?')


if __name__ == "__main__":
    main()
