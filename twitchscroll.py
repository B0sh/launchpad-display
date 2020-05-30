from launchpad import *
from transition import *
import math

class TwitchScroll:
    def __init__(self, message, previous_display):
        self.delay = 0.05
        self.position = 0
        self.message = message
        self.previous_display = previous_display
        unloadDisplay()
            
        self.display = renderFont("  " + message + "   ")

    def loop(self):
        if self.position == -1 or self.position == getLengthOfDisplay(self.display):
            time.sleep(self.delay)
        else:
            rapidRenderFrame(self.display, self.position)
            self.position += 1
            time.sleep(self.delay)

    def finished(self):
        if self.position == -1 or self.position == getLengthOfDisplay(self.display):
            return self.previous_display
        else:
            return False
        