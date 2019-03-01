#!/bin/bash

while true
do
    length_of_time=`shuf -i 60-120 -n 1`;
    timeout $length_of_time python /home/pi/Pimoroni/scrollphat/my_scrolls/sine2.py;
    python /home/pi/Pimoroni/scrollphat/my_scrolls/crash.py
    sh boomkat_retreive.sh
    python /home/pi/Pimoroni/scrollphat/my_scrolls/scroll_boomkat_inverted.py;
done
