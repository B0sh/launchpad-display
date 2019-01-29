# launchpad-display

Creating a 8x8 display out of a [Novation Launchpad S](https://novationmusic.com/launch/launchpad) using Python and MIDI to send signals to the launchpad.

## How it works

The [Novation Launchpad S Programmer's Reference Manual](https://customer.novationmusic.com/sites/customer/files/novation/downloads/4700/launchpad-s-prm.pdf)
details how and in what way to send MIDI singals to control the lights of the launchpad. 
The "note" byte of the MIDI message maps to a tile's XY position and 
the "velocity" byte of the MIDI message relates to brightness and color to set on that tile.
These are abstracted away so that the display script can just directly control the tiles with x, y, and color.


## Ideas

* For stream: Hide secret code that gets randomly generated and added to a text file
