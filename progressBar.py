import tkinter as tk
from tkinter import ttk

import threading
import queue

import time

shared_queue = queue.Queue()

def thread1_main():
    tot_time = 5 # seconds

    elapsed_time = 0

    while(True):
        time.sleep(1)
        shared_queue.put("I'm working")
        elapsed_time += 1
        if(elapsed_time > tot_time):
            break;

    shared_queue.put("task done")

def updates_progress_bar():
    try:
        msg = shared_queue.get(block=False)
    except queue.Empty:
        msg = None
    else:
        # do update the progress bar here
        delta = 1
        val = bar_value.get()+delta
        val = val if val <= bar["maximum"] else 0
        bar_value.set(val)

    if(msg != "task done"):
        root.after(500, updates_progress_bar)
    else:
        print(msg)

if(__name__ == "__main__"):
    root = tk.Tk()
    root.wm_geometry("200x30")

    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    bar_value = tk.IntVar()
    bar = ttk.Progressbar(  root,
                            maximum=3, length=100, variable=bar_value)
    bar.grid(row=0, column=0, sticky="we", padx=5)

    shared_queue = queue.Queue()
    thread1 = threading.Thread(target=thread1_main)
    thread1.deamon = True
    thread1.start()

    root.after(500, updates_progress_bar)

    root.mainloop()

    print("that's all folks")