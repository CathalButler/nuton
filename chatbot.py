import speech_recognition as sr
from chatterbot import ChatBot
import platform
import subprocess
from chatterbot.trainers import ChatterBotCorpusTrainer


# Install festival & festival-english for the bot to response

class VoiceChatBot(ChatBot):

    def speak(self, text):
        if platform.system() == 'Darwin':
            # Use Mac's built-in say command to speak the response
            cmd = ['say', str(text)]
            subprocess.call(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            subprocess.run(
                'echo "' + str(text) + '" | festival --tts',
                shell=True)

    def get_response(self, statement=None, **kwargs):
        response = super().get_response(statement, **kwargs)
        self.speak(response.text)


# Create new Chat bot called 'Unton' that uses a sqlite database
# bot = ChatBot(
#     'Nuton',
#     storage_adapter='chatterbot.storage.SQLStorageAdapter',
#     # database_uri='sqlite:///database.sqlite3',
#     trainer=('chatterbot.corpus.english',
#              "chatterbot.corpus.english.greetings",
#              "chatterbot.corpus.english.conversations",
#              ["Open"]
#              )
# )  # End ChatBot Instance

# Create a bot called 'Nuton'
voiceBot = VoiceChatBot('Nuton')

trainer = ChatterBotCorpusTrainer(voiceBot)
# Train the chat bot with the entire english corpus
trainer.train('chatterbot.corpus.english')

# Instances of speech Recognition
recognizer = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            recognizer_function = getattr(recognizer, 'recognize_google')

            result = recognizer_function(audio)
            if result == str("open an application"):
                voiceBot.speak('What application do you wish to open?')
                # TODO - CB - Have an application open on request
            else:
                voiceBot.get_response(text=result)

    except sr.UnknownValueError:
        voiceBot.speak('I am sorry, I could not understand that.')
    except sr.Recognizer as e:
        message = 'My speech recognition service has failed. {0}'
        voiceBot.speak(message.format(e))
    except (KeyboardInterrupt, EOFError, SystemExit):
        print('end')
        break
