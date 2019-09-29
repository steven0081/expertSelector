from tkinter import *
import threading
import queue
import time
from tkinter import ttk
import tkinter as tk


def openfile():
    thread1 = threading.Thread(target=thread1_main)
    thread1.deamon = True
    thread1.start()

shared_queue = queue.Queue()
bar_value = tk.IntVar()

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


def bar_main():
    root = Tk()

    bar = ttk.Progressbar(  root,
                                maximum=3, length=100, variable=bar_value)
    bar.grid(row=0, column=0, sticky="we", padx=5)


# 创建Tk对象，Tk代表窗口
root = Tk()
# 设置窗口标题
root.title('窗口标题')
root.geometry('600x300+500+200')
# 创建Label对象，第一个参数指定该Label放入root
w = Label(root, text="Hello Tkinter!")
# 调用pack进行布局
w.pack()
#加入按钮
button = Button(root, text='导入专家文件', width=12, command=openfile, padx=2, pady=2)
button.pack()

# 启动主窗口的消息循环
root.mainloop()