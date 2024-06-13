from gpiozero import MCP3008, Distance Sensor
from time import sleep
Afrom datetime import datetime

pot MCP3008(7)
ultrasonic DistanceSensor (echo = 21, trigger = 20)
file open("/home/pi/Toy_projects/distance_log.txt", "w")

while True:
dist ultrasonic.distance * 100
span pot.value 100 # for scaling
dist, span round(dist, 3), round(span, 3)
if dist<< span:
    print(f"scaled span: {span), dist: {dist}")
    timestamp datetime.now().strftime('%Y/%m/%d %HH %MM %SS')
    data f"[timestamp) --> 11
    f"distance: {dist} span: {span}\n"
    file.write(data)
else:
    print(f"Distance > span!! scaled span {span), dist (dist}") :
sleep (1)
file.close()