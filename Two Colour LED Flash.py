# BiColour LED example

# LED connected with resistor between the two pins defines in the code.

from machine import Pin
from utime import sleep

# Define pins used for LED
p1 = 14
p2 = 15

# Note that BOTH pins have to be defined as outputs for this to work
# Defining either one as an input will not work

pin1 = Pin(p1, Pin.OUT, value=0)
pin2 = Pin(p2, Pin.OUT, value=0)

try:
    while True:
        pin1.toggle()
        pin2.value(not pin1.value())
        sleep(0.5)
    
except (KeyboardInterrupt):
        pin1.low()
        pin2.low()
        print("Stop pressed")
