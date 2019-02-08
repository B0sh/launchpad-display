#SingleInstance force
SendMode Input
SetWorkingDir %A_ScriptDir% 

^!r::Reload  ; Assign Ctrl-Alt-R as a hotkey to restart the script.

OnExit, sub_exit
if (midi_in_Open(1))
	ExitApp
Menu TRAY, Icon, icon4.ico

;--------------------  Midi "hotkey" mappings  -----------------------
listenNoteRange(48, 52, "playSomeSounds", 0x02)

return
;----------------------End of auto execute section--------------------

sub_exit:
	midi_in_Close()
ExitApp

;-------------------------Miscellaneous hotkeys-----------------------
Esc::ExitApp

;-------------------------Midi "hotkey" functions---------------------
playSomeSounds(note, vel)
{
    MsgBox "ah"a
      
                
                
}

;-------------------------  Midi input library  ----------------------
#include midi_in_lib.ahk
