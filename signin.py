from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import cx_Oracle
#functionality
def clear():
    usernameEntry.delete(0,END)
    password.delete(0,END)


def Login_user():
    if usernameEntry.get()=='' or password.get()=='':
        messagebox.showerror('Error','All fields are required')
    elif usernameEntry.get()=='Username' or password.get()=='Password':
        messagebox.showerror('Error', 'All fields are required')
    else:
        conn=cx_Oracle.connect(user='airline',password='mmmk')
        cur=conn.cursor()
        query="select * from data where username=:1 and password=:2"
        cur.execute(query,(usernameEntry.get(),password.get()))

        row=cur.fetchone()
        if row==None:
            messagebox.showerror('Error', 'Invalid Username or Password')
            clear()
        else:
            messagebox.showinfo('Success', 'Login Successful')
            LoginPage.destroy()
            import airline


def on_userentry(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)
def on_passentry(event):
    if password.get()=='Password':
        password.delete(0,END)
def hide():
    openeye.config(file='m.png')
    password.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='mm.png')
    password.config(show='')
    eyeButton.config(command=hide)

def signup_page():
    LoginPage.destroy()
    import signup


#GUI Part
LoginPage=Tk()
LoginPage.geometry("1279x600+50+100")
LoginPage.resizable(False,False)
LoginPage.title("Login Page")
p1=PhotoImage(file="login.png")
LoginPage.iconphoto(False,p1)

#Placing Image
bgImage=ImageTk.PhotoImage(file="login1.jpg")
bgLabel=Label(LoginPage,image=bgImage)
bgLabel.place(x=0,y=0)

#Adding Frame
Frame_login=Frame(LoginPage,bg="white",highlightbackground='dodger blue',highlightthickness=2)
Frame_login.place(x=490,y=70,height=470,width=350)
#Adding Label
heading=Label(LoginPage,text='LOGIN PAGE',font=("Impact",30,"bold"),bg='white',fg='dodger blue')
heading.place(x=550,y=100)

#Entry Field for username
usernameEntry=Entry(LoginPage,width=27,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='dodger blue')
usernameEntry.place(x=530,y=200)
usernameEntry.insert(0,'Username')
#frame for line
usernameEntry.bind('<FocusIn>',on_userentry)
Frame(LoginPage,width=250,height=2,bg='dodger blue').place(x=530,y=222)

#Entry field for password
password=Entry(LoginPage,width=27,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='dodger blue')
password.place(x=530,y=280)
password.insert(0,'Password')
password.bind('<FocusIn>',on_passentry)
Frame(LoginPage,width=250,height=2,bg='dodger blue').place(x=530,y=305)

#Eye Button
openeye=PhotoImage(file='mm.png')
eyeButton=Button(LoginPage,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=750,y=280)

#Forget Button
#ForgetButton=Button(LoginPage,text='Forgot Password?',bd=0,bg='white',fg='red',font=('Microsoft Yahei UI Light',9,'bold underline'),activebackground='white',activeforeground='red',cursor='hand2')
#ForgetButton.place(x=700,y=320)

#Login Button
LoginButton=Button(LoginPage,text='Login',font=('Open Sans',16,'bold'),bd=0,fg='white',bg='dodger blue',activeforeground='white',
                   activebackground='dodger blue',cursor='hand2',width=19,command=Login_user)
LoginButton.place(x=540,y=385)

#Signup
signuplabel=Label(LoginPage,text="Don't have an Account?",font=("Open Sans",11,"bold"),bg='white',fg='red')
signuplabel.place(x=520,y=480)
newaccountbutton=Button(LoginPage,text='Create new Account',font=('Open Sans',9,'bold underline'),bd=0,fg='blue',bg='white',activeforeground='blue',
                   activebackground='white',cursor='hand2',width=19,command=signup_page)
newaccountbutton.place(x=690,y=480)

LoginPage.mainloop()






