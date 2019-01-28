from launchpad import *
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

    # background transition
    tiles = list(range(0, 64))
    while (len(tiles) != 0):
        random.shuffle(tiles)
        x = tiles[0] % 8
        y = math.floor(tiles[0] / 8)
        on(x, y, COLORS['.'])
        del tiles[0]
        time.sleep(0.02)

    # walden display
    display = renderFont("  Walden's World  ")
    position = 0
    while (position != getLengthOfDisplay(display) - 8):
        renderFrame(port, display, position)
        position += 1
        time.sleep(DELAY)

    # b0sh display
    display = renderFont("  b0sh_  ")
    position = 0
    while (position != getLengthOfDisplay(display) - 8):
        renderFrame(port, display, position)
        position += 1
        time.sleep(DELAY)

    
    # top down transition
    tiles = list(range(0, 64))
    while (len(tiles) != 0):
        x = tiles[0] % 8
        y = math.floor(tiles[0] / 8)
        on(x, y, COLORS['.'])
        del tiles[0]
        time.sleep(DELAY / 5)
        
    # arbitrary tranformation matrix to transition
    # the middle wrap around
    transition_matrix = [
        57,	56,	55,	54,	53,	52,	51,	50,
        58,	31,	30,	29,	28,	27,	26,	49,
        59,	32,	13,	12,	11,	10,	25,	48,
        60,	33,	14,	3,	2,	9,	24,	47,
        61,	34,	15,	4,	1,	8,	23,	46,
        62,	35,	16,	5,	6,	7,	22,	45,
        63,	36,	17,	18,	19,	20,	21,	44,
        64,	37,	38,	39,	40,	41,	42,	43
    ]
    
    # convert transition matrix to sequential tile operations
    tiles = list(range(0, 64))
    for index, value in enumerate(transition_matrix):
        tiles[value-1] = index
    
    while (len(tiles) != 0):
        x = tiles[0] % 8
        y = math.floor(tiles[0] / 8)
        on(x, y, COLORS['.'])
        del tiles[0]
        time.sleep(DELAY / 5)
