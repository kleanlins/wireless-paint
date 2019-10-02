from _thread import start_new_thread
from time import sleep

import numpy as np
import simpleaudio as sa

import bitarray

import timeit

text = 'eae'
ba = bitarray.bitarray()

ba.frombytes(text.encode('utf-8'))
data = ba.tolist()

data_bit = []
for each in data:
    if each:
        data_bit.append(1)
    else:
        data_bit.append(0)

print(data_bit)
print(len(data_bit))
print("Sent data = ", text)


def modulate(data, freq):
    sleep_time = (1/freq)
    pulse = True

    frequency = 381  # Our played note will be 240 Hz
    fs = 44100  # 44100 samples per second
    seconds = 1.2 * sleep_time  # Note duration of 0.1 seconds

    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * fs, False)

    # Generate a 240 Hz sine wave
    note = np.sin(frequency * t * 2 * np.pi)

    # Ensure that highest value is in 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)

    frequency = 22000  # Our played note will be 240 Hz
    fs2 = 44100  # 44100 samples per second
    seconds = sleep_time  # Note duration of 0.1 seconds
    t = np.linspace(0, seconds, seconds * fs2, False)
    note = np.sin(frequency * t * 2 * np.pi)
    audio2 = note * (2**15 - 1) / np.max(np.abs(note))
    audio2 = audio2.astype(np.int16)

    # sincronização
    play_obj = sa.play_buffer(audio, 1, 2, fs)
    play_obj.wait_done()

    play_obj = sa.play_buffer(audio2, 1, 2, fs)
    play_obj.wait_done()

    for bit in data:
        if bit:
            # start_time = timeit.default_timer()
            play_obj = sa.play_buffer(audio, 1, 2, fs)
            play_obj.wait_done()
            # print(timeit.default_timer() - start_time, "high")
        else:
            # start_time = timeit.default_timer()
            play_obj = sa.play_buffer(audio2, 1, 2, fs)
            play_obj.wait_done()
            # print(timeit.default_timer() - start_time, "low")


# start_new_thread(clock,(frequency,))
# sleep(1)

bits_per_second = 5

modulate(data, bits_per_second)
