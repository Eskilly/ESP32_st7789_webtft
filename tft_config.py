from machine import Pin, SPI
import st7789

TFA = 0
BFA = 0

def config(rotation=0, buffer_size=0, options=0):
    return st7789.ST7789(
        SPI(2, baudrate=40000000,polarity=1, sck=Pin(18), mosi=Pin(23)),
        240,
        240,
        reset=Pin(4, Pin.OUT),
        dc=Pin(2, Pin.OUT),
        backlight=Pin(5, Pin.OUT),
        rotation=rotation,
        options=options,
        buffer_size=buffer_size)