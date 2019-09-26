import pyaudio
import wave
import binascii
from bitstring import BitArray
from bitarray import bitarray
import matplotlib.pyplot as plt
import numpy as np

from image_rcv import binary_to_image

chunk = 1  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 1
fs = 1000  # Record at 44100 samples per second
seconds = 3
filename = "../static/output.wav"

p = pyaudio.PyAudio()  # Create an interface to PortAudio

print('Recording')

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

frames = []  # Initialize array to store frames

# Store data in chunks for 3 seconds
for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    a = BitArray(bytes=data, length=16)
    # print(type(data))
    frames.append(a.int)

# frames = ''.join(frames)
# amplitude = np.fromstring(frames, np.int16)

# Stop and close the stream
stream.stop_stream()
stream.close()
# Terminate the PortAudio interface
p.terminate()

bitstream = []

print(len(frames))
# for each in frames:
# a = BitArray(bytes=each, length=16)
# print(a)
# print(each)
# print(a.int)
# bitstream.append(a.bin)

print('Finished recording')


# Save the recorded data as a WAV file
# wf = wave.open(filename, 'wb')
# wf.setnchannels(channels)
# wf.setsampwidth(p.get_sample_size(sample_format))
# wf.setframerate(fs)
# wf.writeframes(b''.join(frames))
# wf.close()

t = [i for i in range(0, 3000)]
plt.plot(t, frames)
plt.show()
