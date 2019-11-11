import os
opath="/home/rene/PycharmProjects/OmniScript/others/"
if not os.path.isdir(opath):
    os.system("mkdir "+opath)
name = input("Name of shortcut: ")
command = input("Command to execute: ")
os.system("touch "+opath + name+".py")
short = open(opath+name+".py","a+")
short.write("import os\n")
short.write("os.system(\""+ command +"\")")
