"""from tkinter import *
LoginPage=Tk()
LoginPage.geometry("1279x600+50+100")
LoginPage.resizable(False,False)
LoginPage.title("Login Page")
#Placing Image
bgImage=ImageTk.PhotoImage(file="login1.jpg")
bgLabel=Label(LoginPage,image=bgImage)
bgLabel.place(x=0,y=0)

def signup_page():
    newwindow=Toplevel(signup)
    LoginPage.destroy()
    import signup
LoginPage.mainloop()"""

import tkinter as tk
from PIL import ImageTk
from tkinter import *
from tkinter import ttk      #treeview is in ttk
import cx_Oracle


conn=cx_Oracle.connect("airline/mmmk")
cur=conn.cursor()
print(conn.version)

sql="select* from data order by id"
cur.execute(sql)
rows=cur.fetchall()




win=Tk()
#bgImage = ImageTk.PhotoImage(file="air.jpg")
#bgLabel = Label(win, image=bgImage)
#bgLabel.place(x=0, y=0)

frame=Frame(win)
frame.pack(side=tk.LEFT,padx=20)


tv=ttk.Treeview(frame,columns=(1,2,3,4),show="headings",height="30")
tv.grid(row=1,column=1,columnspan=3,padx=30,pady=10)
tv.column(1 ,anchor=CENTER,width=80)
tv.heading(1,text="ID",anchor=CENTER)
tv.heading(2,text="Email",anchor=CENTER)
tv.heading(3,text="Username",anchor=CENTER)
tv.heading(4,text="Password",anchor=CENTER)

for i in rows:
    tv.insert('','end',values=i)


style=ttk.Style(win)
style.theme_use('clam')

style.configure("Treeview",background="grey",foreground="black",font=("Times",12,'normal'),rowheight=70,fieldbackground="red")
style.configure("Treeview.Heading",background='red')


win.title("student data")
#win.geometry("650x500")
win.geometry("1279x600+50+100")
#win.resizable(False,False)




win.mainloop()
