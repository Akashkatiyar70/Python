###  GUI(Graphical user interface)

##Interface -->  Interaction plateform

## Interface Two Types
         # 1. CLI(Cammand line InterFace)
         # 2. GUI(Graphical User interface)

## GUI Application type
          ## Desktop  --> (tkinter) python libraries
          ## mobile   --> (kivy)
          ## web      --> (flask,Django)


from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox,filedialog

# layout create use this class --> Tk()
window=Tk()

window.title('My Application')
window.configure(bg="green")

window.geometry("400x400")

# img=PhotoImage(file=r"C:\Users\akash\Downloads\hellopay-removebg-preview.png")
photo=Image.open(r"C:\Users\akash\Downloads\horizon-call-of-the-3840x2160-10426.jpg")
  
photo=photo.resize((160,200))

img1=ImageTk.PhotoImage(photo)



window.iconphoto(False,img1)


# Label(window,text="Hello I am Akash katiyar").pack(side="bottom")

# logo=PhotoImage(file=r"C:\Users\akash\Downloads\horizon-call-of-the-3840x2160-10426.jpg")



# Label(window,text="python").pack()
# Label(window,image=img).pack(side="bottom")


# Label(window,text="python").grid(row=0,column=0)
# Label(window,text="Hii i am akash").grid(row=1,column=1)

## ==>  pack and grid not use same time

# Label(window,text="python",fg="green",bg="yellow").place(x=100,y=100)
# Label(window,text="Hii i am akash",fg="#ffe59b",bg="black").place(x=200,y=200)

Label(window,text="Hii i am akash",fg="green",bg="red",font=("times",20,"bold")).pack()
# # Label(window,text="Hii i am akash",fg="#ffe59b",bg="black",font=("",30,"bold italic ")).pack()

# l1=Label(window)
# l1.pack()
# # l1.config(text="Python",fg="green",bg="yellow",font=("times",20,"bold"))
# l1.config(text="Java",fg="green",bg="yellow",font=("times",20,"bold"))

# Label(window,image=img1).pack()
     
# def submit():
#   l1.config(text="Python",fg="green",bg="yellow",font=("times",20,"bold"))
    

# Button(window,text="Insert",command=submit).pack()
# Button(window,text="exit",command=exit).pack()


Frame1=Frame(window)
Frame1.pack()
Label(Frame1,text="Name:").pack(side="left")
e1=Entry(Frame1)
e1.pack(side="right")

Frame2=Frame(window)
Frame2.pack()
Label(Frame2,text="Contact:").pack(side="left")
e2=Entry(Frame2)
e2.pack(side="right")

#                                                        #using text to insert data
Frame3=Frame(window)
Frame3.pack()
Label(Frame3,text="Address:").pack(side="left")
s=Scrollbar(Frame3)
s.pack(side="right",fill=Y)
t1=Text(Frame3,height=6,width=15)
t1.pack(side="right")
s.config(command=t1.yview)

#                                                              # create radiobutton 
Frame4=Frame(window)
Frame4.pack()
Label(Frame4,text="Gender:").pack(side="left")

# var=IntVar()
var=StringVar()


r1=Radiobutton(Frame4,text="Male",variable=var,value="male")
r1.pack(side="right")

r2=Radiobutton(Frame4,text="feMale",variable=var,value="female")
r2.pack(side="right")


#                                                              # create checkButton
Frame5=Frame(window)
Frame5.pack()
Label(Frame5,text="course:").pack(side="left")

var1=IntVar()

c1=Checkbutton(Frame4,text="sqp",variable=var1)
c1.pack(side="right")

var2=IntVar()

c2=Checkbutton(Frame4,text="Python",variable=var2)
c2.pack(side="right")

#                                                                  ## Create optionMenu

Frame6=Frame(window)
Frame6.pack()
Label(Frame6,text="State:").pack(side="left")

options=['up','Delhi','Haryana',"Punjab",'Mp','Himanchal',"Uttrakhand"]
var3=StringVar()
opt1=OptionMenu(Frame6,var3,*options)
opt1.pack(side="right")








## adding button in frame
def submit():
  print(e1.get())
  print(e2.get())
  print(t1.get("0.0",END))
  print(var.get())
  print(var1.get(),var2.get())
  print(var3.get())

  #                                        information show function
  if e1.get()=="":
    messagebox.showerror("Error","Submission Failed")
  else:
     messagebox.showinfo("Success","Submitted Succesfully")
#                                                           ## exit and close ask function
def close():
  if messagebox.askokcancel("Exit","Confirm Exit??"):
    exit()
  else:
    pass

frame=Frame(window)
frame.pack()
Button(frame,text="Insert",command=submit,bg="red",fg="white",width=12).pack(side="right")
Button(frame,text="exit",command=close,bg="green",fg="white",width=12).pack(side="left")



window.mainloop()



## GUI Controls

    # Label --> show your output
           # Text
           # Image
    # Button
    #Entry
    #Text
    #Frame
    #RadioButton
    #CheckButton
    #optionMenu
    #Menu
                                            ####   Scrollbar

                                            # Frame3=Frame(window)
                                            # Frame3.pack()
                                            # Label(Frame3,text="Address:").pack(side="left")
                                            # s=Scrollbar(Frame3)
                                            # s.pack(side="right",fill=Y)
                                            # t1=Text(Frame3,height=6,width=15)
                                            # t1.pack(side="right")

                                            # s.config(command=t1.yview)


    #MessageBox  ==> it is madules and import in Tkinter(from tkinter import messagebox,filledialog)
    #filedialog

##  Placing Functions
  # pack(side=)
  # grid(row=,column=)
  # place(x=,y=)



## variable class
 ## IntVar()     --> default values(0)
 ## doubleVar()   --> default values(0.0)
 ## stringVar()   --> default values("")
 ## BooleanVar()   --> default values(False)













