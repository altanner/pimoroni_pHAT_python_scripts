#!/usr/bin/env python

import scrollphat as sp
import sys, time, random, math
from random import randint

sp.set_rotate(True)
sp.set_brightness(50)

lines = open('/home/pi/Pimoroni/scrollphat/my_scrolls/text_to_scroll.txt').read().splitlines()

#while True:
try:        
    line_to_scroll = random.choice(lines)
    sp.write_string("     *  *  *   " + line_to_scroll + "     ")
    string_length = sp.buffer_len()
    while string_length > 0:
        sp.scroll()
        time.sleep(0.065)
        string_length -= 1
except KeyboardInterrupt:
    sp.clear()
    sys.exit(-1)

