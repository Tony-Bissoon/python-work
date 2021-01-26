from gpiozero import Button, LED
from signal import pause

import time

button = Button(4)

red_light = LED(14)
yellow_light = LED(15)
green_light = LED(18)

def start_lights():
    red_light.on()
    time.sleep(1.5)
    red_light.off()
    time.sleep(1)

    yellow_light.on()
    time.sleep(1.5)
    yellow_light.off()
    time.sleep(1)

    green_light.on()
    time.sleep(1.5)
    green_light.off()
    time.sleep(1)
button.when_pressed = start_lights

pause()



