from machine import Pin
from time import sleep

led = machine.Pin("LED", machine.Pin.OUT)


while True:
    sleep(0.5)
    led.on()
    sleep(0.5)
    led.off()

