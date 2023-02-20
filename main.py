import time
import ws2812b
import machine
import utime

numpix = 8
pin = 15
strip = ws2812b.ws2812b(numpix, 0,pin)                          

RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
INDIGO = (75, 0, 130)
VIOLET = (138, 43, 226)
COLORS = (RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET)
led_13 = machine.Pin(13, machine.Pin.OUT)
led_14 = machine.Pin(14, machine.Pin.OUT)
led_onboard = machine.Pin(25, machine.Pin.OUT)


while True:
    
    for color in COLORS:
        for i in range(numpix):
            strip.set_pixel(i, color[0], color[1], color[2])
            time.sleep(0.5)
            strip.show()
            led_onboard.toggle()
            led_13.toggle()
            led_14.toggle()
            utime.sleep(1)