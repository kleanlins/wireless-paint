import winsound
import time

ms = 200
s = ms/1000

t = True
for _ in range(100):
    if t:
        winsound.Beep(2000, ms)
        time.sleep(s)
        t = False
    else:
        winsound.Beep(25000, ms)
        time.sleep(s)
        t = True
