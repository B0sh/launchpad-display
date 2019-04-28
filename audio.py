#!/usr/bin/env python3

# Based off of this spectrum analyzer
# https://gist.github.com/netom/8221b3588158021704d5891a4f9c0edd

import pyaudio
import numpy
import math

from launchpad import *
from transition import *

class LaunchpadAudio:
    def __init__(self):
        self.RATE = 44100
        self.BUFFER = 1524

        # the number of samples represented for each column
        # should be proportional to buffer size
        self.rate8 = int(self.BUFFER / 8 / 4 )

        # dB levels at which each row of frequency responds
        self.levels = [
            -40,
            -48,
            -56,
            -64,
            -72,
            -80,
            -90,
            -100
        ]

        # colors for each row of frequency
        self.color_lookup = "reodaylg"

        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format = pyaudio.paFloat32,
            channels = 1,
            rate = self.RATE,
            input = True,
            output = False,
            frames_per_buffer = self.BUFFER,
            input_device_index = 3
        )

        unloadDisplay()

    def loop(self):
        # Calculate the data from the previous buffer
        try:
            data = numpy.fft.rfft(
                numpy.fromstring(
                    self.stream.read(self.BUFFER), dtype=numpy.float32
                )
            )
        except IOError:
            pass

        # its possible to get zero result when audio disabled, so just skip processing
        try: 
            data = numpy.log10(
                numpy.sqrt(
                    numpy.real(data)**2+numpy.imag(data)**2
                ) / self.BUFFER
            ) * 20
        except ZeroDivisionError:
            pass
        
        # init table
        table = [""] * 8

        for x in range(0, 8):
            # variable slicing cannot be done with : syntax
            s = slice(self.rate8*x , self.rate8*(x+1))
            high = max(data[s])

            for y in range (0, 8):
                if self.levels[y] < high:
                    table[y] += self.color_lookup[x]
                else:
                    table[y] += "."

        # render frame with launchpad as fast as possible
        rapidRenderFrame(table, 0)
        
