import DualColourLED
from time import sleep

myLED = DualColourLED.YGColourLED(14,15)

sleep(1)
myLED.TurnYellow()

sleep(1)
myLED.TurnGreen()

sleep(1)
myLED.Invert()

sleep(1)
myLED.Invert()

sleep(1)
myLED.TurnOff()
