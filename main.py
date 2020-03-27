# https://realpython.com/python-speech-recognition/ -- tutorial
# https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst -- Docs
import speech_recognition as sr

# print(sr.__version__)  # Import verification

# Import the Speech Recogniser
recogniser = sr.Recognizer()

# Import Audio File
harvard = sr.AudioFile('audio_files/harvard.wav')
jackhammer = sr.AudioFile('audio_files/jackhammer.wav')

# Use Microphone
mic = sr.Microphone()


# print(sr.Microphone.list_microphone_names())  # Check all available microphones on system


def capture_from_audio(audio_input, offset, duration, adjust_ambient_duration, display_transcript):
    """Capture Data From File"""
    """Offset and Duration useful for segmenting audio if have prior knowledge of audio file"""
    # Check if Recogniser is valid type
    if not isinstance(recogniser, sr.Recognizer):
        raise TypeError("`recogniser` must be an instance of `Recogniser`")

    print(
        f"Capturing from: {audio_input.filename_or_fileobject}\nOffset: {offset}, Duration: {duration}"
        f", Ambient Adjust Duration: {adjust_ambient_duration}, Transcript Display: {display_transcript}")  # Verify method invocation
    with audio_input as source:
        recogniser.adjust_for_ambient_noise(source, adjust_ambient_duration)  # Adjusting for ambient noise
        audio = recogniser.record(source, offset=offset, duration=duration)
        # Can have multiple audio instances here..
        # This will continue from where you left off in the file, for desired duration.
        # NOTE: This may hurt accuracy
        # audio1 = r.record(source, duration=duration) # Example of second clip
    try:
        print('Recognised: ', recogniser.recognize_google(audio, show_all=display_transcript))  # Output audio recognition
        # print(r.recognize_google(audio1))
    except Exception as e:
        print(e)
        print('ERROR: Could not recognise audio\nPlease check input and try agian...')


def capture_from_mic(mic_input):
    """Capture Data From Microphone"""
    if not isinstance(mic, sr.Microphone):
        raise TypeError("'mic' must be an instance of `Microphone`")
    with mic_input as source:
        recogniser.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recogniser.listen(source)  # Listen to voice
    try:
        print('Recognised: ', recogniser.recognize_google(audio))
    except Exception as e:
        print(e)
        print(f'ERROR: Could not recognise audio\nPlease check input and try agian...\n{e}')


# capture_from_audio(harvard, 0, 0, 1, False)  # Using decent, standard audio clip
# capture_from_audio(jackhammer, 0, 0, 0.5, True)  # Using poor quality, standard audio clip
capture_from_mic(mic)
