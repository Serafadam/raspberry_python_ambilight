import pygame
import pygame.camera
from pygame.locals import *
import time

pygame.init()
pygame.camera.init()
display = pygame.display.set_mode((1920,1080), 0)

cam = pygame.camera.Camera("/dev/video0", (1920,1080))
cam.start()
for i in range(0,25):
    image = cam.get_image()
    display.blit(image, (0,0))
    pygame.display.flip()

print(image.get_view())

cam.stop()