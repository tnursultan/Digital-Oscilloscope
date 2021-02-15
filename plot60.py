from scipy import signal
import matplotlib.pyplot as plot
import matplotlib.animation as animation
import numpy as np
import sys, time, math

import serial
import serial.tools.list_ports

# Sampling rate 3020 hz / second
tx = np.linspace(0, 1, 3020, endpoint=True)

# Plot the square wave signal
plot.plot(tx*100, 2.5*signal.square(4*np.pi * 3.42 * tx + np.pi)+2.5)

# x = np.linspace(-1, 2, 100)
# y = np.exp(x)
#
# plot.figure()
# plot.plot(x, -np.exp(-x))

# Give a title for the square wave plot
plot.title('60 Hz Square Wave Graph')

# Give x axis label for the square wave plot
plot.xlabel('Time (Milliseconds)')

# Give y axis label for the square wave plot
plot.ylabel('Amplitude (Volts)')

plot.grid(True, which='both')

# Provide x axis and line color
plot.axhline(y=0, color='k')

# Set the max and min values for y axis
plot.ylim(-10, 10)

plot.xlim(0, 100)

# Display the square wave drawn
plot.show()

# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# import sys, time, math
#
# import serial
# import serial.tools.list_ports
#
# xsize = 120
#
# try:
#     ser.close() # try to close the last opened port
# except:
#     print('')
#
# portlist=list(serial.tools.list_ports.comports())
# print ('Available serial ports (will try to open the last one):')
# for item in portlist:
#     print (item[0])
#
# # configure the serial port
# ser = serial.Serial(
#     port=item[0],
#     baudrate=115200,
#     parity=serial.PARITY_NONE,
#     stopbits=serial.STOPBITS_TWO,
#     bytesize=serial.EIGHTBITS
# )
# ser.isOpen()
#
# print ('To stop press Ctrl+C')
#
# def data_gen():
#     t = data_gen.t
#
#     while True:
#        strin = ser.readline()
#        t+=1
#        val= float(strin.decode())
#        print(float(strin.decode()))
#        yield t, val
#
#
# def run(data):
#     # update the data
#     t,y = data
#     if t>-1:
#         xdata.append(t)
#         ydata.append(y)
#         if t>xsize: # Scroll to the left.
#             ax.set_xlim(t-xsize, t)
#         line.set_data(xdata, ydata)
#
#     return line
#
# def on_close_figure(event):
#     sys.exit(0)
#
# data_gen.t = -1
# fig = plt.figure()
# fig.canvas.mpl_connect('close_event', on_close_figure)
# ax = fig.add_subplot(111)
# line, = ax.plot([], [], lw=2, label='Voltage curve')
# ax.set_ylim(-5, 10)
# ax.set_xlim(0, xsize)
# ax.grid()
# ax.legend()
# plt.title('Frequency Graph')
# plt.xlabel('Time (Seconds)')
# plt.ylabel('Voltage (Volts)')
#
# xdata, ydata = [], []
#
# # Important: Although blit=True makes graphing faster, we need blit=False to prevent
# # spurious lines to appear when resizing the stripchart.
# ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=500, repeat=False)
# plt.show()
