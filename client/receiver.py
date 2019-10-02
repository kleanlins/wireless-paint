import pyaudio
import wave
import binascii
from bitstring import BitArray
import bitarray
import numpy as np

from image_rcv import binary_to_image

bits_per_sec = 5
bit_frame_size = 1000//bits_per_sec
bit_frame_size = bit_frame_size * 1.2

chunk = 1  # Record in chunks of 1 sample
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 1
fs = 1000  # Record at 44100 samples per second
filename = "../static/output.wav"

p = pyaudio.PyAudio()  # Create an interface to PortAudio

print('Recording')

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)


count = 0

clock_size = 0

qtd_high = 0
qtd_low = 0

frames = []
output = []


print("Waiting for a clock.")
while True:
    data = stream.read(chunk, exception_on_overflow=False)
    a = BitArray(bytes=data, length=16)

    if abs(a.int) > 15000:
        qtd_high += 1
        # clock_size += 1

    if qtd_high > 3:
        qtd_high = 0
        print("Clock found.")
        break

lowstate = [30000, 30000, 30000, 30000, 30000]
while True:
    data = stream.read(chunk, exception_on_overflow=False)
    a = BitArray(bytes=data, length=16)
    clock_size += 1

    lowstate.append(abs(a.int))
    del lowstate[0]

    if np.mean(lowstate) < 5000:
        print(f"Clock ended.\nClock size: {clock_size}ms")
        bit_frame_size = clock_size
        break


qtd_high = 0
qtd_low = 0
count = 0

tail = [1 for _ in range(10)]
bit_value = 0

# bit_frame_size = bit_frame_size * 1.1

while True:
    data = stream.read(chunk, exception_on_overflow=False)
    a = BitArray(bytes=data, length=16)
    count += 1

    # print(abs(a.int))

    if abs(a.int) > 4500:
        qtd_high += 1

    if count == bit_frame_size:
        bit_value = 1 if qtd_high > 130 else 0
        output.append(bit_value)

        print(bit_value)
        # print(qtd_high)

        qtd_high = 0
        count = 0

        tail.append(bit_value)
        del tail[0]
        if np.mean(tail) == 0:
            break

    # # Stop and close the stream
    # # Terminate the PortAudio interface
    # p.terminate()

stream.stop_stream()
stream.close()

print('Finished recording')
print(output[1:-10])
print(len(output[1:-10]))
decoded_data = bitarray.bitarray(output[1:-10]).tobytes().decode('utf-8')
print("Received data = ", decoded_data)

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
