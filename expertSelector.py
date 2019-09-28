import tkinter as tk
from tkinter import filedialog
from tkinter import *
import tkinter.messagebox
import random


def random_list(start,stop,length):
    if length >= 0:
        length=int(length)
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    random_list = []
    #抽取随机数，并保证随机数中没有重复的数字
    while len(random_list) < length:
        flag = True
        ran = random.randint(start, stop)
        for i in range(len(random_list)):
            if ran == random_list[i]:
                flag = False
        if flag == True:
             random_list.append(ran)

    return random_list

def openfile():
    #打开选择文件窗口
    file_path = filedialog.askopenfilename()
    #print(file_path)
    res.set(file_path)
    #导入专家姓名数据
    processFile()

def processFile():
    file = res.get()
    #清空列表变量
    expertList.clear()
    listb.delete(0, END)
    resImport.set('')

    #print(file)
    #逐行读取文件，并将文件内容写入列表变量中
    with open(file, 'r') as f:
        for line in f.readlines():
            content = line.strip()
            expertList.append(content)
    resImport.set(str(len(expertList)))
    #将专家信息写入列表控件中
    for i in range(len(expertList)):
        name = str(i+1)+'、'+expertList[i]
        listb.insert(END, name)


def expertSelector():
    #取抽取专家数量
    n = resNumber.get()
    if int(n) > len(expertList) :
        tk.messagebox.showinfo(title='错误', message='抽取专家数不能大于专家总数！')
        return
    #清空listbox原有数据
    listb2.delete(0, END)
    #print(n)
    l = random_list(1,len(expertList),int(n))
    #print(l)
    for i in range(len(l)):
        s = l[i]
        name = str(s)+'、'+expertList[s-1]
        listb2.insert(END, name)

#申明全局变量
expertList = []
#开始构建窗体
root = tk.Tk()
root.geometry('600x300+500+200')
root.title('专家随机抽取程序')
root.resizable(FALSE, True)
#创建一个标签(选择专家文件)
input_file = Label(root, text='专家文件：',font=('黑体',12),fg='blue')
#让标签显示
input_file.grid(row=0, column=0,sticky='W')
res = StringVar()
input_entry = Entry(root, width=55, textvariable=res)
input_entry.grid(row=0, column=1,columnspan=3,sticky='W')
resImport = StringVar()
resImport.set('')
input_entry = Entry(root, width=6, textvariable=resImport)
input_entry.grid(row=0, column=4)
lb = Label(root, text='人',font=('黑体',9), fg='blue')
lb.grid(row=0, column=4,sticky='e')
#创建一个标签（抽取专家数量）
input_file = Label(root, text='抽取专家数量：',font=('黑体',12),fg='blue')
#让标签显示
input_file.grid(row=1, column=0,sticky='W')
resNumber = StringVar()
input_entry = Entry(root, width=8, textvariable=resNumber)
input_entry.grid(row=1, column=1,sticky='W')
#button = Button(root, text='选择专家文件', width=10, command=openfile)
#button.grid(row=2, column=3)
#画按钮
button = Button(root, text='导入专家文件', width=12, command=openfile, padx=2, pady=2)
button.grid(row=1, column=2)
button = Button(root, text='随机专家抽取', width=12, command=expertSelector, padx=2, pady=2)
button.grid(row=1, column=3)
#画两个列表控件
lb = Label(root, text='导入专家列表',font=('黑体',10),fg='blue')
lb.grid(row=2, column=1)
lb = Label(root, text='抽中专家列表',font=('黑体',10),fg='blue')
lb.grid(row=2, column=3)
#  创建两个列表组件
listb  = Listbox(root)
listb.grid(row=4, column=1)
scroll_1 = Scrollbar(root, command=listb.yview)
listb.configure(yscrollcommand=scroll_1.set)
scroll_1.grid(row=4, column=1, sticky=N+S+E)

listb2 = Listbox(root,selectmode='multiple')
listb2.grid(row=4, column=3)
scroll_2 = Scrollbar(root, command=listb2.yview)
listb2.configure(yscrollcommand=scroll_2.set)
scroll_2.grid(row=4, column=3, sticky=N+S+E)
#打开窗口
root.mainloop()


