import tkinter as tk
from tkinter import filedialog
from tkinter import *
import random


def random_list(start,stop,length):
    if length >= 0:
        length=int(length)
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list

def openfile():
    file_path = filedialog.askopenfilename()
    #print(file_path)
    res.set(file_path)

def processFile():
    file = res.get()
    print(file)
    with open(file, 'r') as f:
        for line in f.readlines():
            content = line.strip()
            expertList.append(content)
    resImport.set('导入专家数量：'+str(len(expertList)))


def expertSelector():
    n= resNumber.get()
    #print(n)
    l = random_list(1,len(expertList),int(n))
    print(l)
    for i in range(len(l)):
        s = l[i]
        print('no:', str(s), expertList[s-1])

expertList = []

root = tk.Tk()
root.geometry('600x300+600+200')
root.title('专家抽取程序')
root.resizable(FALSE, True)
#创建一个标签(选择专家文件)
input_file = Label(root, text='专家文件：',font=('黑体',12),fg='blue')
#让标签显示
input_file.grid(row=0, column=0)
res = StringVar()
input_entry = Entry(root, textvariable=res)
input_entry.grid(row=0, column=1)
resImport = StringVar()
resImport.set('导入专家数量：')
input_entry = Entry(root, textvariable=resImport)
input_entry.grid(row=0, column=3)
#创建一个标签（抽取专家数量）
input_file = Label(root, text='抽取专家数量：',font=('黑体',12),fg='blue')
#让标签显示
input_file.grid(row=1, column=0)
resNumber = StringVar()
input_entry = Entry(root, textvariable=resNumber)
input_entry.grid(row=1, column=1)

button = Button(root, text='选择专家文件', width=10, command=openfile)
button.grid(row=2, column=3)
button = Button(root, text='导入专家', width=10, command=processFile)
button.grid(row=2, column=4)
button = Button(root, text='专家抽取', width=10, command=expertSelector)
button.grid(row=2, column=5)
root.mainloop()
#root.withdraw()

