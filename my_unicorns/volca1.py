import unicornhat as uh
import time, serial, random
from random import randint

uh.set_layout(uh.PHAT) # PHAT is 8x4
uh.brightness(0.5)     # 1 is bright, 0 is dark. <0.4 is normally black...

ser = serial.Serial('/dev/ttyAMA0', baudrate=38400) # MIDI signal in

while True:
    data = ord(ser.read(1)) # read a byte
    if data != 240: # ignore 240, i think 240 is the bpm/clock?
        print data # me

    if data == (14 or 142):        # when you hear a kick
        for y in range(4):
            for x in range(8):
                uh.set_pixel(x,y,255,0,0)
        uh.show()
        
    if data == (206 or 78):        # when you hear a snare
        for y in range(4):
            for x in range(8):
                uh.set_pixel(x,y,0,255,0)
        uh.show()

    if data == (17):        # when you hear a closed hihat
        for y in range(4):
            for x in range(8):
                uh.set_pixel(x,y,0,0,255)
        uh.show()
