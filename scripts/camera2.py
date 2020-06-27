 #!/usr/bin/env python3
import pygame
import pygame.camera
from pygame.locals import *
import numpy as np
import sys
import board
import neopixel
import time
import numpy as np
import gi

def convert(image, pixelval):
  color = image.unmap_rgb(pixelval)
  return (color[0], color[1], color[2])

def main():
  board_pin = board.D18
  pixel_num = 60
  pixels = neopixel.NeoPixel(board_pin, pixel_num)
  pixel_array = np.zeros((60,3),dtype=np.uint8)
  pixels.fill(0)
  duration = 20 #in seconds


  pygame.init()
  pygame.camera.init()

  cam = pygame.camera.Camera("/dev/video0", (1920,1080))
  cam.start()

  for i in range(0,250000):
    image = cam.get_image()
    array = pygame.PixelArray(image)
    for j in range(0,59):
      pixels[j] = convert(image, array[1000, int(1080/60)*j])
    # time.sleep(1)

  cam.stop()

if __name__ == '__main__':
    main()