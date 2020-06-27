
 #!/usr/bin/env python3
import numpy as np
import sounddevice as sd
import sys
import board
import neopixel
import time
import numpy as np
import gi

def led_sound():

    board_pin = board.D18
    pixel_num = 60
    pixels = neopixel.NeoPixel(board_pin, pixel_num)
    pixel_array = np.zeros((60,3),dtype=np.uint8)
    pixels.fill(0)
    duration = 20 #in seconds

    sd.device = 2

    def audio_callback(indata, frames, time, status):
        pixels.fill(0)
        volume_norm = np.linalg.norm(indata)*10
        if int(volume_norm > 59):
            volume_norm = 59
        for i in range(0, int(volume_norm)):
            pixels[i] = (255,0,0)

        print("|" * int(volume_norm))


    stream = sd.InputStream(device=2, channels=1,
        samplerate=44100.0,callback=audio_callback)
    with stream:
        sd.sleep(duration * 1000)

if __name__ == '__main__':
    led_sound()
