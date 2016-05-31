#!/usr/bin/env python

from flask import Flask, render_template
import unicornhat as unicorn
import time, os, stat, threading
from UHScroll import unicorn_scroll
from playIcon import playIcon

app = Flask(__name__)
loops = 4
brightness = 0.3

@app.route('/')
def home():
	return 'ready'

@app.route('/message/<message>')
def message(message):
    unicorn.rotation(270)
    for _ in range(loops):
        unicorn_scroll(message,'red',255,0.1)
    unicorn.clear()
    unicorn.show()
    return "ok"

@app.route('/icon/<icon>')
def icon(icon):
    unicorn.rotation(90)
    for _ in range(loops):
        playIcon(icon)
    unicorn.clear()
    unicorn.show()
    return "ok"

if __name__ == "__main__":
    unicorn.brightness(brightness)
    app.run(host='0.0.0.0', debug=True)
