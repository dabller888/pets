#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   HttpApiTest.py
@Time    :   2020/06/30 22:43:45
@Author  :   iceld 
@Version :   1.0
@Contact :   dabller888@163.com
@License :   (C)Copyright 2020-2022
@Desc    :   None
'''


# here put the import lib

# PySide Kivy Tkinter PyGui WxPython PyQt

from ctypes import *
from tkinter import *
from tkinter import ttk
import json
import requests
from bs4 import BeautifulSoup
import re

from tkinter.messagebox import *
import tkinter.messagebox

root = Tk()

winWidth = 600
winHeight = 500
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

x = int((screenWidth - winWidth) / 2)
y = int((screenHeight - winHeight) / 2)

root.title('API Test Tool v1.0')
# root.geometry("600x500+10+20")
root.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
# root.iconbitmap("./image/icon.ico")
# root.resizable(False, False)
root.resizable(0, 0)

txt = StringVar()

def init():

    _url = 'https://xxx/api/'
    txt.set(_url+'User/login')

    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'application/json'
    }
    txtHeader.delete(0.0, END)
    txtHeader.insert('insert', json.dumps(headers, indent=4))
    
    kv = {
        'username':	'admin',
        'password':	'123456'
    }
    txtParams.delete(0.0, END)
    txtParams.insert('insert', json.dumps(kv, indent=4))


def execFun():
    try:
        data = json.loads(txtParams.get(0.0, END))
        headers = json.loads(txtHeader.get(0.0, END))
        r = requests.request(method=cboxMethod.get(),
                             url=txtUrl.get(), params=data, headers=headers)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        content = r.text
        # print(r.request.headers)
        print(r.content)
        print(content)
        # txtRes.insert('insert', content)
        txtRes.delete(0.0, END)
        txtRes.insert(1.0, content)
    except Exception as ex:
        showinfo('message box', '执行错误：'+str(ex))


def changeFun(event):
    print(cboxMethod.get())


# title
Label(root, text='API Test Tool', font=(
    "微软雅黑", 20)).grid(row=0, column=0, columnspan=2, sticky='s')

lblUrl = Label(root, text='Url: ', width=6)

frame0 = Frame(root)
txtUrl = Entry(frame0,  textvariable=txt, width=50)
cboxMethod = ttk.Combobox(frame0, width=5)
btnExec = Button(frame0, text='execute', command=execFun)

frame0.grid(row=1, column=1, sticky='w')
lblUrl.grid(row=1, column=0)
txtUrl.grid(row=1, column=0)
cboxMethod.grid(row=1, column=1)
btnExec.grid(row=1, column=2)

cboxMethod['value'] = ['GET', 'POST', 'DELETE', 'PUT', 'HEAD', 'PATCH']
cboxMethod.current(0)

cboxMethod.bind("<<ComboboxSelected>>", changeFun)

# header
lblHeader = Label(root, text='Header: ')
txtHeader = Text(root, height=6)
lblHeader.grid(row=2, column=0)
txtHeader.grid(row=2, column=1, columnspan=1, sticky='w')

# parameters
lblParams = Label(root, text='Params: ')
txtParams = Text(root, height=6)
lblParams.grid(row=3, column=0)
txtParams.grid(row=3, column=1, columnspan=1, sticky='w')

# output
tab = ttk.Notebook(root)
frame1 = Frame(tab, bg="gray",  height=180)

txtRes = Text(frame1, bg='white')
tab1 = tab.add(frame1, text="Output")

frame2 = Frame(tab, bg="gray")
tab2 = tab.add(frame2, text="Raw")

frame3 = Frame(tab, bg="gray")
tab3 = tab.add(frame3, text="TextView")
tab.grid(row=4, column=0, columnspan=2, sticky='w')
txtRes.grid(row=4, column=0, columnspan=2)
# tab.pack(expand = True, fill = BOTH)
tab.select(frame1)

init()

root.mainloop()
