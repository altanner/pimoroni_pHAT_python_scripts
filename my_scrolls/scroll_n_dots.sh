#!/bin/bash

while true
do
    length_of_time=`shuf -i 10-45 -n 1`;
    timeout $length_of_time python /home/pi/Pimoroni/scrollphat/my_scrolls/dots_crash.py;
    python /home/pi/Pimoroni/scrollphat/my_scrolls/scroll_rand_1line.py;
done
