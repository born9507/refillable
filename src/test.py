# example.py 참고
import time
import sys
import RPi.GPIO as GPIO
from hx711 import HX711


def cleanAndExit():
    print()
    print("Cleaning...")
    GPIO.cleanup()
    print("Bye!")
    sys.exit()



hx = HX711(5, 6)
hx.set_reading_format("MSB", "MSB")
# hx.set_reference_unit(referenceUnit)
hx.reset()
# hx.tare()

m = 230
b = 54300

weights = []
while True:
    try:
        # y = mx + b -> x = (y - b) / m
        val = hx.get_weight(5)
        weight = (val - b) / m
        weight = round(weight)
        print(weight)

        hx.power_down()
        hx.power_up()
        time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()

# print("mean: ",sum(weights)/len(weights))
cleanAndExit()
