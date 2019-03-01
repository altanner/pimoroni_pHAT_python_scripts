#!/usr/bin/env python

import scrollphat as sp
import math
import time
import sys
from random import randint

i = 0
buf = [0] * 11

while True:
    clear = (randint(0,1000)) # rnd var for timing of crashes
    change_brightness = (randint(0,2))
    if change_brightness == 2:
        sp.set_brightness(randint(1,128))
    y = randint(0,4)
    x = randint(0,10)
    sp.set_pixel(x,y,(randint(0,1)))
    sp.update()
    time.sleep(0.02)
    for r in range(0,2):
        y = randint(0,4)
        x = randint(0,10)
        sp.set_pixel(x,y,0)
        sp.update()
        time.sleep(0.01)
    if clear > 993:
        if clear > 996:
            for w in range(0,randint(3,9)):
                for x in range(0,11):
                    for y in range(0,5):
                        sp.set_pixel(x,y,randint(0,1))
                        sp.set_brightness(128)
                sp.update()
                time.sleep(0.01)
                sp.clear()
                time.sleep(0.01)
        else:
            for w in range(0,randint(3,9)):
                for x in range(0,11):
                    for y in range(0,randint(1,5)):
                        sp.set_pixel(x,y,1)
                        sp.set_brightness(128)
                sp.update()
                time.sleep(0.01)
                sp.clear()
                time.sleep(0.01)
    
