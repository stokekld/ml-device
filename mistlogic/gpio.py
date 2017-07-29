from mistlogic.config import *
from wiringX import gpio as wx

class Gpio(object):
    def __init__(self, props):
        self.__props = props
        self.__gpio = Config('gpio', props)
    
    def declare(self):
        
        for key in self.__props:
            prop = self.__gpio.getProp(key)
            wx.pinMode(prop['pin'], wx.OUTPUT)
            wx.digitalWrite(prop['pin'], prop['value'])

    def setValue(self, name, value):
        prop = self.__props[name]
        prop['value'] = value
        wx.digitalWrite(prop['pin'], value)
        self.__gpio.setProp(name, prop)

    def high(self, name):
        self.setValue(name, GPIO.HIGH)

    def low(self, name):
        self.setValue(name, GPIO.LOW)

    def toggle(self, name):
        prop = self.__props[name]

        if prop['value']:
            self.low(name)
        else:
            self.high(name)






