import board
import numpy as np
import neopixel
import rospy


from raspberry_python_ambilight.msg import LedStrip


class LedControl(object):
    def __init__(self):
        self.node = rospy.init_node('raspberry_ambilight')
        self.board_pin = board.D18
        self.pixel_num = 60
        self.pixels = neopixel.NeoPixel(self.board_pin, self.pixel_num)

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


    def light_pixel_array(self):
        for i in range(self.pixel_num):
            self.pixels[i] = tuple(map(tuple, self.pixel_values))[i]

    def run_controller(self):
        while True:
            try:
                pass
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
