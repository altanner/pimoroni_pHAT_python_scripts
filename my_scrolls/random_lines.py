#!/usr/bin/env python

import math
import time
import scrollphat as sp
import sys

import random
lines = open('text_to_scroll.txt').read().splitlines()
myline = random.choice(lines)
print(myline)
