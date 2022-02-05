#!/usr/bin/python
from difflib import diff_bytes
from time import sleep
from multiprocessing import Process
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

            print (
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

            print (
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

            print (
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

            print (
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

            print (
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

            print (
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