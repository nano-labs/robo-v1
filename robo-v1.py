import os
import serial
import pygame
from pygame.locals import *

os.putenv('DISPLAY', ':0.0')
pygame.init()
pygame.display.set_mode((1, 1))

with serial.Serial('/dev/ttyUSB0', 9600, timeout=1) as ser:
#with serial.Serial('/dev/cu.usbserial-A900abSe', 9600, timeout=1) as ser:

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                ser.write(chr(event.key))
                print "down ", event.key
            if event.type == pygame.KEYUP:
                ser.write(chr(event.key).upper())
                print "up ", event.key
