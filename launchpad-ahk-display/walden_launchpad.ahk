#Include walden_midi_out.ahk
#Include walden_midi_in.ahk
; https://autohotkey.com/board/topic/17212-midi-output-from-ahk/
 
;Constants:
channel := 1               ;midi channel to send on
MidiDevice := 0       ;number of midi output device to use.  
Note := 60            ;midi number for middle C

;Open the Windows midi API dll
hModule := OpenMidiAPI()
;Open the midi port
h_midiout := midiOutOpen(2)

F1::
ASend("red", 3, 5)
Return
F2::
ASend("green", 7, 7)
Return
F3::
ASend("amber", 0, 0)
Return
F4::
ASend("orange", 7, 0)
Return

; TODO: You can use a render order function and then just loop through that
; to get the array of points

; strict x to x downard
F5::
    y := 0
    Loop 64 {
        x := Mod(A_Index - 1, 8)

        AOn("green", x, y)
        Sleep 15

        if (x = 7)
            y := y + 1
    }

    y := 0
    Loop 64 {
        x := Mod(A_Index - 1, 8)

        AOff("orange", x, y)
        Sleep 15

        if (x = 7)
            y := y + 1
    }
    Return

; chaos game animation
F6::
    Points := []

    ; create array of all points
    Loop 64 {
        Points.Push(A_Index - 1)
    }

    Loop 64 {
        max := Points.maxindex()
        Random, r, 1, max

        x := Mod(Points[r], 8)
        y := Floor(Points[r] / 8)
        ; MsgBox %r% %z% %x% %y%
        Points.remove(r)

        AOn("green", x, y)
        Sleep 30
    }
    ; create array of all points
    Loop 64 {
        Points.Push(A_Index - 1)
    }

    Loop 64 {
        max := Points.maxindex()
        Random, r, 1, max

        x := Mod(Points[r], 8)
        y := Floor(Points[r] / 8)
        ; MsgBox %r% %z% %x% %y%
        Points.remove(r)

        AOff("green", x, y)
        Sleep 30
    }
    ; create array of all points
    Loop 64 {
        Points.Push(A_Index - 1)
    }

    Loop 64 {
        max := Points.maxindex()
        Random, r, 1, max

        x := Mod(Points[r], 8)
        y := Floor(Points[r] / 8)
        ; MsgBox %r% %z% %x% %y%
        Points.remove(r)

        AOn("amber", x, y)
        Sleep 30
    }
    ; create array of all points
    Loop 64 {
        Points.Push(A_Index - 1)
    }

    Loop 64 {
        max := Points.maxindex()
        Random, r, 1, max

        x := Mod(Points[r], 8)
        y := Floor(Points[r] / 8)
        ; MsgBox %r% %z% %x% %y%
        Points.remove(r)

        AOff("amber", x, y)
        Sleep 30
    }
    ; create array of all points
    Loop 64 {
        Points.Push(A_Index - 1)
    }

    Loop 64 {
        max := Points.maxindex()
        Random, r, 1, max

        x := Mod(Points[r], 8)
        y := Floor(Points[r] / 8)
        ; MsgBox %r% %z% %x% %y%
        Points.remove(r)

        AOn("orange", x, y)
        Sleep 30
    }
    ; create array of all points
    Loop 64 {
        Points.Push(A_Index - 1)
    }

    Loop 64 {
        max := Points.maxindex()
        Random, r, 1, max

        x := Mod(Points[r], 8)
        y := Floor(Points[r] / 8)
        ; MsgBox %r% %z% %x% %y%
        Points.remove(r)

        AOff("orange", x, y)
        Sleep 30
    }
    ; create array of all points
    Loop 64 {
        Points.Push(A_Index - 1)
    }

    Loop 64 {
        max := Points.maxindex()
        Random, r, 1, max

        x := Mod(Points[r], 8)
        y := Floor(Points[r] / 8)
        ; MsgBox %r% %z% %x% %y%
        Points.remove(r)

        AOn("red", x, y)
        Sleep 30
    }
    ; create array of all points
    Loop 64 {
        Points.Push(A_Index - 1)
    }

    Loop 64 {
        max := Points.maxindex()
        Random, r, 1, max

        x := Mod(Points[r], 8)
        y := Floor(Points[r] / 8)
        ; MsgBox %r% %z% %x% %y%
        Points.remove(r)

        AOff("red", x, y)
        Sleep 30
    }

    Return
; chaos game animation
F7::
    Points := []

    ; create array of all points
    Loop 64 {
        Points.Push(A_Index - 1)
    }

    Loop 64 {
        max := Points.maxindex()
        Random, r, 1, max

        x := Mod(Points[r], 8)
        y := Floor(Points[r] / 8)
        ; MsgBox %r% %z% %x% %y%
        Points.remove(r)

        AOn("green", x, y)
        Sleep 30
    }
    ; create array of all points
    Loop 64 {
        Points.Push(A_Index - 1)
    }

    Loop 64 {
        max := Points.maxindex()
        Random, r, 1, max

        x := Mod(Points[r], 8)
        y := Floor(Points[r] / 8)
        ; MsgBox %r% %z% %x% %y%
        Points.remove(r)

        AOn("amber", x, y)
        Sleep 30
    }
    ; create array of all points
    Loop 64 {
        Points.Push(A_Index - 1)
    }

    Loop 64 {
        max := Points.maxindex()
        Random, r, 1, max

        x := Mod(Points[r], 8)
        y := Floor(Points[r] / 8)
        ; MsgBox %r% %z% %x% %y%
        Points.remove(r)

        AOn("orange", x, y)
        Sleep 30
    }
    ; create array of all points
    Loop 64 {
        Points.Push(A_Index - 1)
    }
    Loop 64 {
        max := Points.maxindex()
        Random, r, 1, max

        x := Mod(Points[r], 8)
        y := Floor(Points[r] / 8)
        ; MsgBox %r% %z% %x% %y%
        Points.remove(r)

        AOn("red", x, y)
        Sleep 30
    }
    ; create array of all points
    Loop 64 {
        Points.Push(A_Index - 1)
    }

    Loop 64 {
        max := Points.maxindex()
        Random, r, 1, max

        x := Mod(Points[r], 8)
        y := Floor(Points[r] / 8)
        ; MsgBox %r% %z% %x% %y%
        Points.remove(r)

        AOff("red", x, y)
        Sleep 30
    }

    Return

^!r::Reload  ; Assign Ctrl-Alt-R as a hotkey to restart the script.


midiInHandler(hInput, midiMsg, wMsg) 
{
	statusbyte := midiMsg & 0xFF
	byte1 := (midiMsg >> 8) & 0xFF
	byte2 := (midiMsg >> 16) & 0xFF

	ToolTip,
	(
Received a message: %wMsg%
wParam = %hInput%
lParam = %midiMsg%
	statusbyte = %statusbyte%
	byte1 = %byte1%
	byte2 = %byte2%
	)

}



; Readers who are versed in the manipulation of binary will have 
; worked out that bits 1 and 0 of the note velocity refer to the level 
; of the red element, and bits 5 and 4 refer to the level of the green 
; element.  The  red  intensity  is  therefore  varied  by  progressively 
; adding 1 to the  ‘off’ value, shown in  Figure 4 as 0 Ch (12). The 
; green intensity is adjustable by progressively adding 10h (16). 
; Red  and  green  light  combine  in  equal  proportions  to  form  the 
; amber  colour,  and  in  other  proportions  to  form  orange  and yellow. 
GetLaunchpadColor(color) {
    if (color = "red") {
        return 3 ; 0b00000011
    } else if (color = "green") {
        return 48 ; 0b00110000
    } else if (color = "amber") {
        return 51 ; 0b00110011
    } else if (color = "orange") {
        return 35 ; 0b00100011
    }
}

GetLaunchpadXY(x, y) {
    return y * 16 + x
}

ASend(color, x, y) {
    global
    AOn(color, x, y) 
    Sleep %NoteDur%
    AOff(color, x, y) 
}

AOff(color, x, y) {
    global
    NoteDur := 30       ;duration to hold note for (approx.)
    Velocity := GetLaunchpadColor(color)
    Note := GetLaunchpadXY(x, y)

    ;Send Note-Off command for middle C 
    midiOutShortMsg(h_midiout, "N0", Channel, Note, 0)
}

AOn(color, x, y) {
    global
    NoteDur := 30       ;duration to hold note for (approx.)
    Velocity := GetLaunchpadColor(color)
    Note := GetLaunchpadXY(x, y)

    ; "N1" is shorthand for "NoteOn". See comments in midiOutShortMsg for a full list of allowable event types 
    midiOutShortMsg(h_midiout, "N1", Channel, Note, Velocity)
}