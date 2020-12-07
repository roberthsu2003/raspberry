#!/usr/bin/python

import bluetooth
import time
from lcd_display import lcd

d = lcd()
d.clear()
d.display_string("Who's Home?", 1)

sleep_time = 600

while True:
    string = ''

    result = bluetooth.lookup_name('1C:66:AA:CF:DD:35', timeout=5)
    if (result != None):
        string = string + ' Dad'
    d.display_string(string, 2)

    result = bluetooth.lookup_name('94:3A:F0:63:2D:99', timeout=5)
    if (result != None):
        string = string + ' Mum'
    d.display_string(string, 2)

    result = bluetooth.lookup_name('34:BB:1F:39:DE:12', timeout=5)
    if (result != None):
        string = string + ' Sophie'
    d.display_string(string, 2)

    f = open('whoshome.log', 'a')
    f.write(time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()) + string + '\n')
    f.close()

    time.sleep(sleep_time)
