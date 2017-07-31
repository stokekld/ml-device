from flask import render_template, jsonify
from Mist.app import service
from mistlogic.tools import *

@service.route('/manual')
def manual():
    commandExe('bash /etc/mistlogic/gpio/gpioctl.sh manual toggle')
    return jsonify(state=True)

