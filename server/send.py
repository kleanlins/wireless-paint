from time import sleep

from _thread import start_new_thread

frequency = 20
data = '00101000101000101001001101011011101010110'

# bool(a) != bool(b) equals a xor b

def clock(freq):
    sleep_time = 1/freq
    while True:
        print("clock")
        sleep(sleep_time)


start_new_thread(clock,(frequency,))
sleep(1)