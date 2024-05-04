import network
from time import sleep
from umqtt.simple import MQTTClient

import DualColourLED
from secrets import wifiHOST, wifiSSID, wifiPWD

def mqtt_connect():
    client = MQTTClient(client_id, mqtt_server, keepalive=3600)
    client.connect()
    print('Connected to %s MQTT Broker'%(mqtt_server))
    return client

def reconnect():
    print('Failed to connect to the MQTT Broker. Reconnecting...')
    time.sleep(5)
    machine.reset()

#  mqtt_server and client_id are global variables used in the conenct function!    
mqtt_server = '10.21.1.22'
client_id = wifiHOST

# Topics and standard messages
DevStatTopic = b'TEST/Device/Info/' + wifiHOST
LightLevelTopic = b'TEST/House/Hall/Light'
DevUpMsg = b'{"Status":"Up"}'
DevDownMsg = b'{"Status":"Down"}'

lightSensor = machine.ADC(26)

myLED = DualColourLED.YGColourLED(14,15)
myLED.TurnYellow()
sleep(1)

network.hostname(wifiHOST)

wlan = network.WLAN(network.STA_IF)

wlan.active(True)

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
#    print(f'Network Status is {wlan_status}')
    myLED.TurnGreen()

try:
    client = mqtt_connect()
except OSError as e:
    reconnect()

try:
    client.publish(DevStatTopic, DevUpMsg)
except:
    print("Initial status publish error")

myLED.TurnOff()

try:
    while True:
      lightValue = lightSensor.read_u16()
#      print(f"Light Level {lightValue:>5}")
      data_msg = b'{"Level":' + str(lightValue) + b'}'
      client.publish(LightLevelTopic, data_msg)
      sleep(20)
    
except KeyboardInterrupt:
    try:
        client.publish(DevStatTopic, DevDownMsg)
    except:
        print("Final status publish error")

wlan.disconnect()
wlan.active(False)
