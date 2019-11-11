import os,sys
from tkinter import filedialog
from tkinter import *
opath="/home/rene/PycharmProjects/OmniScript/others/"
name = ""
if not os.path.isdir(opath):
    os.system("mkdir "+opath)
if len(sys.argv) > 1:
    filename = sys.argv[1]
    data = filename[:-3].split('/')
    os.system("cp "+filename+" "+opath+ data[len(data) - 1]+".py")
    name = data[len(data) - 1]
else:
    root = Tk()
    root.filename = filedialog.askopenfilename(initialdir="/home", title="Select file",
                                               filetypes=(("python scripts", "*.py"), ("all files", "*.*")))
    data = root.filename[:-3].split('/')
    os.system("cp "+root.filename+" "+opath+ data[len(data) - 1]+".py")
    name = data[len(data) - 1]
print("added "+name)