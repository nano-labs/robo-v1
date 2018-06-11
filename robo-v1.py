import os
from time import sleep
from datetime import datetime
import serial
import pygame
from pygame.locals import *
import traceback

reboot_signal = [datetime.now(), 0]
shutdown_signal = [datetime.now(), 0]
while True:
    try:
        os.putenv('DISPLAY', ':0.0')
        pygame.init()
        pygame.display.set_mode((1, 1))

        with serial.Serial('/dev/ttyUSB0', 9600, timeout=1) as ser:
        # with serial.Serial('/dev/cu.usbserial-A900abSe', 9600, timeout=1) as ser:

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        # ser.write(chr(event.key))
                        print "down ", event.key
                        if chr(event.key) == "r":
                            if (datetime.now() - reboot_signal[0]).total_seconds() <= 3:
                                reboot_signal[1] += 1
                            else:
                                reboot_signal = [datetime.now(), 0]
                            if reboot_signal[1] >= 3:
                                print "reboot"
                                os.system('sudo shutdown -r now')
                        if chr(event.key) == "t":
                            if (datetime.now() - shutdown_signal[0]).total_seconds() <= 3:
                                shutdown_signal[1] += 1
                            else:
                                shutdown_signal = [datetime.now(), 0]
                            if shutdown_signal[1] >= 3:
                                print "shutdown"
                                os.system('sudo shutdown -h now')

                    if event.type == pygame.KEYUP:
                        # ser.write(chr(event.key).upper())
                        print "up ", event.key
    except:
        trace = traceback.format_exc()
        print trace
        log = open("/home/pi/robo.log", "a")
        log.write("{}\n".format(trace))
        log.close()
        sleep(5)

