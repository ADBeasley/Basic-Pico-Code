# Control dual colour LED

from machine import Pin

YGOff    = 0
YGYellow = 1
YGGreen  = 2
YGError  = 3

class YGColourLED:
    
    def __init__(self, yellow, green, initial = YGOff):

        self.YellowPin = Pin(yellow, Pin.OUT, value=0)
        self.GreenPin = Pin(green, Pin.OUT, value=0)
        
        if initial == YGOff:
            self.TurnOff()
        elif initial == YGYellow:
            self.TurnYellow()
        elif initial == YGGreen:
            self.TurnGreen()
        else:
            raise ValueError('Undefined starting state.')
    
    def TurnOff(self):
        self.status = YGOff
#         print('Turning off')
        try:
            self.YellowPin.low()
            self.GreenPin.low()
        except:
            self.status = YGError
            raise RuntimeError('Error setting LED off')
            
    
    def TurnYellow(self):
        self.status = YGYellow
#         print('Turning yellow')
        try:
            self.YellowPin.high()
            self.GreenPin.low()
        except:
            self.status = YGError
            raise RuntimeError('Error setting LED to yellow')            
    
    def TurnGreen(self):
        self.status = YGGreen
#         print('Turning green')
        try:
            self.YellowPin.low()
            self.GreenPin.high()
        except:
            self.status = YGError
            raise RuntimeError('Error setting LED off')
        
    def Invert(self):
        if self.status == YGYellow:
#             print('Going to Green')
            self.TurnGreen()
        elif self.status == YGGreen:
#             print('Going to Yellow')
            self.TurnYellow()
        else:
            raise RuntimeError('Cannot invert an off LED')
    