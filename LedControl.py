import sys
import board
import neopixel
import time


class LedControl(object):
    def __init__(self):
        self.board_pin = board.D18
        self.pixel_num = 60
        self.pixels = neopixel.NeoPixel(self.board_pin, self.pixel_num)

    def pixel_rotation(self):
        for i in range(0,self.pixel_num):
            self.pixels[i] = (4*i,0,4*i)
            if i %2 == 0:
                self.pixels[i] = (4*i,4*i,0)
            if i %3 == 0:
                self.pixels[i] = (0,4*i,4*i)

    def turn_off(self):
        self.pixels.fill(0)


if __name__ == '__main__':
    led_controller = LedControl()
    led_controller.turn_off()
    for i in range(0,15):
        led_controller.pixel_rotation()
        led_controller.turn_off()