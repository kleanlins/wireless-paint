import pyaudio
import wave
import binascii
from bitstring import BitArray
import matplotlib.pyplot as plt
import numpy as np
import pyqtgraph as pg

from image_rcv import binary_to_image

bits_per_sec = 10
bit_frame_size = 1000//bits_per_sec

chunk = 1  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 1
fs = 1000  # Record at 44100 samples per second
seconds = 4
filename = "../static/output.wav"

p = pyaudio.PyAudio()  # Create an interface to PortAudio

print('Recording')

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)


frames = [0 for _ in range(1000)]

while True:
    data = stream.read(chunk)
    a = BitArray(bytes=data, length=16)
#     # print(type(data))
    # frames[]
    frames.append(abs(a.int))

    # print(abs(a.int))
    mean = np.mean(frames[-bit_frame_size:])
    # print(mean)
    if mean > 15000:
        print(1)
    else:
        print(0)
    # print(abs(a.int))

# Store data in chunks for 3 seconds
# for i in range(0, int(fs / chunk * seconds)):
#     data = stream.read(chunk)
#     a = BitArray(bytes=data, length=16)
#     # print(type(data))
#     frames.append(a.int)

# frames = ''.join(frames)
# amplitude = np.fromstring(frames, np.int16)

# # Stop and close the stream
# stream.stop_stream()
# stream.close()
# # Terminate the PortAudio interface
# p.terminate()


print('Finished recording')


# Save the recorded data as a WAV file
# wf = wave.open(filename, 'wb')
# wf.setnchannels(channels)
# wf.setsampwidth(p.get_sample_size(sample_format))
# wf.setframerate(fs)
# wf.writeframes(b''.join(frames))
# wf.close()

# t = [i for i in range(0, seconds*1000)]
# frames = [abs(number) for number in frames]
# plt.plot(t, frames)
# plt.show()
