#!/usr/bin/env python

from flask import Flask, render_template
import unicornhat as unicorn
import time, os, stat, threading
from UHScroll import unicorn_scroll
from playIcon import playIcon

app = Flask(__name__)
loops = 4

@app.route('/')
def home():
	return 'ready'

@app.route('/message/<message>')
def message(message):
    for _ in range(loops):
        unicorn_scroll(message,'red',255)
    return "ok"

@app.route('/icon/<icon>')
def icon(icon):
    for _ in range(loops):
        playIcon(icon)
    unicorn.clear()
    unicorn.show()
    return "ok"

if __name__ == "__main__":
    unicorn.brightness(1)
    # unicorn.rotation(270)
    app.run(host='0.0.0.0', debug=True)
