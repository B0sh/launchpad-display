from launchpad import *
import random

DELAY = 0.10

# main loop
while (1):

    random.shuffle(AVAILABLE_COLORS)
    COLORS['x'] = AVAILABLE_COLORS[0]
    COLORS['.'] = AVAILABLE_COLORS[1]

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
