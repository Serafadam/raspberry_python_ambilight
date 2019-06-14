import numpy as np
import rospy
import gi
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk
from raspberry_python_ambilight.msg import LedStrip

class ScreenReader(object):
    def __init__(self):
        rospy.init_node('screen_reader')
        self.pixel_num = 60
        self.w = Gdk.get_default_root_window()
        self.width = self.w.get_width()
        self.height = self.w.get_height()
        self.pix_led_ratio = self.width/self.pixel_num
        self.pixel_screen_positions = np.arange(0, self.width, self.pix_led_ratio)
        self.w = Gdk.get_default_root_window()
        self.pixel_values = np.zeros((60, 3), dtype=np.uint8)
        self.pix_publisher = rospy.Publisher('/raspberry_ambilight/data', LedStrip)
        self.x = self.height - self.height/3

    def get_pixel(self):
        count = 0
        for i in self.pixel_screen_positions:
            pb = Gdk.pixbuf_get_from_window(self.w, i, self.x, 1, 1)
            self.pixel_values[count] = np.frombuffer(pb.get_pixels(), dtype=np.uint8)
            count += 1

    def execute(self):
        while True:
            try:
                self.get_pixel()
                self.pix_publisher.publish(self.pixel_values)
            except KeyboardInterrupt:
                break


if __name__ == '__main__':
    screen_reader = ScreenReader()
    rospy.spin()
    screen_reader.execute()
