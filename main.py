# Cathal Butler & Morgan Reilly | Gesture Based desktop_app Project - 2020

# https://realpython.com/python-speech-recognition/ -- tutorial 0
# https://cmusphinx.github.io/wiki/tutorial/ -- Tutorial 1
# https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst -- Docs
# https://stackoverflow.com/questions/31603555/unknown-pcm-cards-pcm-rear-pyaudio -- Fix for PCM card error
import speech_recognition as sr
import os
import subprocess


def process_audio_file(recogniser, audio_input, offset, duration, adjust_ambient_duration, display_transcript):
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


def capture_from_mic(recogniser, mic_input):
    """Capture Data From Microphone"""
    if not isinstance(mic_input, sr.Microphone):
        raise TypeError("'mic' must be an instance of `Microphone`")
    with mic_input as source:
        recogniser.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recogniser.listen(source)  # Listen to voice
    try:
        audio_recognised = recogniser.recognize_google(audio)
        audio_recognised.lower()
        print('Recognised: ', audio_recognised.lower())
        return audio_recognised

    except Exception as e:
        print(f'ERROR: Could not recognise audio\nPlease check input and try again...\n{e}')


def main():
    # Import the Speech Recogniser
    recogniser = sr.Recognizer()

    # Read in application names
    # commands_dictionary = read_command_file()

    # Import Audio File
    # TODO - Testing files
    harvard = sr.AudioFile('audio_files/harvard.wav')
    jackhammer = sr.AudioFile('audio_files/jackhammer.wav')

    # Use Microphone
    mic = sr.Microphone()

    # Heading
    print('===================================================='
          '\n========== Application Speech Command =============='
          '\n====================================================\n')
    # Options
    print('Please say what option you would like to use:\n1: Command from microphone\n2:Process an audio file'
          '(Please only submit .wav files\n)')

    processed_input = capture_from_mic(recogniser, mic)
    # result = query_dictionary(commands_dictionary, processed_input)
    #
    # if result == "capture_mic":
    #     print('Please say the name of the application you wish to run\n')
    #     request = capture_from_mic(recogniser, mic)
    #     result = query_dictionary(commands_dictionary, request)
    #     exec_command(result)  # execute command
    #
    # elif result == "process_audio_file":
    #     print('Please in the console specify a file path that is .wav format to be processed')
    #     # TODO: Testing the file path is working when it is passed as a str
    #     file_path = input()
    #     request = process_audio_file(recogniser, file_path, 0, 0, 1, False)  # Using decent, standard audio clip


# process_audio_file(harvard, 0, 0, 1, False)  # Using decent, standard audio clip
# process_audio_file(jackhammer, 0, 0, 0.5, True)  # Using poor quality, standard audio clip
# audio_recognised = capture_from_mic(recogniser, mic)

# print('Captured Audio: ', audio_recognised)


if __name__ == "__main__":
    main()
