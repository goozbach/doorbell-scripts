#!/usr/bin/env python

import RPi.GPIO as GPIO
import urllib

from time import sleep
mypins = [ 16, 18 ]
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(mypins, GPIO.IN)
prev_foo=1
prev_bar=1
while True:
  foo = GPIO.input(16)
  if ((prev_foo) and (foo == 0)):
    print "front pressed"
    urllib.urlopen('http://localhost/api/v0.1/ring_chime/front')
  prev_foo = foo
  bar = GPIO.input(18)
  if ((prev_bar) and (bar == 0)):
    print "back pressed"
    urllib.urlopen('http://localhost/api/v0.1/ring_chime/back')
  prev_bar = bar
  sleep(0.05)

