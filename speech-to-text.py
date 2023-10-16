# NOTE: this example requires PyAudio because it uses the Microphone class

from vosk import Model, KaldiRecognizer
import pyaudio
import json

model = Model("model/vosk-model-small-en-us-0.15")

recognizer = KaldiRecognizer(model, 16000)

cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)

stream.start_stream()

while True:
    data = stream.read(4096)
    # if len(data) == 0:
    #     break
    if recognizer.AcceptWaveform(data):
        res = json.loads(recognizer.Result())
        text = res["text"]
        print(f'vosk output: {text}')
