import pygame
import sys
import time
import serial
from matplotlib import pyplot as plt

if __name__ == "__main__":
  pygame.init()
  pygame.display.set_mode((400, 400), 0, 8)
  outSerial = serial.Serial("/dev/ttyUSB0", 115200)
  roll = 0.0
  pitch = 0.0
  yaw = 0.0
  thrust = 0.0
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_0:
          thrust = 0.0
        if event.key == pygame.K_1:
          thrust = 0.1
        if event.key == pygame.K_2:
          thrust = 0.2
        if event.key == pygame.K_3:
          thrust = 0.3
        if event.key == pygame.K_4:
          thrust = 0.4
        if event.key == pygame.K_5:
          thrust = 0.5
    outString = str(int(127+roll*127))+" "+str(int(127+pitch*127))+" "+str(int(127+yaw*127))+" "+str(int(0+thrust*255))+"\n"
    print outString
    outSerial.write(outString)
    time.sleep(1e-1)
