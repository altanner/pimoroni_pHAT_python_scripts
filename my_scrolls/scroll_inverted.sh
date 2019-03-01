#!/bin/bash

while true
do
    length_of_time=`shuf -i 10-30 -n 1`;
    timeout $length_of_time python /home/pi/Pimoroni/scrollphat/my_scrolls/dots_interim.py;
    python /home/pi/Pimoroni/scrollphat/my_scrolls/crash.py
    python /home/pi/Pimoroni/scrollphat/my_scrolls/scroll_rand_1line_inverted.py;
done
