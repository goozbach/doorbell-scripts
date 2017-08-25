#!/usr/bin/env python

from flask import Flask, jsonify
import RPi.GPIO as GPIO
from time import sleep

mypins = [ 11, 13 ]
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(mypins, GPIO.OUT, initial=GPIO.LOW)

app = Flask(__name__)

mydoors = ['front', 'back', 'side']
doornum = { 'front': 11, 'back': 13 }
@app.route('/api/v0.1/ring_chime/<string:door>', methods=["Get"])

def ring_chime(door):
    print door
    if door not in mydoors:
        retobj = { 'status': 'fail', 'msg': 'door does not exist', 'door': door}
    else:
        GPIO.output(doornum[door],GPIO.HIGH)
        sleep(1)
        GPIO.output(doornum[door],GPIO.LOW)
        retobj = { 'status': 'success', 'ringing': door }
    return jsonify(retobj)


if __name__ == '__main__':
    app.run(debug=True)
    GPIO.cleanup()
