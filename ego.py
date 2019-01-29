from launchpad import *
from transition import *
import random
import math

DELAY = 0.10


# main loop
while (1):

    # TODO: Break off as function
    # Remove possibilty for amber on orange
    random.shuffle(AVAILABLE_COLORS)
    COLORS['x'] = AVAILABLE_COLORS[0]
    COLORS['.'] = AVAILABLE_COLORS[1]


    transition_matrix = getRandomTransition()
    
    # convert transition matrix to sequential tile operations
    tiles = list(range(0, 64))
    for index, value in enumerate(transition_matrix):
        tiles[value-1] = index
    
    while (len(tiles) != 0):
        x = tiles[0] % 8
        y = math.floor(tiles[0] / 8)
        on(x, y, COLORS['.'])
        del tiles[0]
        time.sleep(DELAY / 3)


    # walden display
    display = renderFont("  Walden's World  ")
    position = 0
    while (position != getLengthOfDisplay(display) - 8):
        renderFrame(port, display, position)
        position += 1
        time.sleep(DELAY)

#    # b0sh display
#    display = renderFont("  b0sh_  ")
#    position = 0
#    while (position != getLengthOfDisplay(display) - 8):
#        renderFrame(port, display, position)
#        position += 1
#        time.sleep(DELAY)





