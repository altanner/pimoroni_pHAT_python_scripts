#!/usr/bin/env python

import scrollphat as sp
import math
import time
import sys
from random import randint

i = 0
buf = [0] * 11
sp.set_brightness(20)

while True: # light random pixels with random brightness
    sp.set_brightness(randint(1,100))
    for q in range(randint(0,3)):
        y = randint(0,4)
        x = randint(0,10)
        sp.set_pixel(x,y,1)
        sp.update()
    time.sleep(0.1)
    sp.clear()
    
