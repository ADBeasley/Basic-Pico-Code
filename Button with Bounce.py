from machine import Pin
from time import sleep

btn = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_UP)
btnCount = 0

def btn_handler(pin):

    global btnCount
    btnCount += 1
    
    if pin is btn:
        print(f"Button pressed {btnCount:>2}")
        sleep(1)
        
btn.irq(trigger = machine.Pin.IRQ_RISING, handler = btn_handler)

while True:
    sleep(0.1)
    