from launchpad import *
from transition import *
import math

class TwitchScroll:
    def __init__(self, message):
        self.delay = 0.05
        self.position = 0
        self.message = message
        unloadDisplay()
            
        self.display = renderFont("  " + message + "   ")

    def loop(self):
        if self.position == -1 or self.position == getLengthOfDisplay(self.display):
            time.sleep(self.delay)
        else:
            rapidRenderFrame(self.display, self.position)
            self.position += 1
            time.sleep(self.delay)

    def is_completed(self):
        if self.position == -1 or self.position == getLengthOfDisplay(self.display):
            return True
        else:
            return False
        