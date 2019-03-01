#!/usr/bin/env python

import scrollphat as sp
import sys
import time

#sp.set_brightness(1)

while True:
    try:
        for y in range(0,5):
            for x in range(0,11):
#                sp.set_brightness(3 * x)
                sp.set_pixel(x,y,1)
                sp.update()
            time.sleep(1)
    except KeyboardInterrupt:
        sp.clear()
        sys.exit(-1)


