import mido
import time
import signal
import random

FONT = {}
AVAILABLE_COLORS = ['red', 'green', 'amber', 'orange', 'none']
COLORS = {
    "x": "red",
    "r": "red",
    "e": "orangered",
    "g": "green",
    "n": "dimgreen",
    "a": "amber",
    "o": "orange",
    "d": "dimorange",
    "y": "yellow",
    "l": "lime",
    ".": "none",
}


def getNoteFromLaunchpadXY(x, y):
    return x + y * 16


def getVelocityFromLaunchpadColor(color):
    color = str(color)

    if color.isdigit():
        return int(color)

    if color in COLORS:
        color = COLORS[color]
    
    if color == "red":
        return 15  # 0b00000011
    elif color == "dimred":
        return 14
    elif color == "yellow":
        return 62
    elif color == "green":
        return 48  # 0b00110000
    elif color == "amber":
        return 51  # 0b00110011
    elif color == "orange":
        return 35  # 0b00100011
    elif color == "dimorange":
        return 46
    elif color == "orangered":
        return 27
    elif color == "lime":
        return 57
    else:
        return 0


def tile(action, x, y, color=''):
    note = getNoteFromLaunchpadXY(x, y)
    velocity = getVelocityFromLaunchpadColor(color)
    return mido.Message(action, note=note, velocity=velocity)

def all_colors_display():
    i = 0
    for y in range(0, 8):
        for x in range(0, 8):
            on(x, y, i)
            i += 1
            

def on(x, y, color):
    port.send(tile("note_on", x, y, color))


def off(x, y):
    port.send(tile("note_off", x, y))


def unloadDisplay():
    global COLORS
    COLORS = {
        "x": "red",
        "r": "red",
        "e": "orangered",
        "g": "green",
        "n": "dimgreen",
        "a": "amber",
        "o": "orange",
        "d": "dimorange",
        "y": "yellow",
        "l": "lime",
        ".": "none",
    }


    # create a 2d array of 8x8 dots
    display = [['.'] * 8] * 10
    rapidRenderFrame(display, 0)


# create the font text
def initFont(file):
    file = open(file)

    i = 0
    for line in file.readlines():
        line = line.rstrip('\n')

        if i % 9 == 0:
            # if a character is not detected
            if len(line) != 1:
                break
            char = line
            char_display = []
            # print ("char: ", line)
        else:
            char_display.append(line)
            FONT[char] = char_display
            # print (line)
        i += 1


# return an array of the display from a file
def generateDisplayFromFile(file):
    file = open(file)

    display = []
    for line in file.readlines():
        line = line.rstrip()
        if len(display) < 8:
            display.append(line)
        else:
            config = line.split(' ')
            COLORS[config[0]] = config[1]
    return display


def getLengthOfDisplay(display):
    return len(display[0])


# generate the next set of random colors according to a set of rules
def generateNextColors():
    while True:
        random.shuffle(AVAILABLE_COLORS)
        background = AVAILABLE_COLORS[0]
        text = AVAILABLE_COLORS[1]
        if background == "amber" and text == "orange":
            continue
        elif background == "orange" and text == "amber":
            continue
        elif background == "orange" and text == "red":
            continue
        elif background == "red" and text == "orange":
            continue
        elif background == "red" and text == "yellow":
            continue
        elif background == "yellow" and text == "red":
            continue
        elif background == COLORS['.']:
            continue
        # elif text == COLORS['x']:
        #    continue
        else:
            break

    COLORS['x'] = text
    COLORS['.'] = background


# combine font characters into a display from a string
def renderFont(text):
    display = [''] * 8
    for char in text:
        if char in FONT:
            char = FONT[char]
        # if the character doesn't exist, use !
        else:
            char = FONT["!"]

        for x in range(0, 8):
            display[x] = display[x] + char[x]

    return display


# send the signals to render a given display frame
def renderFrame(display, position):
    frame = []
    for line in display:
        position = position % len(line)
        line = line + line
        frame.append(line[position:position + 8])

    y = 0
    for line in frame:
        for x in range(0, 8):
            if line[x] in COLORS:
                on(x, y, COLORS[line[x]])
            else:
                off(x, y)
        y += 1


# use the launchpad's Rapid LED Update mode
def rapidRenderFrame(display, position):
    frame = []
    for line in display:
        position = position % len(line)
        line = line + line
        frame.append(line[position:position + 8])

    # send a dummy signal on channel 1 to reset midi position
    off(15, 7)

    last_color = -1
    for line in frame:
        for x in range(0, 8):
            if line[x] in COLORS:
                c = COLORS[line[x]]
            else:
                c = COLORS['none']

            if last_color == -1:
                last_color = c
            else:
                color1 = getVelocityFromLaunchpadColor(last_color)
                color2 = getVelocityFromLaunchpadColor(c)

                message = mido.Message("note_on", note=color1, velocity=color2, channel=2)
                port.send(message)

                last_color = -1

# use the launchpad's Rapid LED Update mode
def rapidRenderFrameWithButton(display, position):
    frame = []
    for line in display:
        position = position % len(line)
        line = line + line
        frame.append(line[position:position + 9])

    # create empty points array
    points = []
    for i in range(81):
        points.append('.')

    # setup the order for rapid render mode:
    # Starting at the top-left-hand corner in either mode, subsequent note
    # messages update the 64-pad grid horizontally and then vertically. They
    # then update the eight clip launch buttons, and then the eight mode
    # buttons.

    for index, line in enumerate(frame):
        if index == 0:
            for point_index, point in enumerate(line):
                points[point_index + 64 + 8] = point
        else:
            index = index - 1
            for point_index, point in enumerate(line):
                if point_index == 8:
                    points[64 + index] = point
                else:
                    points[point_index + index * 8] = point

    # send a dummy signal on channel 1 to reset midi position
    off(15, 7)

    last_color = -1
    for point in points:
        if point in COLORS: c = COLORS[point]
        else:
            c = COLORS['none']

        if last_color == -1:
            last_color = c
        else:
            color1 = getVelocityFromLaunchpadColor(last_color)
            color2 = getVelocityFromLaunchpadColor(c)

            message = mido.Message("note_on", note=color1, velocity=color2, channel=2)
            port.send(message)

            last_color = -1

########### SETUP ############

# Get the launchpad device no matter which port its plugged in
device_name = False
for device in mido.get_output_names():
    if "Launchpad" in device:
        device_name = device

if device_name == False:
    print("No Launchpad detected!")
    exit()

port = mido.open_output(device_name)
initFont("characters.txt")

unloadDisplay()

# https://keyboardinterrupt.org/catching-a-keyboardinterrupt-signal/?doing_wp_cron=1548654812.1566979885101318359375
# def keyboardInterruptHandler(signal, frame):
#    unloadDisplay(port)
#    port.close()

# signal.signal(signal.SIGINT, keyboardInterruptHandler)


        
