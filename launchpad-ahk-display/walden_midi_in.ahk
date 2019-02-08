; ;;"#defines"
; inDeviceID := 0
; CALLBACK_WINDOW := 0x10000


; Gui, +LastFound
; hWnd := WinExist()



; ; MsgBox, hWnd = %hWnd%`nPress OK to open winmm.dll library

; OpenCloseMidiAPI()
; OnExit, Sub_Exit


; ; MsgBox, winmm.dll loaded.`nPress OK to open midi device`nDevice ID = %inDeviceID%`nhWnd = %hWnd%`ndwFlags = CALLBACK_WINDOW

; hMidiIn =
; VarSetCapacity(hMidiIn, 4, 0)

; result := DllCall("winmm.dll\midiInOpen", UInt,&hMidiIn, UInt,inDeviceID, UInt,hWnd, UInt,0, UInt,CALLBACK_WINDOW, "UInt")

; If result
; {
; 	MsgBox, error, midiInOpen returned %result%`n
; 	GoSub, sub_exit
; }

; hMidiIn := NumGet(hMidiIn) ; because midiInOpen writes the value in 32 bit binary number, AHK stores it as a string


; ; MsgBox, Midi input device opened successfully`nhMidiIn = %hMidiIn%`n`nPress OK to start the midi device

; result := DllCall("winmm.dll\midiInStart", UInt,hMidiIn)
; If result
; {
; 	MsgBox, error, midiInStart returned %result%`n
; 	GoSub, sub_exit
; }


; ;	#define MM_MIM_OPEN         0x3C1           /* MIDI input */
; ;	#define MM_MIM_CLOSE        0x3C2
; ;	#define MM_MIM_DATA         0x3C3
; ;	#define MM_MIM_LONGDATA     0x3C4
; ;	#define MM_MIM_ERROR        0x3C5
; ;	#define MM_MIM_LONGERROR    0x3C6

; OnMessage(0x3C1, "midiInHandler")
; OnMessage(0x3C2, "midiInHandler")
; OnMessage(0x3C3, "midiInHandler")
; OnMessage(0x3C4, "midiInHandler")
; OnMessage(0x3C5, "midiInHandler")
; OnMessage(0x3C6, "midiInHandler")

; return


; sub_exit:

; If (hMidiIn)
; 	DllCall("winmm.dll\midiInClose", UInt,hMidiIn)
; OpenCloseMidiAPI()

; ExitApp

; ;--------End of auto-execute section-----
; ;----------------------------------------


; OpenCloseMidiAPI() {
; ;    Static hModule 
; ;    If hModule 
; ;       DllCall("FreeLibrary", UInt,hModule), hModule := "" 
; ;    If (0 = hModule := DllCall("LoadLibrary",Str,"winmm.dll")) { 
; ;       MsgBox Cannot load library winmm.dll 
; ;       ExitApp
; ;    } 
; } 



