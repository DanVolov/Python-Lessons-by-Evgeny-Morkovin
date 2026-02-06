import pyaudio
import audioop

audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16,channels=1, rate=44100, frames_per_buffer=1024, input=True)

while True:
    data = stream.read(1024)
    r = audioop.rms(data, 2)
    print(r)
stream.close()
audio.terminate()
