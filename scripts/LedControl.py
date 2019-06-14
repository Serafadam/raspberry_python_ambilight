import board
import numpy as np
import neopixel
import rospy
import gi
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk

from raspberry_python_ambilight.msg import LedStrip


class LedControl(object):
    def __init__(self):
        self.node = rospy.init_node('raspberry_ambilight')
        self.board_pin = board.D18
        self.pixel_num = 60
        self.pixels = neopixel.NeoPixel(self.board_pin, self.pixel_num)
        self.pixel_screen_positions = np.arange(0, 1280, 1280 / self.pixel_num)
        self.w = Gdk.get_default_root_window()
        self.pixel_values = np.zeros((60, 3), dtype=np.uint8)
        self.pixel_subscriber = rospy.Subscriber('/raspberry_ambilight/data', LedStrip, self.led_cb)

    def pixel_rotation(self):
        for i in range(0, self.pixel_num):
            self.pixels[i] = (4 * i, 0, 4 * i)
            if i % 2 == 0:
                self.pixels[i] = (4 * i, 4 * i, 0)
            if i % 3 == 0:
                self.pixels[i] = (0, 4 * i, 4 * i)

    def turn_off(self):
        self.pixels.fill(0)

    def get_pixel(self):
        count = 0
        for i in self.pixel_screen_positions:
            pb = Gdk.pixbuf_get_from_window(self.w, i, 500, 1, 1)
            self.pixel_values[count] = np.frombuffer(pb.get_pixels(), dtype=np.uint8)
            count += 1

    def light_pixel_array(self):
        for i in range(self.pixel_num):
            self.pixels[i] = tuple(map(tuple, self.pixel_values))[i]

    def run_controller(self):
        while (True):
            try:
                self.get_pixel()
                self.light_pixel_array()
            except KeyboardInterrupt:
                led_controller.turn_off()
                break

    def led_cb(self, msg):
        for i in range(self.pixel_num):
            self.pixels[i] = tuple(map(tuple, msg.strip))[i]


if __name__ == '__main__':
    led_controller = LedControl()
    rospy.spin()
    led_controller.turn_off()

    led_controller.run_controller()
