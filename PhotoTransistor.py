import machine
from time import sleep

lightSensor = machine.ADC(26) # Setup the analogue (A0) on GP26 with a human-readable name

try:
    while True:
      # First read the light value on the analog input
      lightValue = lightSensor.read_u16()
      print(f"Light Level {lightValue:>5}")
      sleep(10)
      
except (KeyboardInterrupt):
    pass
