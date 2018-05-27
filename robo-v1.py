import serial
import pygame
from pygame.locals import *

pygame.init()
with serial.Serial('/dev/cu.usbserial-A900abSe', 9600, timeout=1) as ser:

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                ser.write(chr(event.key))
                print "down ", event.key
            if event.type == pygame.KEYUP:
                ser.write(chr(event.key).upper())
                print "up ", event.key
