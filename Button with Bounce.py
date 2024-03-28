from machine import Pin
from time import sleep

btn = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_UP)

def btn_handler(pin):
    
    if pin is btn:
        print("Button Pressed")
        sleep(1)
        
btn.irq(trigger = machine.Pin.IRQ_RISING, handler = btn_handler)

while True:
    sleep(0.1)
    