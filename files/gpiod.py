from mistlogic.gpio import Gpio
from wiringX import gpio as wx
import atexit
import os

wx.setup()

gpio = Gpio({
    'manual': {
        'value': wx.LOW,
        'pin': 17
        },
    'auto': {
        'value': wx.LOW,
        'pin': 27
        }
    })

gpio.declare()

thefifo = '/etc/mistlogic/gpio.fifo'

os.mkfifo(thefifo)

def cleanup():
    os.remove(thefifo)
atexit.register(cleanup)

while True:
    with open(thefifo, 'r') as fifo:
        for line in fifo:
            name, value = line.strip().split(',')

            if value not in ['high', 'low', 'toggle']:
                print "No se encuentra la opcion " + value
                continue

            if value == "high":
                gpio.high(name)
            elif value == "low":
                gpio.low(name)
            elif value == "toggle":
                gpio.toggle(name)
            else:
                pass
