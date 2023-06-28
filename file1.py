from tkinter import*
import tkinter.messagebox
top =Tk()
top.geometry("600x300")
name: Label(top, text="Print id:").place(x= 20,y=40)
fathersName: Label(top, text="Print model:").place(x=20,y=80)
motherName: Label(top , text="company name:").place(x=20,y=120)
    
def CallBack():
    tkinter.messagebox.showinfo("Message", "Your data is submitted")
submit: Button(top, text="SUBMIT",command=CallBack).place(x=30,y=240)
e1=Entry(top).place(x=120,y=40)
e2=Entry(top).place(x=120,y=80)
e3=Entry(top).place(x=120,y=120)

top.mainloop()