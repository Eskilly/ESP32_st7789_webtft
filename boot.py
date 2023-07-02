try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'DESKTOP-RP2SCQP4177'
password = 'www12345687'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)
import time
time.sleep(3)
if station.isconnected() == False:
  import web_wifi

print('Connection successful')
print(station.ifconfig())
