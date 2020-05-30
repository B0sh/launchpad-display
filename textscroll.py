from launchpad import *
from transition import *
import math
import datetime
import random

class TextScroll:
    def __init__(self):
        self.iteration = random.randint(0, 4)
        self.delay = 0.15
        self.position = 0 
        self.scroll_display = None
        self.full_display = None

        unloadDisplay()
    
    def reset(self):
        self.scroll_display = None
        self.full_display = None

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
            
        self.position = 0
        self.iteration += 1

        self.setNextDisplay()

    def setNextDisplay(self):
        x = self.iteration % 4

        if random.randint(1, 8192) == 1:
            self.scroll_display = renderFont("  ShinyLaunchpad   ")
            return

        if random.randint(1, 100) == 1:
            if random.randint(0, 1) == 0:
                self.scroll_display = renderFont("  ABCDEFGHIJKLMNOPQRSTUVWXYZ   ")
            else:
                self.full_display = " ABCDEFGHIJKLMNOPQRSTUVWXYZ   "
            return 

        if x == 0:
            if random.randint(0, 1) == 0:
                self.full_display = " Walden's World "
            else:
                self.scroll_display = renderFont("  Walden's World   ")
        elif x == 1:
            self.scroll_display = renderFont("  twitch.tv/b0sh_   ")
        elif x == 2:
            today = datetime.datetime.today().strftime('%A, %B %d  %I:%M %p')
            self.scroll_display = renderFont("  " + today + "  ")
        elif x == 3:
            if random.randint(0, 1) == 0:
                self.full_display = " Subscribe with Twitch Prime "
            else:
                self.scroll_display = renderFont("  Subscribe with Twitch Prime!   ")

    def loop(self):
        if self.scroll_display == None and self.full_display == None:
            self.reset()
        elif self.scroll_display != None:
            if self.position == getLengthOfDisplay(self.scroll_display) - 8:
                self.reset()
            else:
                rapidRenderFrame(self.scroll_display, self.position)
                self.position += 1
                time.sleep(self.delay)
        elif self.full_display != None:
            if self.position == len(self.full_display):
                self.reset()
            else:
                character = self.full_display[self.position]
                rapidRenderFrame(renderCharacter(character), 0)
                self.position += 1
                time.sleep(self.delay * 2)

    def is_completed(self):
        return False
