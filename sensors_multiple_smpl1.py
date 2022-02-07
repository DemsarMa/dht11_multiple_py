#!/usr/bin/python
from difflib import diff_bytes
from time import sleep
from dotenv import load_dotenv
from pathlib import Path
from multiprocessing import Process
import os
import sys
import Adafruit_DHT


class Sensor:

    def __init__(self, id ,pin):
        self.id = id
        self.sensor =  Adafruit_DHT.DHT11(pin)

    def read_temp():
        return self.sensor.temperature
    
    def exit():
        self.sensor.exit()

sensors = [
    Sensor(1,4),
    Sensor(2,14),
    Sensor(3,15),
    Sensor(4,17),
    Sensor(5,18),
    Sensor(6,27)
]

def read_sensor(sensor):
    while True:
        try:
            temp = sensor.read_temp()
            print(f"Temp: {temp:0.1f}*C")

            if temp >= int(os.getenv('WARNING_TEMP')):
                    print("Sensor {sensor.id} has reached over 60*C!")
            elif temp >= int(os.getenv('CRIT_TEMP')):
                    print("Sensor {sensor.id} has reached over 70*C!")

        except RuntimeError as error:
            print(error.args[0])
            sleep(2.0)
            continue

        except Exception as error:
            sensor.exit()
            raise error

        sleep(2.0)


def main():
    for sensor in sensors:
        proc = Process(target=read_sensor,args=sensor)
        proc.start()

if __name__ == '__main__':
    main()