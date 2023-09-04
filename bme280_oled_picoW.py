from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time
import bme280
sdaPIN=Pin(2)
sclPIN=Pin(3)
i2c=machine.I2C(1,sda=sdaPIN, scl=sclPIN, freq=400000)
bme = bme280.BME280(i2c=i2c)
WIDTH =128 
HEIGHT= 64
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)
while True:
    t, p, h = bme.read_compensated_data()
    temperature=t/100
    p = p // 256
    pressure = p // 100
    hi = h // 1024
    hd = h * 100 // 1024 - hi * 100
    print ("{}C".format(temperature), "{}hPa".format(pressure),
            "{}.{:02d}%".format(hi, hd))
    oled.text("Temp:", 0, 0)
    oled.text(str(temperature), 80, 0)
    oled.text("Pressure:", 0, 20)
    oled.text(str(pressure), 80, 20)
    oled.text("Humidity:", 0, 40)
    oled.text(str(hi), 80, 40)
    oled.show()
    time.sleep(1)
    oled.fill(0)
