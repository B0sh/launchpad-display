from launchpad import *
from transition import *
import math
import datetime

DELAY = 0.20


# main loop
while (1):

    generateNextColors()

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
    # Display = renderFont("  Walden's World  ")
    display = renderFont("B0sh_  ")
    
 #   today = datetime.datetime.today().strftime('%A, %B %d  %I:%M %p')
 #   display = renderFont("  " + today + "  ")


    position = 0
    while (position != getLengthOfDisplay(display) - 8):
        rapidRenderFrame(display, position)
        position += 1
        time.sleep(DELAY)

#    # b0sh display
#    display = renderFont("  b0sh_  ")
#    position = 0
#    while (position != getLengthOfDisplay(display) - 8):
#        renderFrame(display, position)
#        position += 1
#        time.sleep(DELAY)





