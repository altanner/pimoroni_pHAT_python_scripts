#!/usr/bin/env python

import unicornhat as unicorn
import time, colorsys
import numpy as np
import random
from random import randint

#unicorn.brightness(0.5)
unicorn.set_layout(unicorn.PHAT)

while True:
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
    for p in range(3):
        red2 = randint(0,255)
        gre2 = randint(0,255)
        blu2 = randint(0,255)
        unicorn.set_pixel(randint(0,8), randint(0,4), red2, gre2, blu2)
    unicorn.show()
    time.sleep(0.06)
    unicorn.clear()
    unicorn.show()
    time.sleep(0.3)
    
#    for y in range(4):
#        for x in range(8):
#            h = 0.1 * rand_mat[x, y]
#            s = 0.8
#            v = rand_mat[x, y]
#            rgb = colorsys.hsv_to_rgb(h, s, v)
#            r = int(rgb[0]*255.0)
#            g = int(rgb[1]*255.0)
#            b = int(rgb[2]*255.0)
#            unicorn.set_pixel(x, y, r, g, b)
#        unicorn.show()
#	time.sleep(0.3)
