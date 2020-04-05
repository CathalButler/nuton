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
   * [Speech Recognition](https://pypi.org/project/SpeechRecognition/) | Speech Recognition engine using the Google API
   * [Festival](http://www.cstr.ed.ac.uk/projects/festival/) | Multi-lingual text-to-speech package
### Nuton
Nuton, is your personal bot that will interpret voice commands you issue it. It does this with the help of the package 
listed above. Nuton uses the the Chatterbot package to build and train itself, it then ties in with the speech recognition
to interpret a command from a user with the aid of the google recognition API and that command is then process using the 
Chatterbot dataset and custom logic adapters designed to allow operations like opening applications and querying the weather

![](uploads/nuton.png)


### Environment Setup -- Linux
* Note: [Festival](http://www.cstr.ed.ac.uk/projects/festival/) may need to be manully install if it is not already
installed with your OS 
* Download [requirements.txt](/requirements.txt)
* Create Virtual Environment
* `python3 -m venv venv`
* Activate Virtual Environment
* `source venv/bin/activate`
* Pip install packages
* `pip install -r requirements.txt`

### Running The Application
* Assuming correct set up and activation of environment
* In root directory, type:
* `python main.py`

### Development & Testing
This project was developed and tested on
* OS: [Manjaro Linux](https://manjaro.org/download/official/kde/) & [Ubuntu 19.19](https://ubuntu.com/)
* Python 3.8.2
* [PyCharm 2019.3.4 (Professional Edition)](https://www.jetbrains.com/pycharm/)
  - Build #PY-193.6911.25, built on March 18, 2020
  
### References
 * https://chatterbot.readthedocs.io/en/stable/index.html
 * https://github.com/Uberi/speech_recognition#readme
 * http://www.cstr.ed.ac.uk/projects/festival/
 * https://realpython.com/python-speech-recognition/
 * https://cmusphinx.github.io/wiki/tutorial/
 * https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst
 * https://stackoverflow.com/questions/31603555/unknown-pcm-cards-pcm-rear-pyaudio -- Fix for PCM card error
 

