import tkinter as tk
from textscroll import *
from audio import *
import time
import threading
import sys
import random
import queue
import twitch
from twitchbot import TwitchBot
from twitchscroll import * 

launchpadAudio = LaunchpadAudio()
# https://www.oreilly.com/library/view/python-cookbook/0596001673/ch09s07.html
class GUI:
    def __init__ (self, master, queue, client):
        self.client = client
        self.queue = queue
        
        master.configure(background='#0F0020')
        master.protocol('WM_DELETE_WINDOW', client.endApplication)

        title_label = tk.Label(text="Launchpad Control Panel", fg="#F0E0D0", bg="#0F0020", font=("Helvetica", 16))
        title_label.pack(padx=10, pady=8)

        # init GUI
        text_button = tk.Button(master, text='Text Scroll', width=30, command=client.set_text_scroll, padx=3, pady=3)
        text_button.pack(padx=10, pady=8)

        audio_button = tk.Button(master, text='Audio Spectrogram', width=30, command=client.set_audio, padx=3, pady=3)
        audio_button.pack(padx=10, pady=8)

        self.twitch_button = tk.Button(master, text='Start Twitch', width=30, command=self.toggle_twitch, padx=3, pady=3)
        self.twitch_button.pack(padx=10, pady=8)

        stop_button = tk.Button(master, text='Clear', width=30, command=client.stop_launchpad, padx=3, pady=3)
        stop_button.pack(padx=10, pady=8)

        variable = tk.StringVar(master)
        options = launchpadAudio.get_audio_devices().keys()

        # variable.set("")

        audio_option = tk.OptionMenu(master, variable, *options, command=client.set_audio_input)
        audio_option.config(width=29)
        audio_option.pack(padx=10, pady=8)

    def toggle_twitch(self):
        if self.twitch_button['text'] == 'Start Twitch':
            self.twitch_button.configure(text='Stop Twitch')
            self.client.start_twitch() 
        else:
            self.twitch_button.configure(text='Start Twitch')
            self.client.stop_twitch()
    
    def processIncoming (self):
        # handle all messages in the queue, if any
        while self.queue.qsize():
            try:
                msg = self.queue.get(0)
                print (msg)
            # incase there is no elements
            except queue.Empty:
                pass


class ThreadedClient:
    # Launch the main part of GUI and worker thread
    def __init__ (self, master):
        # Start GUI and async threads
        self.active = None
        self.launch_twitch = False
        self.twitch_bot = None

        self.twitch_message_queue = queue.Queue()

        self.master = master
        self.queue = queue.Queue()
        self.audio_index = 4

        self.gui = GUI(master, self.queue, self)

        # Configure threads
        self.running = 1
        self.thread1 = threading.Thread(target=self.workerThread1)
        self.thread1.start()

        self.thread2 = threading.Thread(target=self.workerThread2)
        self.thread2.start()

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
        previous_active = None

        while self.running:

            while self.twitch_message_queue.qsize():
                try:
                    msg = self.twitch_message_queue.get(0)

                    # Drops messages when currently displaying a chat message
                    if type(self.active).__name__ != "TwitchScroll":
                        previous_active = type(self.active).__name__
                        self.active = TwitchScroll(msg)
                # incase there is no elements
                except queue.Empty:
                    pass

            if self.active == None:
                time.sleep(.25)
            elif self.active == 'stop':
                self.active = None
                unloadDisplay()
            elif self.active == 'TextScroll':
                self.active = TextScroll()
            elif self.active == 'LaunchpadAudio':
                self.active = launchpadAudio.start(self.audio_index)
            elif self.active.is_completed():
                if previous_active == None:
                    self.active = None
                else:
                    self.active = previous_active
                    previous_active = None
            else:
                self.active.loop()

    def workerThread2(self):
        while self.running:
            if self.launch_twitch == True and self.twitch_bot == None:
                self.launch_twitch = False
                self.twitch_bot = TwitchBot(self.twitch_message_queue)
            else:
                time.sleep(.5)

    def set_audio_input(self, audio_name):
        audio_index = launchpadAudio.get_audio_devices()[audio_name]
        print("Set audio input:", audio_index, " - ", audio_name)
        self.audio_index = audio_index
            
    def set_text_scroll(self):
        self.active = 'TextScroll'

    def set_audio(self):
        self.active = 'LaunchpadAudio'

    def stop_launchpad(self):
        self.active = 'stop'

    def start_twitch(self):
        self.launch_twitch = True

    def stop_twitch(self):
        # delete twitch bot object instance so that it disconnects from irc
        self.twitch_bot = None
        self.launch_twitch = False

    def endApplication(self):
        self.running = 0
        self.twitch_bot = None
        unloadDisplay()

    

q = tk.Tk()
q.title('Launchpad Display')
q.geometry("320x280")

client = ThreadedClient(q)

try:
    q.mainloop()
except:
    client.endApplication()
