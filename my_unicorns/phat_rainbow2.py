#!/usr/bin/env python

import unicornhat as unicorn
import time, math, colorsys, random

unicorn.set_layout(unicorn.PHAT)
unicorn.brightness(0.5)

i = 0.0
offset = 30
#sin_or_cos = [sin, cos]
while True:
#    i = i + 0.3
    i = i + random.uniform(0.06, 0.6)
    for y in range(4):
        for x in range(8):
#            r = 0#x * 32
#            g = 0#y * 32
#            xy = x + y / 4
            r = (math.cos((x+i)/2.0) + math.cos((y+i)/2.0)) * 64.0 + 128.0
            g = (math.sin((x+i)/1.5) + math.sin((y+i)/2.0)) * 64.0 + 128.0
            b = (math.sin((x+i)/2.0) + math.cos((y+i)/1.5)) * 64.0 + 128.0
#            b = (math.sin((x+i)/2.0) + math.cos((y+i)/1.5)) * 64.0 + 128.0 this is what these were before ^^^
            r = max(0, min(random.uniform(0, 255), r + (1/offset)))
            g = max(0, min(255, g + offset))
            b = max(0, min(255, b + offset))
            unicorn.set_pixel(x,y,int(r),int(g),int(b))
        unicorn.show()
        time.sleep(0.01)
