'''

сколько времени
время

какая погода
погоде
'''
import pyaudio
import wave

audio = pyaudio.PyAudio()

stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
print('Start...')
frames = []
for i in range(0, int(44100 / 1024 * 5)):
    data = stream.read(1024)
    frames.append(data)
print('Finish...')
stream.stop_stream()
stream.close()
audio.terminate()

with wave.open('1.wav', 'wb') as f:
    f.setnchannels(1)
    f.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    f.setframerate(44100)
    f.writeframes(b''.join(frames))



wf = wave.open('1.wav', 'rb')
audio = pyaudio.PyAudio()
stream = audio.open(
   format=audio.get_format_from_width(wf.getsampwidth()),
    channels=wf.getnchannels(),
    rate=wf.getframerate(),
    output=True,
)
data = wf.readframes(1024)
while data:
    stream.write(data)
    data = wf.readframes(1024)
stream.close()
audio.terminate()

audio = pyaudio.PyAudio()
num_devices = audio.get_device_count()
print('Number of devices:', num_devices)




