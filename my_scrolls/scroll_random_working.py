#!/usr/bin/env python

import scrollphat as sp
import sys
import time
import random
from random import randint

sp.set_rotate(True)
sp.set_brightness(10)

lines = open('text_to_scroll.txt').read().splitlines()

while True:
    myline = random.choice(lines)
    spacer = "   -   "
    random_spacer = randint(3,5)
    random_spacer_length = len(spacer) * random_spacer
    text_length = len(myline)

    sp.write_string((spacer * random_spacer) + random.choice(lines) + (spacer * random_spacer))
        
    length = (text_length + (random_spacer_length * 2) * 5) # pixels to scroll, in total.
    print length

    for x in range(0,length):
        try:
            sp.scroll()
            time.sleep(0.075)
        except KeyboardInterrupt:
            sp.clear()
            sys.exit(-1)
