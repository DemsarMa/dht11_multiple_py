#!/usr/bin/python
from difflib import diff_bytes
from time import sleep
from dotenv import load_dotenv
from pathlib import Path
from multiprocessing import Process
import os
import sys
import Adafruit_DHT

sens1 = Adafruit_DHT.DHT11(4)
sens2 = Adafruit_DHT.DHT11(14)
sens3 = Adafruit_DHT.DHT11(15)
sens4 = Adafruit_DHT.DHT11(17)
sens5 = Adafruit_DHT.DHT11(18)
sens6 = Adafruit_DHT.DHT11(27)

def sens1():
    while True:
        try:
            sens1_temp = sens1.temperature

            print(
                "Temp: {0:0.1f}*C".format(
                    sens1_temp
                )
            )

        except RuntimeError as error:
            print(error.args[0])
            sleep(2.0)
            continue
    
        except Exception as error:
            sens1.exit()
            raise error

        sleep(2.0)

def sens2():
    while True:
        try:
            sens2_temp = sens2.temperature

            print(
                "Temp: {0:0.1f}*C".format(
                    sens2_temp
                )
            )

        except RuntimeError as error:
            print(error.args[0])
            sleep(2.0)
            continue
    
        except Exception as error:
            sens2.exit()
            raise error

        sleep(2.0)

def sens3():
    while True:
        try:
            sens3_temp = sens3.temperature

            print(
                "Temp: {0:0.1f}*C".format(
                    sens3_temp
                )
            )

        except RuntimeError as error:
            print(error.args[0])
            sleep(2.0)
            continue
    
        except Exception as error:
            sens3.exit()
            raise error

        sleep(2.0)

def sens4():
    while True:
        try:
            sens4_temp = sens4.temperature

            print(
                "Temp: {0:0.1f}*C".format(
                    sens4_temp
                )
            )

        except RuntimeError as error:
            print(error.args[0])
            sleep(2.0)
            continue
    
        except Exception as error:
            sens4.exit()
            raise error

        sleep(2.0)

def sens5():
    while True:
        try:
            sens5_temp = sens5.temperature

            print(
                "Temp: {0:0.1f}*C".format(
                    sens5_temp
                )
            )

        except RuntimeError as error:
            print(error.args[0])
            sleep(2.0)
            continue
    
        except Exception as error:
            sens5.exit()
            raise error

        sleep(2.0)

def sens6():
    while True:
        try:
            sens6_temp = sens6.temperature

            print(
                "Temp: {0:0.1f}*C".format(
                    sens6_temp
                )
            )

        except RuntimeError as error:
            print(error.args[0])
            sleep(2.0)
            continue
    
        except Exception as error:
            sens6.exit()
            raise error

        sleep(2.0)

def sens1warn():
    if sens1.temperature >= int(os.getenv('WARNING_TEMP')):
        print("Sensor 1 has reached over 60*C!")

def sens2warn():
    if sens2.temperature >= int(os.getenv('WARNING_TEMP')):
        print("Sensor 2 has reached over 60*C!")

def sens3warn():
    if sens3.temperature >= int(os.getenv('WARNING_TEMP')):
        print("Sensor 3 has reached over 60*C!")

def sens4warn():
    if sens4.temperature >= int(os.getenv('WARNING_TEMP')):
        print("Sensor 4 has reached over 60*C!")

def sens5warn():
    if sens5.temperature >= int(os.getenv('WARNING_TEMP')):
        print("Sensor 5 has reached over 60*C!")

def sens6warn():
    if sens6.temperature >= int(os.getenv('WARNING_TEMP')):
        print("Sensor 6 has reached over 60*C!")

def sens1crit():
    if sens1.temperature >= int(os.getenv('CRIT_TEMP')):
        print("Sensor 1 has reached over 70*C!")

def sens2crit():
    if sens2.temperature >= int(os.getenv('CRIT_TEMP')):
        print("Sensor 2 has reached over 70*C!")

def sens3crit():
    if sens3.temperature >= int(os.getenv('CRIT_TEMP')):
        print("Sensor 3 has reached over 70*C!")

def sens4crit():
    if sens4.temperature >= int(os.getenv('CRIT_TEMP')):
        print("Sensor 4 has reached over 70*C!")

def sens5crit():
    if sens5.temperature >= int(os.getenv('CRIT_TEMP')):
        print("Sensor 5 has reached over 70*C!")

def sens6crit():
    if sens6.temperature >= int(os.getenv('CRIT_TEMP')):
        print("Sensor 6 has reached over 70*C!")

if __name__ == '__main__':

    proc1 = Process(target=sens1)
    proc1.start()

    proc2 = Process(target=sens2)
    proc2.start()

    proc3 = Process(target=sens3)
    proc3.start()

    proc4 = Process(target=sens4)
    proc4.start()

    proc5 = Process(target=sens5)
    proc5.start()

    proc6 = Process(target=sens6)
    proc6.start()

    proc7 = Process(target=sens1warn)
    proc7.start()

    proc8 = Process(target=sens2warn)
    proc8.start()

    proc9 = Process(target=sens3warn)
    proc9.start()

    proc10 = Process(target=sens4warn)
    proc10.start()

    proc11 = Process(target=sens5warn)
    proc11.start()
    
    proc12 = Process(target=sens6warn)
    proc12.start()

    proc13 = Process(target=sens1crit)
    proc13.start()

    proc14 = Process(target=sens2crit)
    proc14.start()

    proc15 = Process(target=sens3crit)
    proc15.start()

    proc16 = Process(target=sens4crit)
    proc16.start()

    proc17 = Process(target=sens5crit)
    proc17.start()
    
    proc18 = Process(target=sens6crit)
    proc18.start()