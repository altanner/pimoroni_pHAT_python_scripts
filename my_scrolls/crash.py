#!/usr/bin/env python

import scrollphat as sp
import math
import time
import sys
from random import randint

sp.set_rotate(False)

clear = randint(0,10)
if clear > 5:
    for w in range(0,randint(5,20)):
        for x in range(0,11):
            for y in range(0,5):
                sp.set_pixel(x,y,randint(0,1))
                sp.set_brightness(128)
        sp.update()
        time.sleep(0.01)
        sp.clear()
else:
    for w in range(0,randint(5,20)):
        for x in range(0,11):
            for y in range(0,randint(1,5)):
                sp.set_pixel(x,y,1)
                sp.set_brightness(128)
        sp.update()
        time.sleep(0.01)
        sp.clear()
    
