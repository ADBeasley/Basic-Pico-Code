# I2C Scanner
from machine import Pin, I2C

# Use GPxx as pin ID
# Power + GND
# SDA -> Data 
# SCL -> Clock

# Pin out of tiny display looking from bottom (i.e. screen face down)

#      Gxx - G = GND
#      LA3 - L = scl, A = SDA, 3 = 3v3
# ########
# ########
# For tiny display - address should come back as 0x3C


# Note - have to specificy I2C bus (0 or 1) to match the pins being used
i2c = I2C(0, scl=Pin(1), sda=Pin(0))

print('I2C SCANNER')
devices = i2c.scan()

if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:', len(devices))

  for device in devices:
    print("I2C hexadecimal address: ", hex(device))
    