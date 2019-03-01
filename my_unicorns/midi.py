import unicornhat as uh
import time
import serial
import random
from random import randint

uh.set_layout(uh.PHAT)
uh.brightness(0.5)

ser = serial.Serial('/dev/ttyAMA0', baudrate=38400) #original    
#ser = serial.Serial('/dev/ttyAMA0') # bens first one, doesnt seem to work
#ser = serial.Serial('/dev/ttyAMA0', baudrate=31250) #sees program change?
#ser = serial.Serial('/dev/ttyAMA0', baudrate=38400) # my try on jani comment

message = [0, 0, 0]
while True:
  i = 0
  while i < 3:
    data = ord(ser.read(1)) # read a byte
    if data != 240: # i think 240 is the bpm?
      print data # me
    if data == 14 or data == 142:
      for y in range(4):
        for x in range(8):
          uh.set_pixel(x,y,randint(0,255),randint(0,255),randint(0,255))
      uh.show()
    if data == 206:
      for y in range(4):
        for x in range(8):
          uh.set_pixel(x,y,255,255,255)
        uh.show()
      
#    if data >> 7 != 0:  
#      i = 0      # status byte!   this is the beginning of a midi message!
#    message[i] = data
#    i += 1
#    if i == 2 and message[0] >> 4 == 12:  # program change: don't wait for a
#      message[2] = 0                      # third byte: it has only 2 bytes
#      i = 3#

#  messagetype = message[0] >> 4
#  messagechannel = (message[0] & 15) + 1
#  note = message[1] if len(message) > 1 else None
#  velocity = message[2] if len(message) > 2 else None

#  if messagetype == 9:    # Note on
#    print 'Note on'
#  elif messagetype == 8:  # Note off
#    print 'Note off'            
#  elif messagetype == 12: # Program change
#    print 'Program change'
