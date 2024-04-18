import network
from time import sleep

import DualColourLED
from secrets import wifiHOST, wifiSSID, wifiPWD

myLED = DualColourLED.YGColourLED(14,15)
myLED.TurnYellow()
sleep(1)

network.hostname(wifiHOST)

wlan = network.WLAN(network.STA_IF)

wlan.active(True)

# nets = wlan.scan()
# print('The networks are:', *nets, sep='\n')

wlan.connect(wifiSSID, wifiPWD)

wlan_wait = 10
while wlan_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wlan_wait -= 1
    print('Waiting for connection...')
    myLED.TurnOff()
    sleep(0.25)
    myLED.TurnYellow()
    sleep(0.5)

if wlan.status() != 3:
    raise RuntimeError('Network connection failed')
else:
    print('WiFi connected')
    wlan_status = wlan.ifconfig()
    print(f'Network Status is {wlan_status}')
    myLED.TurnGreen()

try:
    while True:
        sleep(0.1)
except KeyboardInterrupt:
    myLED.TurnOff()
    wlan.disconnect()
    wlan.active(False)
