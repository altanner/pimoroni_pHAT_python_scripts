#!/usr/bin/env python

import time
import unicodedata
import tweepy
import Queue as queue
from sys import exit
import scrollphathd
from scrollphathd.fonts import font5x7

# rotate
scrollphathd.rotate(degrees=180)

# make less bright
#scrollphathd.set_brightness(0.5)


# adjust the tracked keyword below to your keyword or #hashtag... FOR SOME REASON THIS CANNOT BE A VERY LONG HASHTAG
#keyword = '#softwareengineering'
keyword = '#datascience'

# TWITTER KEYS
# you'll need to add these yourself
consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

if consumer_key == '' or consumer_secret == '' or access_token == '' or access_token_secret == '':
    print("You need to configure your Twitter keys...")
    exit(0)

# make FIFO queue
q = queue.Queue()

# define main loop to fetch formatted tweet from queue
def mainloop():
    scrollphathd.clear()
    scrollphathd.show()

    while True:
        # grab the tweet string from the queue
        try:
            scrollphathd.clear()
            status = q.get(False)
            scrollphathd.write_string(status,font=font5x7, brightness=0.5)
            status_length = scrollphathd.write_string(status, x=0, y=0,font=font5x7, brightness=0.5)
            time.sleep(0.25)

            while status_length > 0:
                scrollphathd.show()
                scrollphathd.scroll(1)
                status_length -= 1
                # scroll speed
                time.sleep(0.006)

            scrollphathd.clear()
            scrollphathd.show()
            time.sleep(0.25)

            q.task_done()

        except queue.Empty:
            time.sleep(1)

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if not status.text.startswith('RT'):
            # format the incoming tweet string
            status = u'   >>>>>   @{name}: {text}     '.format(name=status.user.screen_name.lower(), text=status.text.lower())
            try:
                status = unicodedata.normalize('NFKD', status).encode('ascii', 'ignore')
            except BaseException as e:
                print(e)

            # put tweet into the fifo queue
            q.put(status)

    def on_error(self, status_code):
        print("Error: {}".format(status_code))
        if status_code == 420:
            return False


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

myStream.filter(track=[keyword], stall_warnings=True, is_async=True)

try:
    mainloop()

except KeyboardInterrupt:
    myStream.disconnect()
    del myStream
    print("ok, just a moment, exiting")

