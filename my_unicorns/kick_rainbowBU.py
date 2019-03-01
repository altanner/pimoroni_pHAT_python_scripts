#!/usr/bin/env python

import unicornhat as unicorn
import time, math, colorsys
import random
from random import randint

unicorn.set_layout(unicorn.PHAT)
#unicorn.brightness(0.5)

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
        bright = bright - 0.01 #fade on each pass until black
