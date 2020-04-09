## Gesture Based UI Project  2020

### Developers: Morgan Reilly | Cathal Butler

### Project Statement
*Develop an application with a Natural User Interface. There are a number of options available to
you and this is an opportunity to combine a lot of technology that you have worked with over the
past four years*

### The Project
This project was initially meant to be a Kinect game but was changed due to hardware limitations after the outbreak of COVID-19.
The aim for this project is to make something based around gesture based UI, after carrying out some research it was decided that a
personal voice assistant is what the project was going to be based on using 
   * [Chatterbot](https://chatterbot.readthedocs.io/en/stable/) | Machine Learning, conversational dialog engine.
   * [Speech Recognition](https://pypi.org/project/SpeechRecognition/) | Speech Recognition engine using the Google API.
   * [eSpeak](http://espeak.sourceforge.net/) | Open source speech synthesizer for English and other languages.
  
### What is Nuton
Nuton is your bot that will interpret voice commands you issue it. It does this with the help of the package 
listed above. Nuton uses the Chatterbot package to build and train itself, it then ties in with the speech recognition
to interpret a command from a user with the aid of the google recognition API and that command is then process using the 
Chatterbot dataset and custom logic adapters designed to allow operations like opening applications, querying the weather 
and so on.

### Architecture

![](uploads/nuton.png)

* ### How Nuton Works
    * Nuton is created and trained using [Chatterbot](https://chatterbot.readthedocs.io/en/stable/) a Python machine learning, 
    conversational dialog engine. A Chatterbot starts off with no knowledge of how to communicate but with the help
    of user input, corpus data and logic adapters, the bot can learn and return the correct response to the users input.
    
        ![](uploads/nutons_process_flow.png)
        
* ### Training
    *  Chatterbot has a lot of corpus data files you can use to train the bot or you can specify your own one. In Nutons case
    the English corpus was used for training as well as some custom coupes data that works better with custom logic adapters
  
* ### Gesture Implementation With Hardware
    *  As the project statement states, *develop an application with natural user interacting* this was done by 
    implementing a microphone into the program to record the user's voice. With the help of the Python Speech Recognition 
    engine, it analyzes the audio and return the result as text. The text result would then be passed onto the Chatterbot 
    to process it and return its result.


### Environment Setup -- Linux
* Download [requirements.txt](/requirements.txt)
* Create Virtual Environment
* `python3 -m venv venv`
* Activate Virtual Environment
* `source venv/bin/activate`
* Pip install packages
* `pip install -r requirements.txt`

### eSpeak
 * Ubuntu
    - `sudo apt-get install espeak`
    - Test `echo "Hello World." | espeak`
    - Hello World will be played back to you.
    
 * Manjaro / Arch Linux
    - `sudo pacman -S espeak`
    - Test `echo "Hello World." | espeak`
    - Hello World will be played back to you.

### Running The Application
* Assuming correct set up and activation of environment
* `cd chatbot` 
* `python main.py`

### Development & Testing
This project was developed and tested on
* #### Testing Environments
    * OS: [Manjaro Linux](https://manjaro.org/download/official/kde/) & [Ubuntu 19.19](https://ubuntu.com/)
    * Python 3.8.2
    * [PyCharm 2019.3.4 (Professional Edition)](https://www.jetbrains.com/pycharm/)
      - Build #PY-193.6911.25, built on March 18, 2020
* #### Test Cases 
    * Testing that was carried can be found here [nuton_test_cases.xlsx](/uploads/nuton_test_cases.xlsx)

  
### References
 * https://chatterbot.readthedocs.io/en/stable/index.html
 * https://github.com/Uberi/speech_recognition#readme
 * http://espeak.sourceforge.net/
 * https://realpython.com/python-speech-recognition/
 * https://cmusphinx.github.io/wiki/tutorial/
 * https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst
 * https://stackoverflow.com/questions/31603555/unknown-pcm-cards-pcm-rear-pyaudio -- Fix for PCM card error
 

