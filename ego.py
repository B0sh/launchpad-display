from launchpad import *
from transition import *
import math
import datetime

class TextScroll:
    def __init__(self):
        self.loops = 0
        self.delay = 0.15
        self.position = -1

        unloadDisplay()
    
    def reset(self):
        generateNextColors()
        transition = getRandomTransition()

        # convert transition matrix to sequential tile operations
        tiles = list(range(0, 64))
        for index, value in enumerate(transition['matrix']):
            tiles[value-1] = index
        
        while (len(tiles) != 0):
            x = tiles[0] % 8
            y = math.floor(tiles[0] / 8)
            on(x, y, transition['colors'][len(tiles)-1])
            del tiles[0]
            time.sleep(self.delay / 3)

            
        x = self.loops % 2
        if x == 0:
            self.display = renderFont("  Walden's World  b0sh_  ")
        elif x == 1:
            today = datetime.datetime.today().strftime('%A, %B %d  %I:%M %p')
            self.display = renderFont("  " + today + "  ")

        self.position = 0
        self.loops += 1


    def loop(self):
        if self.position == -1 or self.position == getLengthOfDisplay(self.display) - 8:
            self.reset()
        else:
            rapidRenderFrame(self.display, self.position)
            self.position += 1
            time.sleep(self.delay)
