import tkinter as tk
from tkinter import Label, Button
import time
localtime = time.asctime(time.localtime(time.time()))
#outer structure of app
class app1:
    def __init__(self,top):
        self.top=top
        top.title("Restaurant Management")
        top.geometry("1028x500")
        top.configure(background="#091833")

        #pre define fonts 
        font10="{Courier New}10 normal"
        font11="{U.S. 101} 25 bold"
        font12="Al-aramco 11 bold"
        font13="{Courier New} 10 bold"
        font14="{serge UI} 15 bold"
        font15="Arial 13 bold"
        font16="{segoe UI} 13 bold"

        self.Label1=tk.Label(master=top,text="Restaurant Management System",background="#091833",font=font11,foreground="#f2a343")
        self.Label1.place(relx=0.268,rely=0.02,height=51,width=507)
        localtime1 = Label(master=top,text=localtime,background="#091833",font=font16,foreground="steel blue")
        localtime1.place(relx=0.420,rely=0.12)
        #labels for food items
        self.Label2=tk.Label(master=top,text="Order Num :",background="#091833",font=font12,foreground="white")
        self.Label2.place(relx=0.054,rely=0.25)
        self.Label2=tk.Label(master=top,text="Friend Potato :",background="#091833",font=font12,foreground="white")
        self.Label2.place(relx=0.038,rely=0.32)
        self.Label2=tk.Label(master=top,text="Chk Burger :",background="#091833",font=font12,foreground="white")
        self.Label2.place(relx=0.051,rely=0.4)
        self.Label2=tk.Label(master=top,text="Big King :",background="#091833",font=font12,foreground="white")
        self.Label2.place(relx=0.071,rely=0.48)
        self.Label2=tk.Label(master=top,text="Chk Royal :",background="#091833",font=font12,foreground="white")
        self.Label2.place(relx=0.060,rely=0.56)
        self.Label2=tk.Label(master=top,text="Veg Salad :",background="#091833",font=font12,foreground="white")
        self.Label2.place(relx=0.058,rely=0.64)
        self.Label2=tk.Label(master=top,text="Drinks :",background="#091833",font=font12,foreground="white")
        self.Label2.place(relx=0.08,rely=0.71)

        #entry food
        self.entry1=tk.Entry(master=top,background="#d9d9d9",foreground="#c60000",selectbackground="#f2a343",font=font13)
        self.entry1.place(relx=0.18,rely=0.25)
        self.entry1=tk.Entry(master=top,background="#d9d9d9",foreground="#c60000",selectbackground="#f2a343",font=font13)
        self.entry1.place(relx=0.18,rely=0.32)
        self.entry1=tk.Entry(master=top,background="#d9d9d9",foreground="#c60000",selectbackground="#f2a343",font=font13)
        self.entry1.place(relx=0.18,rely=0.4)
        self.entry1=tk.Entry(master=top,background="#d9d9d9",foreground="#c60000",selectbackground="#f2a343",font=font13)
        self.entry1.place(relx=0.18,rely=0.48)
        self.entry1=tk.Entry(master=top,background="#d9d9d9",foreground="#c60000",selectbackground="#f2a343",font=font13)
        self.entry1.place(relx=0.18,rely=0.56)
        self.entry1=tk.Entry(master=top,background="#d9d9d9",foreground="#c60000",selectbackground="#f2a343",font=font13)
        self.entry1.place(relx=0.18,rely=0.63)
        self.entry1=tk.Entry(master=top,background="#d9d9d9",foreground="#c60000",selectbackground="#f2a343",font=font13)
        self.entry1.place(relx=0.18,rely=0.71)

        #calc
        self.entry1=tk.Entry(master=top,background="#d9d9d9",foreground="#c60000",selectbackground="#f2a343",font=font13)
        self.entry1.place(relx=0.705,rely=0.24,height=35,relwidth=0.267)

        self.Button1=tk.Button(master=top,text='''7''',background="#122c63",font=font14,foreground="#ffffff",borderwidth='0')
        self.Button1.place(relx=0.705,rely=0.34,height=44,width=67)
        self.Button1=tk.Button(master=top,text='''8''',background="#122c63",font=font14,foreground="#ffffff",borderwidth='0')
        self.Button1.place(relx=0.780,rely=0.34,height=44,width=67)
        self.Button1=tk.Button(master=top,text='''9''',background="#122c63",font=font14,foreground="#ffffff",borderwidth='0')
        self.Button1.place(relx=0.856,rely=0.34,height=44,width=67)
        self.Button1=tk.Button(master=top,text='''/''',background="#122c63",font=font14,foreground="#ffffff",borderwidth='0')
        self.Button1.place(relx=0.934,rely=0.34,height=44,width=37)

        self.Button1=tk.Button(master=top,text='''4''',background="#122c63",font=font14,foreground="#ffffff",borderwidth='0')
        self.Button1.place(relx=0.705,rely=0.44,height=44,width=67)
        self.Button1=tk.Button(master=top,text='''5''',background="#122c63",font=font14,foreground="#ffffff",borderwidth='0')
        self.Button1.place(relx=0.780,rely=0.44,height=44,width=67)
        self.Button1=tk.Button(master=top,text='''6''',background="#122c63",font=font14,foreground="#ffffff",borderwidth='0')
        self.Button1.place(relx=0.856,rely=0.44,height=44,width=67)
        self.Button1=tk.Button(master=top,text='''*''',background="#122c63",font=font14,foreground="#ffffff",borderwidth='0')
        self.Button1.place(relx=0.934,rely=0.44,height=44,width=37)


        self.Button1=tk.Button(master=top,text='''1''',background="#122c63",font=font14,foreground="#ffffff",borderwidth='0')
        self.Button1.place(relx=0.705,rely=0.54,height=44,width=67)
        self.Button1=tk.Button(master=top,text='''2''',background="#122c63",font=font14,foreground="#ffffff",borderwidth='0')
        self.Button1.place(relx=0.780,rely=0.54,height=44,width=67)
        self.Button1=tk.Button(master=top,text='''3''',background="#122c63",font=font14,foreground="#ffffff",borderwidth='0')
        self.Button1.place(relx=0.856,rely=0.54,height=44,width=67)
        self.Button1=tk.Button(master=top,text='''-''',background="#122c63",font=font14,foreground="#ffffff",borderwidth='0')
        self.Button1.place(relx=0.934,rely=0.54,height=44,width=37)


        self.Button1=tk.Button(master=top,text='''0''',background="#122c63",font=font14,foreground="#ffffff",borderwidth='0')
        self.Button1.place(relx=0.705,rely=0.64,height=44,width=145)
        self.Button1=tk.Button(master=top,text='''.''',background="#122c63",font=font14,foreground="#ffffff",borderwidth='0')
        self.Button1.place(relx=0.856,rely=0.64,height=44,width=67)
        self.Button1=tk.Button(master=top,text='''+''',background="#122c63",font=font14,foreground="#ffffff",borderwidth='0')
        self.Button1.place(relx=0.934,rely=0.64,height=44,width=37)
        self.Button1=tk.Button(master=top,text='''=''',background="#f2a343",font=font14,foreground="#ffffff",borderwidth='0')
        self.Button1.place(relx=0.705,rely=0.74,height=34,width=272)
        
        #---Cost---
        self.Label2=tk.Label(master=top,text="Cost :",background="#091833",font=font12,foreground="#f2a343")
        self.Label2.place(relx=0.40,rely=0.32)

        self.Label2=tk.Label(master=top,text="Tax :",background="#091833",font=font12,foreground="white")
        self.Label2.place(relx=0.4,rely=0.4)
        self.Label2=tk.Label(master=top,text="Service charge :",background="#091833",font=font12,foreground="white")
        self.Label2.place(relx=0.35,rely=0.48)
        self.Label2=tk.Label(master=top,text="Subtotal :",background="#091833",font=font12,foreground="white")
        self.Label2.place(relx=0.38,rely=0.56)
        self.Label2=tk.Label(master=top,text="Total :",background="#091833",font=font12,foreground="white")
        self.Label2.place(relx=0.40,rely=0.64)

        #--entry cost--
        self.entry3=tk.Entry(master=top,background="#d9d9d9",foreground="#c60000",selectbackground="#f2a343",font=font13)
        self.entry3.place(relx=0.467,rely=0.32)
        self.entry1=tk.Entry(master=top,background="#d9d9d9",foreground="#c60000",selectbackground="#f2a343",font=font13)
        self.entry1.place(relx=0.467,rely=0.4)
        self.entry1=tk.Entry(master=top,background="#d9d9d9",foreground="#c60000",selectbackground="#f2a343",font=font13)
        self.entry1.place(relx=0.467,rely=0.48)
        self.entry1=tk.Entry(master=top,background="#d9d9d9",foreground="#c60000",selectbackground="#f2a343",font=font13)
        self.entry1.place(relx=0.467,rely=0.56)
        self.entry1=tk.Entry(master=top,background="#d9d9d9",foreground="#c60000",selectbackground="#f2a343",font=font13)
        self.entry1.place(relx=0.466,rely=0.64)





root=tk.Tk()
my_gui=app1(root)
root.mainloop()