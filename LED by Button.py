from machine import Pin
from time import sleep, ticks_ms, ticks_diff

led = Pin("LED", Pin.OUT)
btn = Pin(18, Pin.IN, Pin.PULL_UP)

LEDLastOn = ticks_ms()

def btn_handler(PinID):
    global LEDLastOn
    
    if (PinID is btn) and \
       (ticks_diff(ticks_ms(), LEDLastOn) > 500):
        LEDLastOn = ticks_ms()
        led.toggle()
        

btn.irq(trigger = Pin.IRQ_RISING, handler = btn_handler)

while True:
    sleep(0.1)