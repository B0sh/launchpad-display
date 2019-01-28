import mido
import time

FONT = {}
COLORS = {
    "x": "red",
    ".": "none",
}


def getNoteFromLaunchpadXY(x, y):
    return x + y * 16

def getVelocityFromLaunchpadColor(color):
    if color == "red":
        return 3 # 0b00000011
    elif color == "green":
        return 48 # 0b00110000
    elif color == "amber":
        return 51 # 0b00110011
    elif color == "orange":
        return 35 # 0b00100011
    else:
        return 0

def tile(action, x, y, color=''):
    note = getNoteFromLaunchpadXY(x, y)
    velocity = getVelocityFromLaunchpadColor(color)
    return mido.Message(action, note=note, velocity=velocity)


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

# combine font characters into a display from a string
def renderFont(text):
    display = ['', '', '', '', '', '', '', '']
    for char in text:
        if char in FONT:
            char = FONT[char]
        # if the character doesn't exist, use !
        else:
            char = FONT["!"]
            
        for x in range(0, 8):
            display[x] = display[x] + char[x]

    return display

def renderFrame(port, display, position):

    frame = []
    for line in display:
        position = position % len(line) 
        line = line + line
        frame.append(line[position:position+8])

    # print(frame)
    
    x = 0
    y = 0
    for line in frame:
        for x in range (0, 8):
            
            if line[x] in COLORS:
                
                port.send(tile("note_on", x, y, COLORS[line[x]]))
            else:
                port.send(tile("note_off", x, y, "amber"))

        y += 1

def unloadDisplay(port):
    for y in range (0, 8):
        for x in range(0, 8):
            port.send(tile("note_off", x, y))


########### SETUP ############
            
# Get the launchpad device no matter which port its plugged in
device_name = False
for device in mido.get_output_names():
    if "Launchpad" in device:
        device_name = device

if device_name == False:
    print ("No Launchpad detected!")
    exit()

port = mido.open_output(device_name)

initFont("characters.txt")
        
