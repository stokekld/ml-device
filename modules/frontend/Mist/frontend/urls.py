from flask import render_template
from Mist.app import service
from mistlogic.config import *

gpio = Config('gpio', {})

@service.route('/')
def index():
    return render_template('index.html', error={})

@service.route('/equipo')
def equipo():
    prop = gpio.getProp('manual')
    manual = ''

    if prop['value']:
        manual = "checked"
    return render_template('equipo.html', manual = manual);
