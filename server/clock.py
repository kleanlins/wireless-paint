from _thread import start_new_thread
from time import sleep

import numpy as np
import simpleaudio as sa

data = [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0]
def modulate(data, freq):
	sleep_time = (1/freq)
	pulse = True

	frequency = 1000  # Our played note will be 440 Hz
	fs = 44100  # 44100 samples per second
	seconds = sleep_time  # Note duration of 0.1 seconds

	# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
	t = np.linspace(0, seconds, seconds * fs, False)

	# Generate a 440 Hz sine wave
	note = np.sin(frequency * t * 2 * np.pi)

	# Ensure that highest value is in 16-bit range
	audio = note * (2**15 - 1) / np.max(np.abs(note))
	# Convert to 16-bit data
	audio = audio.astype(np.int16)	

	for each in data:
		print(bool(each) != bool(pulse))
		if bool(each) != bool(pulse):
			#winsound.Beep(3000, 50)
			play_obj = sa.play_buffer(audio, 1, 2, fs)
			#play_obj.wait_done()
		else:
			sleep(sleep_time)
		pulse = not pulse


#start_new_thread(clock,(frequency,))
sleep(1)

modulate(data, 20)