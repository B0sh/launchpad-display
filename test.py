from launchpad import *

display = renderFont("  abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ ")

display = renderFont("  abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789  ")

# print (display)

# display = generateDisplayFromFile("b0sh.txt")

# main loop
position = 0
while (position):
    renderFrame(port, display, position)
    position += 1
    time.sleep(0.01)


time.sleep(2)
unloadDisplay(port)

port.close()

