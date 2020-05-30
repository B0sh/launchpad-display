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
        self.p = pyaudio.PyAudio()

        # https://stackoverflow.com/questions/21610198/runtimewarning-divide-by-zero-encountered-in-log
        # Disable divide by zero errors
        numpy.seterr(divide = 'ignore') 

        self.RATE = 44100
        self.BUFFER = 1524

        # the number of samples represented for each column
        # should be proportional to buffer size
        self.rate9 = int(self.BUFFER / 9 / 4 )

        # dB levels at which each row of frequency responds
        self.levels = [ ]

        dB = -26
        for x in range(9):
            self.levels.append(dB)
            dB = dB - 9

        # colors for each row of frequency
        self.color_lookup = "reodaylgg"


    def start(self, audio_index):
        self.stream = self.p.open(
            format = pyaudio.paFloat32,
            channels = 1,
            rate = self.RATE,
            input = True,
            output = False,
            frames_per_buffer = self.BUFFER,
            input_device_index = audio_index
        )

        unloadDisplay()

        return self

    def get_audio_devices(self):
        info = self.p.get_host_api_info_by_index(0)
        numdevices = info.get('deviceCount')
        input_devices = {} 
        for i in range(0, numdevices):
            if (self.p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                name = self.p.get_device_info_by_host_api_device_index(0, i).get('name'); 
                input_devices[name] = i
                # print ("Input Device id ", i, " - ", name)

        return input_devices

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
        data = numpy.log10(
            numpy.sqrt(
                numpy.real(data)**2+numpy.imag(data)**2
            ) / self.BUFFER
        ) * 20
        
        # init table
        table = [""] * 9

        for x in range(0, 9):
            # variable slicing cannot be done with : syntax
            s = slice(self.rate9*x , self.rate9*(x+1))
            high = max(data[s])

            for y in range (0, 9):
                if self.levels[y] < high:
                    table[y] += self.color_lookup[x]
                else:
                    table[y] += "."

        # render frame with launchpad as fast as possible
        rapidRenderFrame(table, 0)
        
    def is_completed(self):
        return False
