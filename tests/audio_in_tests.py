# Cathal Butler & Morgan Reilly | Gesture Based desktop_app Project - 2020

# https://realpython.com/python-speech-recognition/ -- tutorial 0
# https://cmusphinx.github.io/wiki/tutorial/ -- Tutorial 1
# https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst -- Docs
# https://stackoverflow.com/questions/31603555/unknown-pcm-cards-pcm-rear-pyaudio -- Fix for PCM card error
import speech_recognition as sr
import os


def capture_from_audio(recogniser, audio_input, offset, duration, adjust_ambient_duration, display_transcript):
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
        print('Recognised: ',
              recogniser.recognize_google(audio, show_all=display_transcript))  # Output audio recognition
    except Exception as e:
        print(e)
        print('ERROR: Could not recognise audio\nPlease check input and try agian...')


def capture_from_mic(recogniser, mic):
    """Capture Data From Microphone"""
    if not isinstance(mic, sr.Microphone):
        raise TypeError("'mic' must be an instance of `Microphone`")
    with mic as source:
        recogniser.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recogniser.listen(source)  # Listen to voice
    try:
        audio_recognised = recogniser.recognize_google(audio)
        print('Recognised: ', recogniser.recognize_google(audio))
    except Exception as e:
        print(e)
        print(f'ERROR: Could not recognise audio\nPlease check input and try agian...\n{e}')

    return audio_recognised


def run_mic_test(recogniser, microphone):
    audio_recognised = capture_from_mic(recogniser, microphone)
    print('Captured Audio: ', audio_recognised)


def run_file_test(recogniser):
    working_dir = os.path.dirname(os.path.abspath(__file__))
    # Import Audio File
    harvard = sr.AudioFile(os.path.join(working_dir, 'audio_files/harvard.wav'))
    jackhammer = sr.AudioFile(os.path.join(working_dir, 'audio_files/jackhammer.wav'))
    capture_from_audio(recogniser, harvard, 0, 0, 1, False)  # Using decent, standard audio clip
    capture_from_audio(recogniser, jackhammer, 0, 0, 0.5, True)  # Using poor quality, standard audio clip


def main():
    recogniser = sr.Recognizer()  # Import the Speech Recogniser
    microphone = sr.Microphone()  # Use Microphone

    run_file_test(recogniser)
    run_mic_test(recogniser, microphone)


if __name__ == "__main__":
    main()
