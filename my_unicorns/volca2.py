import unicornhat as uh
import time, serial, random
from random import randint

uh.set_layout(uh.PHAT)
uh.brightness(0.5)

ser = serial.Serial('/dev/ttyAMA0', baudrate=38400) #original    

message = [0, 0, 0]
while True:
    i = 0 # there are 3 bytes to the midi message? something like that
    while i < 3:
      data = ord(ser.read(1)) # read a byte
      if data != 240: # i think 240 is the bpm?
        print data # me
      if data == 14 or data == 142:
        for y in range(4):
          for x in range(8):
            uh.set_pixel(x,y,randint(0,255),randint(0,255),randint(0,255))
        uh.show()
      if data == 206:
        for y in range(4):
          for x in range(8):
            uh.set_pixel(x,y,255,255,255)
        uh.show()
      
