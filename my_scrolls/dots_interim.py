#!/usr/bin/env python

import scrollphat as sp
import math
import time
import sys
from random import randint

while True:
    change_brightness = (randint(0,2))
    if change_brightness == 2:
        sp.set_brightness(randint(1,32))
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
