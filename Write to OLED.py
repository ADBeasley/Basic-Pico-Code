# Test message on Tiny OLED screen

from machine import Pin, I2C
from time import sleep

import ssd1306

# Note screen is assumed to be at 0x3c - look to use SoftI2C if it is not.
i2c = I2C(0, scl=Pin(1), sda=Pin(0))

oled_width = 128
oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('Hello, World!', 0, 0)
oled.text('Hellord!', 0, 10)

oled.show()

#######################################################
# WARNING - After poweroff() you cannot power back on #
#           with the poweron() function - you have to #
#           use the init_display() function           #
#           Creating the OLED object runs the init so #
#           you do not need to init at the end of the #
#           program for the next time :-)             #
#######################################################

# Clear the screen by turning it off.
sleep(2)
oled.poweroff()

# Power the screen back up and display new text
sleep(2)
oled.init_display()
oled.text("New text", 0, 0)
oled.show()

# Turnthe screen off at the end else it will stay showing the last message
sleep(2)
oled.poweroff()
