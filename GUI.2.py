from tkinter import*
from tkinter import filedialog

window=Tk()

window.geometry("500x600")
def newfile():
    global t2
    t2=Text(window)
    t2.pack()

def savefile():
    # f=filedialog.asksaveasfilename()
    f=filedialog.asksaveasfile()

    f.write(t2.get("0.0",END))
    t2.get("0.0",END)
        

def openfile():
    f=filedialog.askopenfile()
    t1=Text(window)
    t1.pack()
    t1.insert("0.0",f.read())


menubar=Menu(window,tearoff=0)
filemenu=Menu(menubar)
menubar.add_cascade(label="File",menu=filemenu)

filemenu.add_command(label="new File",command=newfile)
filemenu.add_command(label="Open File",command=openfile)
filemenu.add_command(label="Save File",command=savefile)
filemenu.add_command(label="Close File")
filemenu.add_command(label="new Folder")
filemenu.add_command(label="Save Folder")
filemenu.add_command(label="Close Folder")


helpmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="help",menu=helpmenu)

helpmenu.add_command(label="About")



window.config(menu=menubar)

window.mainloop()