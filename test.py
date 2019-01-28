from launchpad import *

display = renderFont("        euwi        ")

# display = generateDisplayFromFile("b0sh.txt")

# main loop
position = 0
while (1):
    renderFrame(port, display, position)
    position += 1
    time.sleep(0.25)

    if getLengthOfDisplay(display) - 8 == position:
        display = renderFont("        akka")
        position = 0

time.sleep(2)
unloadDisplay(port)

port.close()

