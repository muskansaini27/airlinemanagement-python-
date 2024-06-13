from tkinter import *
import datetime as dt
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
import cx_Oracle
swap_count = 0

def Signup():
    global swap_count
    swap_count += 1
    if swap_count > 5:
       Signup.destroy()
       return
    def clear():
        emailEntry.delete(0, END)
        UsernameEntry.delete(0, END)
        PasswordEntry.delete(0, END)
        confirmpasswordEntry.delete(0, END)
        check.set(0)

    def login_page():
        Signup.destroy()
        Login()

    def connect_database():
        if emailEntry.get() == '' or UsernameEntry.get() == '' or PasswordEntry.get() == '' or confirmpasswordEntry.get() == '':
            messagebox.showerror('Error', 'All Fields are Required')
        elif PasswordEntry.get() != confirmpasswordEntry.get():
            messagebox.showerror('Error', 'Password mismatch')
        elif '@' and '.com' not in emailEntry.get():
            messagebox.showinfo('Error', 'Enter valid email\n For example-abc@gmail.com,abc@yahoo.com')
        elif check.get() == 0:
            messagebox.showerror('Error', 'Please accept our terms and services')
        else:
            conn = cx_Oracle.connect(user='airline', password='mmmk')
            cur = conn.cursor()
            # if user already exists
            query = f"select * from data where username=:1"
            cur.execute(query, (UsernameEntry.get(),))
            row = cur.fetchone()
            if row != None:
                messagebox.showerror('Error', 'User already exists,Please change your username')
            else:
                # to insert new user
                a = f"insert into data(email,username,password) values('{emailEntry.get()}','{UsernameEntry.get()}','{PasswordEntry.get()}')"
                cur.execute(a)
                conn.commit()
                cur.close()
                conn.close()
                messagebox.showinfo('Success', 'You have successfully registered')
                clear()
                Signup.destroy()
                import signin

    # GUI part
    Signup = Tk()
    Signup.geometry("1279x600+50+100")
    Signup.resizable(False, False)
    Signup.title("Signup Page")

    # Adding Image
    bgimg = ImageTk.PhotoImage(file='login1.jpg')
    bgLabel = Label(Signup, image=bgimg)
    bgLabel.place(x=0, y=0)

    # adding frame
    Frame_login = Frame(Signup, bg="white", highlightbackground='dodger blue', highlightthickness=2, )
    Frame_login.place(x=490, y=70, height=500, width=350)
    # Adding labels and Entry fields for email
    # heading=Label(Signup,text='CREATE AN ACCOUNT',font=("Impact",28,"bold"),bg='deeppink',fg='grey1')
    heading = Label(Signup, text='CREATE AN ACCOUNT', font=("Open Sans", 20, "bold"), bg='dodger blue', fg='yellow')
    heading.place(x=500, y=100)

    # adding label and entry fiel for email
    emailEntry = StringVar()
    email = Label(Signup, text="Email", font=("RBNO2 Light Light", 12, 'bold'), fg="dodger blue", bg="white")
    email.place(x=500, y=170)
    emailEntry = Entry(Signup, width=27, font=('Monotype', 11), bd=2, fg='black', bg="white", )
    emailEntry.place(x=520, y=200)

    # adding label and entry fiel for username
    UsernameEntry = StringVar()
    Username = Label(Signup, text="Username", font=("Open sans", 12, 'bold'), fg="dodger blue", bg="white")
    Username.place(x=500, y=235)
    UsernameEntry = Entry(Signup, width=27, font=('Monotype', 11), bd=2, fg='black', bg="white")
    UsernameEntry.place(x=520, y=260)

    # aading label and entry fiel for Password
    PasswordEntry = StringVar()
    Password = Label(Signup, text="Password", font=("Open sans", 12, 'bold'), fg="dodger blue", bg="white")
    Password.place(x=500, y=300)
    PasswordEntry = Entry(Signup, width=27, font=('Monotype', 11), bd=2, fg='black', bg="white", show='*')
    PasswordEntry.place(x=520, y=325)

    # aading label and entry fiel for confirmPassword
    confirmpassword = Label(Signup, text="ConfirmPassword", font=("Open sans", 12, 'bold'), fg="dodger blue",
                            bg="white")
    confirmpassword.place(x=500, y=360)
    confirmpasswordEntry = Entry(Signup, width=27, font=('Monotype', 11), bd=2, fg='black', bg="white", show='*')
    confirmpasswordEntry.place(x=520, y=390)

    # check Button
    check = IntVar()
    terms = Checkbutton(Signup, text='I agree to the Terms and Conditions',
                        font=('Microsoft Yahei UI Light', 11, 'bold'), fg='red',
                        bg='white', activebackground="white", activeforeground="red", cursor='hand2', variable=check)
    terms.place(x=500, y=420)

    # SignUp Button
    signupbutton = Button(Signup, text="Sign Up", font=('Microsoft Yahei UI Light', 12, 'bold'), bd=0, width=25,
                          fg="white", bg="dodger blue",
                          activebackground="dodger blue", activeforeground="white", cursor='hand2',
                          command=connect_database)
    signupbutton.place(x=520, y=470)

    # label and login button
    alreadyaccount = Label(Signup, text="Already Have an account?", font=("Open Sans", 11, "bold"), bg='white',
                           fg='red')
    alreadyaccount.place(x=520, y=530)
    Loginbutton = Button(Signup, text='Login', font=('Open Sans', 9, 'bold underline'), bd=0, fg='blue', bg='white',
                         activeforeground='blue',
                         activebackground='white', cursor='hand2', width=10, command=login_page)
    Loginbutton.place(x=720, y=530)

    Signup.mainloop()


def Login():
 global swap_count
 swap_count += 1
 if swap_count > 5:
    LoginPage.destroy()
    return
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
     Signup()


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


Signup()
Login()



