#!/usr/bin/python
from difflib import diff_bytes
from time import sleep
from dotenv import load_dotenv
from pathlib import Path
from multiprocessing import Process
import os
import sys
import Adafruit_DHT
import paramiko

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
                f"Temp: {sens1_temp:0.1f}*C"
            )

            if sens1.temperature >= int(os.getenv('WARNING_TEMP')):
                print("Sensor 1 has reached over 60*C!")
            elif sens1.temperature >= int(os.getenv('CRIT_TEMP')):
                print("Sensor 1 has reached over 70*C!")
                ssh = paramiko.SSHClient()
                ssh.connect(int(os.getenv("SENS1_IP")), int(os.getenv("SENS1_USER")), int(os.getenv("SENS1_PASS")))
                stdin, stdout, stderr = ssh.exec_command("/usr/bin/poweroff")

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
                f"Temp: {sens2_temp:0.1f}*C"
            )

            if sens2.temperature >= int(os.getenv('WARNING_TEMP')):
                print("Sensor 2 has reached over 60*C!")
            elif sens2.temperature >= int(os.getenv('CRIT_TEMP')):
                print("Sensor 2 has reached over 70*C!")
                ssh = paramiko.SSHClient()
                ssh.connect(int(os.getenv("SENS2_IP")), int(os.getenv("SENS2_USER")), int(os.getenv("SENS2_PASS")))
                stdin, stdout, stderr = ssh.exec_command("/usr/bin/poweroff")

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
                f"Temp: {sens3_temp:0.1f}*C"
            )

            if sens3.temperature >= int(os.getenv('WARNING_TEMP')):
                print("Sensor 3 has reached over 60*C!")
            elif sens3.temperature >= int(os.getenv('CRIT_TEMP')):
                print("Sensor 3 has reached over 70*C!")
                ssh = paramiko.SSHClient()
                ssh.connect(int(os.getenv("SENS3_IP")), int(os.getenv("SENS3_USER")), int(os.getenv("SENS3_PASS")))
                stdin, stdout, stderr = ssh.exec_command("/usr/bin/poweroff")

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
                f"Temp: {sens4_temp:0.1f}*C"
            )

            if sens4.temperature >= int(os.getenv('WARNING_TEMP')):
                print("Sensor 4 has reached over 60*C!")
            elif sens4.temperature >= int(os.getenv('CRIT_TEMP')):
                print("Sensor 4 has reached over 70*C!")
                ssh = paramiko.SSHClient()
                ssh.connect(int(os.getenv("SENS4_IP")), int(os.getenv("SENS4_USER")), int(os.getenv("SENS4_PASS")))
                stdin, stdout, stderr = ssh.exec_command("/usr/bin/poweroff")

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
                f"Temp: {sens5_temp:0.1f}*C"
            )

            if sens5.temperature >= int(os.getenv('WARNING_TEMP')):
                print("Sensor 5 has reached over 60*C!")
            elif sens5.temperature >= int(os.getenv('CRIT_TEMP')):
                print("Sensor 5 has reached over 70*C!")
                ssh = paramiko.SSHClient()
                ssh.connect(int(os.getenv("SENS5_IP")), int(os.getenv("SENS5_USER")), int(os.getenv("SENS5_PASS")))
                stdin, stdout, stderr = ssh.exec_command("/usr/bin/poweroff")

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
                f"Temp: {sens6_temp:0.1f}*C"
            )

            if sens6.temperature >= int(os.getenv('WARNING_TEMP')):
                print("Sensor 6 has reached over 60*C!")
            elif sens6.temperature >= int(os.getenv('CRIT_TEMP')):
                print("Sensor 6 has reached over 70*C!")
                ssh = paramiko.SSHClient()
                ssh.connect(int(os.getenv("SENS6_IP")), int(os.getenv("SEN62_USER")), int(os.getenv("SENS6_PASS")))
                stdin, stdout, stderr = ssh.exec_command("/usr/bin/poweroff")

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