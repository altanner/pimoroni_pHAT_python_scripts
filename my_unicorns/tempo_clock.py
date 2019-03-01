#!/usr/bin/env python

import unicornhat as unicorn
import numpy as np
import time, math, colorsys, random, serial
from random import randint

unicorn.set_layout(unicorn.PHAT)

def kick_rainbow():
    random_r = randint(0,255)
    random_g = randint(0,255)
    random_b = randint(0,255)
    random_math_r = randint(32,640)
    random_math_g = randint(32,640)
    random_math_b = randint(32,640)
    bright = 1
    i = 0.0
    offset = 30

    for q in range(20): #splash a kick for 20 revs
        i = i + 0.3
        for y in range(4):
            for x in range(8):
                r = 0#x * 32
                g = 0#y * 32
                xy = x + y / 4
                r = (math.cos((x+i)/2.0) + math.cos((y+i)/2.0)) * 64 + 128.0
                g = (math.sin((x+i)/1.5) + math.sin((y+i)/2.0)) * 64 + 128.0
                b = (math.sin((x+i)/2.0) + math.cos((y+i)/1.5)) * 64 + 128.0
                r = max(0, min(random_r, r + offset))
                g = max(0, min(random_g, g + offset))
                b = max(0, min(random_b, b + offset))
                unicorn.set_pixel(x,y,int(r),int(g),int(b))
            unicorn.brightness(bright)
            unicorn.show()
            time.sleep(0.001)
            if bright > 0.3:
                bright = bright - 0.01 #fade on each pass until black
    unicorn.clear()
    
def hihat_splash():
    unicorn.brightness(1)
    y_loc = randint(0,2)
    x_loc = randint(0,6)
    red = randint(192,255)
    gre = randint(192,255)
    blu = randint(192,255)
    unicorn.set_pixel(x_loc, y_loc, red, gre, blu)
    unicorn.set_pixel((x_loc + 1), y_loc, red, gre, blu)
    unicorn.set_pixel((x_loc + 1), (y_loc + 1), red, gre, blu)
    unicorn.set_pixel(x_loc, (y_loc + 1), red, gre, blu)
    for p in range(7):
        red2 = randint(0,255)
        gre2 = randint(0,255)
        blu2 = randint(0,255)
        unicorn.set_pixel(randint(0,8), randint(0,4), red2, gre2, blu2)
    unicorn.show()
    time.sleep(0.05)
    unicorn.clear()
    unicorn.show()
#    unicorn.set_pixel((x_loc - 1), (y_loc - 1), red2, gre2, blu2)
#    unicorn.set_pixel((x_loc - 1), (y_loc + 2), red2, gre2, blu2)
#    unicorn.set_pixel((x_loc + 2), (y_loc - 1), red2, gre2, blu2)
#    unicorn.set_pixel((x_loc + 2), (y_loc + 2), red2, gre2, blu2)
#    unicorn.brightness(0.7)
#    unicorn.show()
#    time.sleep(0.05)
#    unicorn.clear()
#    unicorn.show()

ser = serial.Serial('/dev/ttyAMA0', baudrate=38400) #original

message = [0, 0, 0]
while True:
    i = 0
    while i < 3:
        data = ord(ser.read(1)) # read a byte
#        if data != 240: # i think 240 is the bpm?
#            print data # me
        if data == (14 or 142): #kicks contain this message
            print("kick")
            kick_rainbow()
        if data == 17: # hihats
            hihat_splash()
#        if data == 206:
#            for y in range(4):
#                for x in range(8):
#                    unicorn.set_pixel(x,y,255,255,255)
#                unicorn.show()
                                                                                  

