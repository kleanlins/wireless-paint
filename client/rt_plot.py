from numpy import *
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
from bitstring import BitArray
import pyaudio

# Create object serial port

### START QtApp #####
# you MUST do this once (initialize things)
app = QtGui.QApplication([])
####################

win = pg.GraphicsWindow(title="Signal from serial port")  # creates a window
# creates empty space for the plot in the window
p = win.addPlot(title="Realtime plot")
curve = p.plot()                        # create an empty "plot" (a curve to plot)

windowWidth = 500                       # width of the window displaying the curve
# create array that will contain the relevant time series
Xm = linspace(0, 0, 3000)
ptr = -windowWidth                      # set first x position

# Realtime data plot. Each time this function is called, the data display is updated
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

frames = [0 for i in range(0, 3000)]  # Initialize array to store frames
t = [i for i in range(0, 3000)]


def update():
    global curve, ptr, Xm
    # shift data in the temporal mean 1 sample left
    Xm[:-1] = Xm[1:]
    # value = ser.readline()                # read line (single value) from the serial port
    data = stream.read(chunk)
    a = BitArray(bytes=data, length=16)
    # vector containing the instantaneous values
    Xm[-1] = float(a.int)
    ptr += 1                              # update x position for displaying the curve
    curve.setData(Xm)                     # set the curve with this data
    curve.setPos(ptr, 0)                   # set x position in the graph to 0
    QtGui.QApplication.processEvents()    # you MUST process the plot now


### MAIN PROGRAM #####
# this is a brutal infinite loop calling your realtime data plot
while True:
    update()

### END QtApp ####
pg.QtGui.QApplication.exec_()  # you MUST put this at the end
