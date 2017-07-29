from mistlogic.config import *
import RPi.GPIO as GPIO

class Gpio(object):
    def __init__(self, props):
        self.__props = props
        self.__gpio = Config('gpio', props)
    
    def declare(self):
        
        for key in self.__props:
            prop = self.__gpio.getProp(key)
            GPIO.setup(prop['pin'], GPIO.OUT)
            GPIO.output(prop['pin'], prop['value'])

    def setValue(self, name, value):
        prop = self.__props[name]
        prop['value'] = value
        GPIO.output(prop['pin'], value)
        self.__gpio.setProp(name, prop)

    def high(self, name):
        self.setValue(name, wx.HIGH)

    def low(self, name):
        self.setValue(name, wx.LOW)

    def toggle(self, name):
        prop = self.__props[name]

        if prop['value']:
            self.low(name)
        else:
            self.high(name)






