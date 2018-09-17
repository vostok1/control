#!/usr/bin/env python
import time
import serial
import matplotlib.pyplot as plt
from drawnow import *
from time import sleep
values = []


ser = serial.Serial(
 port='/dev/ttyACM0',
 baudrate = 9600,
 parity=serial.PARITY_NONE,
 stopbits=serial.STOPBITS_ONE,
 bytesize=serial.EIGHTBITS,
 timeout=0.4
)

plt.ion()
cnt=0	
for i in range(0,2):
	values.append(0.0)
def plotValues():
    plt.title('Serial value from Nucleo')
    plt.grid(True)
    plt.ylabel('Values')
    plt.plot(values, 'rx-', label='values')
    plt.legend(loc='upper right')
    plt.ylim(0, 120) 

while 1:
	x=ser.readline()
	
	cnt = float(x)
	
	print x
	values.append(cnt)
	values.pop(0)
	drawnow(plotValues)
	
	        
	