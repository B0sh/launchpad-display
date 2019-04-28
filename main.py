import tkinter as tk
from ego import *
from audio import *
import time
import threading
import sys
import random
import queue

# https://www.oreilly.com/library/view/python-cookbook/0596001673/ch09s07.html
class GUI:
    def __init__ (self, master, queue, client):
        self.queue = queue
        
        master.configure(background='#0F0020')
        master.protocol('WM_DELETE_WINDOW', client.endApplication)

        title_label = tk.Label(text="Launchpad Control Panel", fg="#F0E0D0", bg="#0F0020", font=("Helvetica", 16))
        title_label.pack(padx=10, pady=10)

        # init GUI
        text_button = tk.Button(master, text='Ego Scroll', width=25, command=client.set_text_scroll, padx=4, pady=4)
        text_button.pack(padx=10, pady=10)

        audio_button = tk.Button(master, text='Audio', width=25, command=client.set_audio, padx=4, pady=4)
        audio_button.pack(padx=10, pady=10)

        stop_button = tk.Button(master, text='Stop', width=25, command=client.stop_launchpad, padx=4, pady=4)
        stop_button.pack(padx=10, pady=10)

    
    def processIncoming (self):
        # handle all messages in the queue, if any
        while self.queue.qsize():
            try:
                msg = self.queue.get(0)
                print (msg)
            # incase there is no elements
            except Queue.Empty:
                pass


class ThreadedClient:
    # Launch the main part of GUI and worker thread
    def __init__ (self, master):
        # Start GUI and async threads
        self.active = None
        self.master = master
        self.queue = queue.Queue()

        self.gui = GUI(master, self.queue, self)

        # Configure threads
        self.running = 1
        self.thread1 = threading.Thread(target=self.workerThread1)
        self.thread1.start()

        # Start up checks to see if GUI needs to do anything
        self.periodicCall()

    # check if there is something new in the queue
    def periodicCall(self):
        self.gui.processIncoming()

        # force shutdown if GUI not running
        if not self.running:
            sys.exit(1)

        self.master.after(200, self.periodicCall)

    # this is where we handle async actions 
    def workerThread1(self):
        while self.running:
            if self.active == None:
                time.sleep(.25)
            elif self.active == 'stop':
                self.active = None
                unloadDisplay()
            elif self.active == 'text':
                self.active = TextScroll()
            elif self.active == 'audio':
                self.active = LaunchpadAudio()  
            else:
                self.active.loop()
    
    def set_text_scroll(self):
        self.active = 'text'

    def set_audio(self):
        self.active = 'audio'

    def stop_launchpad(self):
        self.active = 'stop'

    def endApplication(self):
        print ("END APPLICATION")
        self.running = 0

    

q = tk.Tk()
q.title('Launchpad Display')
q.geometry("300x240")

client = ThreadedClient(q)

try:
    q.mainloop()
except:
    client.endApplication()
