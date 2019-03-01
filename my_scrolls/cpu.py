#!/usr/bin/env python

import time
import scrollphat
import psutil
import sys

i = 0
scrollphat.set_brightness(20)

cpu_values = [0] * 11

while True:
	try:
		cpu_values.pop(0)
		cpu_values.append(psutil.cpu_percent())

		scrollphat.graph(cpu_values, 0, 25)

		time.sleep(0.2)
	except KeyboardInterrupt:
		scrollphat.clear()
		sys.exit(-1)
