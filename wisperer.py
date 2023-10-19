# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import whisper
import numpy as np
import torch
import soundfile as sf

# DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# base_model = whisper.load_model("base.en")
# print(
#     f"Model is {'multilingual' if base_model.is_multilingual else 'English-only'} "
#     f"and has {sum(np.prod(p.shape) for p in base_model.parameters()):,} parameters."
# )

# # transcribing a .wav file
# print(base_model.transcribe("transcribe-audio-1697623765857191700.wav")['text'])

# obtain audio from the microphone (Batch processing)
r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Say something!")
#     audio = r.listen(source)

# # recognize speech using whisper
# try:
#     print("Whisper thinks you said " + r.recognize_whisper(audio, language="english"))
# except sr.UnknownValueError:
#     print("Whisper could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Whisper")

# Real time processing

# Start listening to the microphone
with sr.Microphone() as source:
    print("Say something!")

    # Adjust for ambient noise
    r.adjust_for_ambient_noise(source)

    # Initialize a variable to store the spoken text
    spoken_text = ""

    while True:
        try:
            audio = r.listen(source, timeout=1)  # Adjust the timeout as needed

            # Recognize speech using Whisper
            text = r.recognize_whisper(audio, language="english")

            # Append the recognized text to the spoken_text variable
            spoken_text += " " + text

            print("You said: " + text)

        except sr.WaitTimeoutError:
            # If there's a period of silence, break the loop
            break

        except sr.UnknownValueError:
            # Handle unrecognized speech or silence
            pass

        except sr.RequestError as e:
            print("Could not request results from Whisper")

    # Print and save the entire spoken text
    print("Spoken text: " + spoken_text)

# # # recognize speech using Whisper API
# OPENAI_API_KEY = "INSERT OPENAI API KEY HERE"
# try:
#     print(f"Whisper API thinks you said {r.recognize_whisper_api(audio, api_key=OPENAI_API_KEY)}")
# except sr.RequestError as e:
#     print("Could not request results from Whisper API")