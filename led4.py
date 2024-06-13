from gpiozero import LED
from time import sleep

leed={
    "red": LED(5),
    "yellow": LED(6),
    "green":LED(13)
}
while True:
    for i in led.keys():
        led[i].blink(on_time=1,off_time=1)
        sleep(2)
