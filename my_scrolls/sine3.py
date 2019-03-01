#!/usr/bin/env python

import scrollphat
import math
import time
import sys
from random import randint

i = 0
buf = [0] * 11
scrollphat.set_brightness(1)

while True:
    try:
        for x in range(0, 11):
            y = (math.sin((i + (x * 10)) / 10.0) + 1) # Produces range from 0 to 2
            y *= 2.5 # Scale to 0 to 5
            buf[x] = 1 << int(y)

#        scrollphat.set_brightness(randint(1,100))
        for q in range(randint(0,3)):
            y = randint(0,4)
            x = randint(0,10)
            scrollphat.set_pixel(x,y,1)
                                     #   sp.update()
                                      #      time.sleep(0.1)
                                       #         sp.clear()
                                                
        scrollphat.set_buffer(buf)
        scrollphat.update()

        time.sleep(0.5)

        i += 1
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)
