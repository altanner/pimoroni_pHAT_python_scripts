# get everything and put it in boomkat_output_file
wget -O - http://boomkat.com | grep -A1 '\(release__artist\|release__title\|release__label\)' > /home/pi/Pimoroni/scrollphat/my_scrolls/boomkat_output_file

# remove empty lines
sed -i '/^$/d' /home/pi/Pimoroni/scrollphat/my_scrolls/boomkat_output_file

# remove whitespace
sed -i 's/^[ \t]*//;s/[ \t]*$//' /home/pi/Pimoroni/scrollphat/my_scrolls/boomkat_output_file

# remove -- lines
sed -i '/--/d' /home/pi/Pimoroni/scrollphat/my_scrolls/boomkat_output_file

# remove html lines
sed -i '/</d' /home/pi/Pimoroni/scrollphat/my_scrolls/boomkat_output_file

# add hyphens
sed -i 's/$/  - /' /home/pi/Pimoroni/scrollphat/my_scrolls/boomkat_output_file

# link three lines at a time
sed -i -e 'N;N;s/\n/ /g' /home/pi/Pimoroni/scrollphat/my_scrolls/boomkat_output_file

# remove trailing hyphens
sed -i 's/  - $//' /home/pi/Pimoroni/scrollphat/my_scrolls/boomkat_output_file

# clean ampersands
sed -i 's/&amp;/\&/' /home/pi/Pimoroni/scrollphat/my_scrolls/boomkat_output_file

# clean single quotes
sed -i "s/&#39;/'/" /home/pi/Pimoroni/scrollphat/my_scrolls/boomkat_output_file
