# RPLCD library by Danilo Bargen
# http://rplcd.readthedocs.io/
# Test script by Michael Horne
# Accompanies blog post at http://www.recantha.co.uk/blog/?p=18467

# Import libraries
from RPLCD import i2c
from time import sleep

# Set-up some constants to initialise the LCD
lcdmode = 'i2c'
cols = 16
rows = 2
charmap = 'A00'
i2c_expander = 'PCF8574'
address = 0x3f # If you don't know what yours is, do i2cdetect -y 1
port = 1 # 0 on an older Pi

# Initialise the LCD
lcd = i2c.CharLCD(i2c_expander, address, port=port, charmap=charmap,
                  cols=cols, rows=rows)

# Write a string, wait 5 seconds, turn the backlight off and clear the display
lcd.write_string('Hello world')
sleep(5)
lcd.backlight_enabled = False
lcd.close(clear=True)

