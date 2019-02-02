from launchpad import *
from transition import *
import math
import datetime

DELAY = 0.15


# main loop
main_loops = 0
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


    # text display
    x = main_loops % 2
    if x == 0:
        display = renderFont("  Walden's World  b0sh_  ")
    elif x == 1:
        today = datetime.datetime.today().strftime('%A, %B %d  %I:%M %p')
        display = renderFont("  " + today + "  ")
         
    position = 0
    while (position != getLengthOfDisplay(display) - 8):
        rapidRenderFrame(display, position)
        position += 1
        time.sleep(DELAY)



    main_loops += 1
