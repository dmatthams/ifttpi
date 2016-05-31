#!/usr/bin/env python

from flask import Flask, render_template
import unicornhat as unicorn
import time, os, stat, threading
from UHScroll import unicorn_scroll

app = Flask(__name__)

@app.route('/')
def home():
	return 'ready'

@app.route('/message/<message>')
def message(message):
    unicorn_scroll(message,'red',255,5)
    return "ok"

@app.route('/icon/<icon>')
def icon():
	s = threading.Thread(None,unicorn.show)
	s.start()
	return "ok"

if __name__ == "__main__":
    unicorn.brightness(0.3)
    unicorn.rotation(90)
	app.run(host='0.0.0.0', debug=True)
