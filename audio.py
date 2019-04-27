#!/usr/bin/env python3

# Based off of this spectrum analyzer
# https://gist.github.com/netom/8221b3588158021704d5891a4f9c0edd

import pyaudio
import numpy
import math

from launchpad import *
from transition import *

RATE = 44100
BUFFER = 1524

# dB levels at which each row of frequency responds
levels = [
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
color_lookup = "reodaylg"

# the number of samples represented for each column
# should be proportional to buffer size
rate8 = int(BUFFER / 8 / 4 )

p = pyaudio.PyAudio()

stream = p.open(
    format = pyaudio.paFloat32,
    channels = 1,
    rate = RATE,
    input = True,
    output = False,
    frames_per_buffer = BUFFER,
    input_device_index = 3
)


while True:
    # Calculate the data from the previous buffer
    try:
        data = numpy.fft.rfft(
            numpy.fromstring(
                stream.read(BUFFER), dtype=numpy.float32
            )
        )
    except IOError:
        pass

    # its possible to get zero result when audio disabled, so just skip processing
    try: 
        data = numpy.log10(
            numpy.sqrt(
                numpy.real(data)**2+numpy.imag(data)**2
            ) / BUFFER
        ) * 20
    except ZeroDivisionError:
        pass
    
    # init table
    table = [""] * 8

    for x in range(0, 8):
        # variable slicing cannot be done with : syntax
        s = slice(rate8*x , rate8*(x+1))
        high = max(data[s])

        for y in range (0, 8):
            if levels[y] < high:
                table[y] += color_lookup[x]
            else:
                table[y] += "."

    # render frame with launchpad as fast as possible
    rapidRenderFrame(table, 0)
    
