from gpiozero import LED
led_red = LED(10)
while True:
    led_red.on()
