
import os
import sys
from tkinter import filedialog
from tkinter import *
path="/home/rene/PycharmProjects/OmniScript/src/"
opath="/home/rene/PycharmProjects/OmniScript/others/"
print("Omni Script for python script execution")
#print("ARGS: "+ str(sys.argv))
if len(sys.argv) < 2:
    print("Omni -h for help")
elif "-h" == sys.argv[1]:
    print("setup: add scripts with the setup option or call already added scripts with each name.\n"
          "edit: Edit this or other Scripts manually with the edit option")
    print("list: List scripts with the list option")
    print("remove: Remove scripts with the remove option")
    print("shortcut: Add Shortcut-scripts with the shortcut option")
elif "setup" == sys.argv[1] and len(sys.argv) <= 2:
    os.system("python3.7 "+path+"setup.py")
elif "setup" == sys.argv[1] and len(sys.argv) == 3:
    os.system("python3.7 "+path+"setup.py " + sys.argv[2])
elif "edit" == sys.argv[1] and len(sys.argv) <= 2:
    os.system("nano "+path+"Omni.py")
elif "edit" == sys.argv[1]:
    os.system("nano "+opath+ sys.argv[2]+".py")
elif "shortcut" == sys.argv[1]:
    os.system("python3.7 "+path+"shortcut.py")
elif "list" == sys.argv[1]:
    print("contains:")
    print("    setup")
    print("    shortcut")
    files = []
    for r,d,f in os.walk(opath):
        for file in f:
            if '.py' in file:
                files.append(file)
    for f in files:
        if f != "Omni.py":
            print("    "+f[:-3])
elif "remove" == sys.argv[1]:
    if sys.argv[2] == "setup":
        print("Action prohibited")
    elif sys.argv[2] == "Omni":
        print("Action prohibited")
    elif sys.argv[2] == "shortcut":
        print("Action prohibited")
    else:
        os.system("rm "+opath+ sys.argv[2]+".py")
        print("removed " + sys.argv[2])
else:
    os.system("python3.7 "+opath + sys.argv[1] +".py")
