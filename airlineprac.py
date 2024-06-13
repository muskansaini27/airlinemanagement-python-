from tkinter import *
import datetime as dt
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
import cx_Oracle
#Functionalities
# To check Availability of Flights in user(treeview):
def Avail_flight():
   conn=cx_Oracle.connect("airline/mmmk")
   cur=conn.cursor()
   print(conn.version)

   sql="select* from flights" 
   cur.execute(sql)
   rows=cur.fetchall()
   win=Tk()
   frame=Frame(win)
   frame.pack(side=LEFT)


   tv=ttk.Treeview(frame,columns=(1,2,3,4,5,6,7,8,9,10),show="headings",height="50")
   tv.grid(row=1,column=1,columnspan=2,padx=0,pady=10)
   tv.column(1 ,anchor=CENTER,width=170)
   tv.heading(1,text="FlightNo")
   tv.column(2, anchor=CENTER, width=170)
   tv.heading(2,text="Flightname")
   tv.column(3, anchor=CENTER, width=170)
   tv.heading(3,text="Source")
   tv.column(4, anchor=CENTER, width=170)
   tv.heading(4,text="Destination")
   tv.column(5, anchor=CENTER, width=100)
   tv.heading(5, text="Departure Time")
   tv.column(6, anchor=CENTER, width=100)
   tv.heading(6, text="Arrival Time", anchor=CENTER)
   tv.column(7, anchor=CENTER, width=100)
   tv.heading(7, text="Fare")
   tv.column(8, anchor=CENTER, width=100)
   tv.heading(8, text="Filled seats")
   tv.column(9, anchor=CENTER, width=80)
   tv.heading(9, text="Empty seats")
   tv.column(10, anchor=CENTER, width=100)
   tv.heading(10, text="Date")


   for i in rows:
     tv.insert('','end',values=i)

   style=ttk.Style(win)
   style.theme_use('clam')

   style.configure("Treeview",background="silver",foreground="black",font=("Times",12,'normal'),rowheight=30,fieldbackground="powderblue")
   style.map('Treeview',background=[('selected','grey')])
   style.configure("Treeview.Heading",background='cyan3')
   win.title("Flight details")
   win.geometry("1279x600+50+100")
   win.mainloop()


# for booking ticket in Database:
def ticket_click():
   if IDEntry.get()=='' or  passEntry.get()=='' or flightEntry.get()=='' or seatEntry.get()=='' or mobEntry.get()=='' or addressEntry.get()=='' or statusEntry.get()=='':
      messagebox.showerror('Error',"All fields are required")
   else:
      conn = cx_Oracle.connect(user='airline', password='mmmk')
      cur = conn.cursor()
      a = f"insert into passenger1 values('{IDEntry.get() }','{passEntry.get()}',TO_DATE('{flightEntry.get()}', 'YYYY-MM-DD'),'{seatEntry.get()}','{mobEntry.get()}','{addressEntry.get()}','{statusEntry.get()}')"
      cur.execute(a)
      conn.commit()                                                  
      messagebox.showinfo('Success', 'Your Ticket has been Booked')
      cur.close()
      conn.close()

#For Booking Ticket in user:
def book_ticket():
   window=Toplevel()
   window.geometry("1279x600+50+100")
   window.resizable(False, False)
   window.title('Book ticket')
   global IDEntry
   global passEntry
   global flightEntry
   global seatEntry
   global mobEntry
   global addressEntry
   global  statusEntry

   
   # Generate a unique passenger ID using uuid
   import uuid
   unique_passenger_id = str(uuid.uuid4().int)[:3]

   bgImage = ImageTk.PhotoImage(file="tr1.jpg")
   bgLabel = Label(window, image=bgImage)
   bgLabel.place(x=0, y=0)

   heading = Label(window, text='Book your Flights ', font=("impact", 50), fg='black',bg="skyblue",borderwidth=4,relief="solid")
   heading.place(x=50, y=60)


   Frame_login=Frame(window, bg="Black", highlightbackground='black', highlightthickness=5)
   Frame_login.place(x=680, y=40, height=430, width=450)

   label=Label(window,text="Passenger Id",font=('monotype 12 bold'),foreground='black',background='white',width=15,bd=3)
   label.place(x=700,y=60)
   IDEntry = Entry(window, width=20 ,font=('Microsoft Yahei UI Light', 11, 'bold'), bd=2, fg='black')
   IDEntry.insert(0, unique_passenger_id)  # Insert the generated ID into the entry widget
   IDEntry.place(x=930 , y=60)

   label = Label(window, text="Passenger Name", font=('monotype 12 bold'),foreground='Black',background='white',width=15,bd=3)
   label.place(x=700, y=110)
   passEntry = Entry(window, width=20, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=2, fg='black')
   passEntry.place(x=930, y=110)

   label = Label(window, text="DOB", font=('monotype 12 bold'), foreground='Black', background='white',width=15,bd=3)
   label.place(x=700, y=160)
   flightEntry = Entry(window, width=20, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=2, fg='black')
   flightEntry.place(x=930, y=160)

   label = Label(window, text="Mobile no", font=('monotype 12 bold'), foreground='Black', background='white',width=15,bd=3)
   label.place(x=700, y=210)
   seatEntry = Entry(window, width=20, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=2, fg='black')
   seatEntry.place(x=930, y=210)

   label = Label(window, text="Address",font=('monotype 12 bold'), foreground='Black', background='white',width=15,bd=3)
   label.place(x=700, y=260)
   mobEntry = Entry(window, width=20, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=2, fg='black')
   mobEntry.place(x=930, y=260)

   label = Label(window, text="Class", font=('monotype 12 bold'), foreground='Black', background='white',width=15,bd=3)
   label.place(x=700, y=310)
   addressEntry = Entry(window, width=20, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=2, fg='black')
   addressEntry.place(x=930, y=310)

   label = Label(window, text="Flight No", font=('monotype 12 bold'), foreground='Black', background='white',width=15,bd=3)
   label.place(x=700, y=360)
   statusEntry = Entry(window, width=20, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=2, fg='black')
   statusEntry.place(x=930, y=360)

   ticketButton = Button(window, text='Book Ticket', font=('Open Sans', 20, 'bold'), bd=0, fg='white', bg='blue',
                        activeforeground='white',
                        activebackground='blue', cursor='hand2', width=15,command=ticket_click)
   ticketButton.place(x=750, y=400)

   window.mainloop()


#  for getting ticket from database:
def display():
    conn = cx_Oracle.connect(user='airline', password='mmmk')
    cur = conn.cursor()
    query = "select pass_no from passenger1 where pass_no=:1"
    cur.execute(query, (IDEntry.get(),))
    row = cur.fetchone()
    if row == None:
          messagebox.showerror('Error', 'Invalid Passenger Id')
    else:
          query = "select pass_name from passenger1 where pass_no=:1"
          cur.execute(query, (IDEntry.get(),))
          rows = cur.fetchone()
          nameEntry.insert(0,rows)
          nameEntry.config(state="disabled")

          a = f"Select flight_no from passenger1 where pass_no=:1"
          cur.execute(a, (IDEntry.get(),))
          rows = cur.fetchone()
          flightnoEntry.insert(0, rows)
          flightnoEntry.config(state="disabled")

          a = f"Select class from passenger1 where pass_no=:1"






          cur.execute(a,(IDEntry.get(),))
          rows = cur.fetchone()
          classEntry.insert(0, rows)
          classEntry.config(state="disabled")


          a=f"Select flights.flightname from flights inner join passenger1 on flights.flightno=passenger1.flight_no where pass_no=:1"
          cur.execute(a,(IDEntry.get(),))
          rows = cur.fetchone()
          flight_nameEntry.insert(0, rows)
          flight_nameEntry.config(state="disabled")

          a = f"Select flights.source from flights inner join passenger1 on flights.flightno=passenger1.flight_no where pass_no=:1"
          cur.execute(a,(IDEntry.get(),))
          rows = cur.fetchone()
          sourceEntry.insert(0, rows)
          sourceEntry.config(state="disabled")

          a = f"Select flights.destination from flights inner join passenger1 on flights.flightno=passenger1.flight_no where pass_no=:1"
          cur.execute(a,(IDEntry.get(),))
          rows = cur.fetchone()
          destinationEntry .insert(0, rows)
          destinationEntry.config(state="disabled")

          a = f"Select flights.departuretime from flights inner join passenger1 on flights.flightno=passenger1.flight_no where pass_no=:1"
          cur.execute(a,(IDEntry.get(),))
          rows = cur.fetchone()
          dtimeEntry.insert(0, rows)
          dtimeEntry.config(state="disabled")

          a = f"Select flights.arrivaltime from flights inner join passenger1 on flights.flightno=passenger1.flight_no where pass_no=:1"
          cur.execute(a,(IDEntry.get(),))
          rows = cur.fetchone()
          atimeEntry.insert(0, rows)
          atimeEntry.config(state="disabled")

          a = f"Select flights.f_date from flights inner join passenger1 on flights.flightno=passenger1.flight_no where pass_no=:1"
          cur.execute(a, (IDEntry.get(),))
          rows = cur.fetchone()
          dateEntry.insert(0, rows)
          dateEntry.config(state="disabled")

    cur.close()
    conn.close()

# frontend part of get Ticket:
def get_ticket():
   window=Toplevel()
   window.geometry("1279x600+50+100")
   window.resizable(False, False)
   window.title('Get ticket')
   bgImage = ImageTk.PhotoImage(file="ticket.jpg")
   bgLabel = Label(window, image=bgImage)
   bgLabel.place(x=0, y=0)


   global IDEntry
   global nameEntry
   global flightnoEntry
   global classEntry
   global dtimeEntry
   global flight_nameEntry
   global sourceEntry
   global destinationEntry
   global atimeEntry
   global dateEntry
   headingLabel = Label(window, text="Spark Airlines-Ticket Window", font=("Impact", 20), bg='white',fg='black',
                        width=29, bd=2, height=2)
   headingLabel.place(x=800, y=50)
   getticketButton = Button(window, text='Get Ticket', font=('Open Sans', 16, 'bold'), bd=0, fg='white', bg='blue',
                         activeforeground='white',
                         activebackground='blue', cursor='hand2', width=10,command=display)
   getticketButton.place(x=530,y=30)
   # for passenger id
   passIDLabel = Label(window, text="Enter your passenger ID", font=("Open sans", 15), fg='black', bg='white',
                       width=20, bd=2)
   passIDLabel.place(x=80, y=30)
   IDEntry = Entry(window, width=10, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
   IDEntry.place(x=380, y=30)

   # Inside Frame

   frame2 = Frame(window, bg="black", highlightthickness=4)
   frame2.place(x=50, y=100, height=480, width=600)

   headingLabel = Label(window, text="Spark Airlines-Ticket Window", font=("arial", 25, "bold"), bg='gray55',
                        fg='white',
                        width=24, borderwidth=4, relief="solid", height=2)
   headingLabel.place(x=770, y=50)

   # for passenger name
   nameEntry=StringVar()
   passnameLabel = Label(window, text="Passenger Name", font=("Open sans", 15), fg='black', bg='white', width=20,
                         bd=2)
   passnameLabel.place(x=80, y=120)
   nameEntry = Entry(window, width=20, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
   nameEntry.place(x=350, y=120)

   # for passenger flight no
   flightnoEntry=StringVar()
   flightno_Label = Label(window, text="Flight No", font=("Open sans", 15), fg='black', bg='white', width=20, bd=2)
   flightno_Label.place(x=80, y=170)
   flightnoEntry = Entry(window, width=20, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
   flightnoEntry.place(x=350, y=170)

   # for passenger class
   classEntry=StringVar()
   classLabel = Label(window, text="Class", font=("Open sans", 15), fg='black', bg='white', width=20, bd=2)
   classLabel.place(x=80, y=220)
   classEntry = Entry(window, width=20, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
   classEntry.place(x=350, y=220)

   # for flight name
   flight_nameEntry=StringVar()
   flightnameLabel = Label(window, text="Flight Name", font=("Open sans", 15), fg='black', bg='white', width=20,
                           bd=2)
   flightnameLabel.place(x=80, y=270)
   flight_nameEntry = Entry(window, width=20, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
   flight_nameEntry.place(x=350, y=270)

   # for source
   sourceEntry=StringVar()
   sourceLabel = Label(window, text="Source", font=("Open sans", 15), fg='black', bg='white', width=20, bd=2)
   sourceLabel.place(x=80, y=320)
   sourceEntry = Entry(window, width=20, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
   sourceEntry.place(x=350, y=320)

   # for destination
   destinationEntry=StringVar()
   destinationLabel = Label(window, text="Destination", font=("Open sans", 15), fg='black', bg='white', width=20,
                            bd=2)
   destinationLabel.place(x=80, y=370)
   destinationEntry = Entry(window, width=20, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
   destinationEntry.place(x=350, y=370)

   # for departure time
   dtimeEntry=StringVar()
   departureLabel = Label(window, text="Departure Time ", font=("Open sans", 15), fg='black', bg='white', width=20,
                          bd=2)
   departureLabel.place(x=80, y=420)
   dtimeEntry = Entry(window, width=20, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
   dtimeEntry.place(x=350, y=420)

   # for arrivaltime
   atimeEntry=StringVar()
   arrivaLabel = Label(window, text="Arrival Time", font=("Open sans", 15), fg='black', bg='white', width=20, bd=2)
   arrivaLabel.place(x=80, y=470)
   atimeEntry = Entry(window, width=20, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
   atimeEntry.place(x=350, y=470)

   dateEntry = StringVar()
   dateLabel = Label(window, text="Date", font=("Open sans", 15), fg='black', bg='white', width=20, bd=2)
   dateLabel.place(x=80, y=520)
   dateEntry = Entry(window, width=20, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
   dateEntry.place(x=350, y=520)



   window.mainloop()

#for cancelling ticket database part:
def cancelflight():
   conn = cx_Oracle.connect(user='airline', password='mmmk')
   cur = conn.cursor()
   query2="Select pass_no from passenger1 where pass_no=:1 "
   cur.execute(query2,(passnoEntry.get(),))
   row = cur.fetchone()
   if passnoEntry.get()=='' or passnameEntry.get()=='':
      messagebox.showerror('Error','PLease fill all the Fields')
   else:
    if row == None:
      messagebox.showerror('Error', 'Invalid Passenger Id or Passenger Name')
    else:
      query1 = "Delete from passenger1 where pass_no=:1"
      cur.execute(query1,(passnoEntry.get(),))
      conn.commit()
      messagebox.showinfo('success','your ticket has been cancelled')

   cur.close()
   conn.close()

#frontend of cancel ticket:
def cancel_flight():
   window=Toplevel()
   window.geometry("1279x600+50+100")
   window.resizable(False, False)
   window.title('Cancel reservation')
   bgImage = ImageTk.PhotoImage(file="cancel1.jpg")
   bgLabel = Label(window, image=bgImage)
   bgLabel.place(x=0, y=0)

   global passnoEntry
   global passnameEntry
   Frame_login = Frame(window, bg="turquoise", highlightbackground='black', highlightthickness=5)
   Frame_login.place(x=80,y=80,height=250,width=450)



   passno_label = Label(window, text="Passenger ID", font=('monotype 15 bold'), foreground='Black',background='white',width=15)
   passno_label.place(x=100, y=120)
   passnoEntry = Entry(window, width=15, font=('Microsoft Yahei UI Light', 15, 'bold'), bd=2, fg='black')
   passnoEntry.place(x=300, y=120)

   passname_label = Label(window, text="Passenger Name", font=('monotype 15 bold'), foreground='Black', background='white',
                        width=15)
   passname_label.place(x=100, y=190)
   passnameEntry = Entry(window, width=15, font=('Microsoft Yahei UI Light', 15, 'bold'), bd=2, fg='black')
   passnameEntry.place(x=300, y=190)

   CancelButton = Button(window, text='Cancel Ticket', font=('Open Sans', 16, 'bold'), bd=0, fg='white', bg='blue',
                         activeforeground='white',
                         activebackground='blue', cursor='hand2', width=15,command=cancelflight)
   CancelButton.place(x=230, y=250)

   window.mainloop()

#Login Page
def main_page():
    def clear():
        emailEntry.delete(0, END)
        UsernameEntry.delete(0, END)
        PasswordEntry.delete(0, END)
        confirmpasswordEntry.delete(0, END)
        check.set(0)

    def login_page():
        def clear():
            usernameEntry.delete(0, END)
            password.delete(0, END)
# database part for Login window
        def Login_user():
            if usernameEntry.get() == '' or password.get() == '':
                messagebox.showerror('Error', 'All fields are required')
            elif usernameEntry.get() == 'Username' or password.get() == 'Password':
                messagebox.showerror('Error', 'All fields are required')
            else:
                conn = cx_Oracle.connect(user='airline', password='mmmk')
                cur = conn.cursor()
                query = "select * from data where username=:1 and password=:2"
                cur.execute(query, (usernameEntry.get(), password.get()))

                row = cur.fetchone()
                if row == None:
                    messagebox.showerror('Error', 'Invalid Username or Password')
                    clear()
                else:
                    messagebox.showinfo('Success', 'Login Successful')
                    # user main part
                    airline = Toplevel()
                    airline.geometry("1279x600+50+100")
                    airline.resizable(False, False)
                    airline.title("Airlines")

                    bgImage = ImageTk.PhotoImage(file="aeroplane4.jpg")
                    bgLabel = Label(airline, image=bgImage)
                    bgLabel.place(x=0, y=0)



                    date = dt.datetime.now()
                    label = Label(airline, text=f"{date:%A,%B,%d,%Y}", font="Calibri,20,bold", fg="black")
                    label.place(x=1000, y=550)

                    heading = Label(airline, text='Welcome to Spark Airlines', font=("Impact", 30, "bold underline"),
                                    fg='black', bg="turquoise2")
                    heading.place(x=400, y=10)


                    Button_1 = Button(airline, text='Available flights', font=('monotype 12 bold'), bg='white',
                                      fg='black', activebackground='white', activeforeground='black',
                                      command=Avail_flight)
                    Button_1.place(x=150, y=150, width=270, height=50)
                    Button_2 = Button(airline, text='Book flight', font=('monotype 12 bold'), bg='white', fg='black',
                                      activebackground='white', activeforeground='black', command=book_ticket)
                    Button_2.place(x=150, y=220, width=270, height=50)
                    Button_3 = Button(airline, text='Get Ticket', font=('monotype 12 bold'), bg='white', fg='black',
                                      activebackground='white', activeforeground='black', command=get_ticket)
                    Button_3.place(x=150, y=290, width=270, height=50)
                    Button_3 = Button(airline, text='Cancel Ticket', font=('monotype 12 bold'), bg='white', fg='black',
                                      activebackground='white', activeforeground='black', command=cancel_flight)
                    Button_3.place(x=150, y=360, width=270, height=50)

                    airline.mainloop()


        def on_userentry(event):
            if usernameEntry.get() == 'Username':
                usernameEntry.delete(0, END)

        def on_passentry(event):
            if password.get() == 'Password':
                password.delete(0, END)

        def hide():
            openeye.config(file='m.png')
            password.config(show='*')
            eyeButton.config(command=show)

        def show():
            openeye.config(file='mm.png')
            password.config(show='')
            eyeButton.config(command=hide)



        # GUI Part
        LoginPage = Toplevel()
        LoginPage.geometry("1279x600+50+100")
        LoginPage.resizable(False, False)
        LoginPage.title("Login Page")
        p1 = PhotoImage(file="login.png")
        LoginPage.iconphoto(False, p1)
        # Placing Image
        bgImage = ImageTk.PhotoImage(file="login1.jpg")
        bgLabel = Label(LoginPage, image=bgImage)
        bgLabel.place(x=0, y=0)

        # Adding Frame
        Frame_login = Frame(LoginPage, bg="white", highlightbackground='dodger blue', highlightthickness=2)
        Frame_login.place(x=490, y=70, height=400, width=350)
        # Adding Label
        heading = Label(LoginPage, text='LOGIN PAGE', font=("Impact", 30, "bold"), bg='white', fg='dodger blue')
        heading.place(x=550, y=100)

        # Entry Field for username
        usernameEntry = Entry(LoginPage, width=27, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0,
                              fg='dodger blue')
        usernameEntry.place(x=530, y=200)
        usernameEntry.insert(0, 'Username')
        # frame for line
        usernameEntry.bind('<FocusIn>', on_userentry)
        Frame(LoginPage, width=250, height=2, bg='dodger blue').place(x=530, y=222)

        # Entry field for password
        password = Entry(LoginPage, width=27, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='dodger blue')
        password.place(x=530, y=280)
        password.insert(0, 'Password')
        password.bind('<FocusIn>', on_passentry)
        Frame(LoginPage, width=250, height=2, bg='dodger blue').place(x=530, y=305)

        # Eye Button
        openeye = PhotoImage(file='mm.png')
        eyeButton = Button(LoginPage, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2',
                           command=hide)
        eyeButton.place(x=750, y=280)



        # Login Button
        LoginButton = Button(LoginPage, text='Login', font=('Open Sans', 16, 'bold'), bd=0, fg='white',
                             bg='dodger blue', activeforeground='white',
                             activebackground='dodger blue', cursor='hand2', width=19, command=Login_user)
        LoginButton.place(x=540, y=385)

        LoginPage.mainloop()
    #signup
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
                #Signup.destroy()
                #import signin

    # GUI part
    Signup = Toplevel()
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

# Treeview of admin:
def check_pass():
    conn = cx_Oracle.connect("airline/mmmk")
    cur = conn.cursor()
    print(conn.version)

    sql = "select * from passenger1"
    cur.execute(sql)
    rows = cur.fetchall()
    win = Tk()
    frame = Frame(win)
    frame.pack(side=LEFT)

    tv = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5, 6, 7), show="headings", height="50")
    tv.grid(row=1, column=1, columnspan=2, padx=0, pady=10)
    tv.column(1, anchor=CENTER, width=170)
    tv.heading(1, text="PassNo")
    tv.column(2, anchor=CENTER, width=170)
    tv.heading(2, text="Passname")
    tv.column(3, anchor=CENTER, width=200)
    tv.heading(3, text="DOB")
    tv.column(4, anchor=CENTER, width=200)
    tv.heading(4, text="Mobile No")
    tv.column(5, anchor=CENTER, width=200)
    tv.heading(5, text="Address")
    tv.column(6, anchor=CENTER, width=200)
    tv.heading(6, text="Class")
    tv.column(7, anchor=CENTER, width=200)
    tv.heading(7, text="Flight No")

    for i in rows:
        tv.insert('', 'end', values=i)

    style = ttk.Style(win)
    style.theme_use('clam')

    style.configure("Treeview", background="silver", foreground="black", font=("Times", 12, 'normal'), rowheight=30,
                    fieldbackground="powderblue")
    style.map('Treeview', background=[('selected', 'grey')])
    style.configure("Treeview.Heading", background='cyan3')
    win.title("Flight details")
    win.geometry("1279x600+50+100")
    win.mainloop()

#for  insert flight database  part
def insertadminflight():
    if NoEntry.get() == '' or nameEntry .get() == '' or SourceEntry .get() == '' or DestinationEntry.get() == '' or DtimeEntry.get() == '' or AtimeEntry.get() == '' or fareEntry.get() == '' or FseatsEntry.get()==''or  EseatsEntry.get()=='' or DateEntry.get()=='':
        messagebox.showerror('Error', "All fields are required")
    else:
        conn = cx_Oracle.connect(user='airline', password='mmmk')
        cur = conn.cursor()
        a = f"insert into flights values('{NoEntry.get()}','{nameEntry.get()}','{SourceEntry .get()}','{DestinationEntry.get()}','{DtimeEntry.get()}','{AtimeEntry.get()}','{fareEntry.get()}','{FseatsEntry.get()}','{EseatsEntry.get()}',TO_DATE('{DateEntry.get()}', 'YYYY-MM-DD'))"
        cur.execute(a)
        conn.commit()
        messagebox.showinfo('Success', 'Flight has been added')
        cur.close()
        conn.close()


# add new flight for admin
def insert_flight():
    window = Toplevel()
    window.geometry("1279x600+50+100")
    window.resizable(False, False)
    window.title('Get ticket')
    bgImage = ImageTk.PhotoImage(file="ticket.jpg")
    bgLabel = Label(window, image=bgImage)
    bgLabel.place(x=0, y=0)

    global NoEntry
    global nameEntry
    global SourceEntry
    global DestinationEntry
    global DtimeEntry
    global AtimeEntry
    global fareEntry
    global FseatsEntry
    global EseatsEntry
    global DateEntry
    headingLabel = Label(window, text="Spark Airlines-Ticket Window", font=("Impact", 20), bg='white', fg='black',
                         width=29, bd=2, height=2)
    headingLabel.place(x=800, y=50)
    # Inside Frame

    frame2 = Frame(window, bg="black", highlightthickness=4)
    frame2.place(x=50, y=50, height=5500, width=600)

    headingLabel = Label(window, text="Spark Airlines", font=("arial", 25, "bold"), bg='gray55',
                         fg='white',
                         width=24, borderwidth=4, relief="solid", height=2)
    headingLabel.place(x=770, y=50)

    NoEntry = StringVar()
    NoLabel = Label(window, text="Flight No", font=("Open sans", 15), fg='black', bg='white', width=20, bd=2)
    NoLabel.place(x=80, y=70)
    NoEntry = Entry(window, width=20, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
    NoEntry.place(x=350, y=70)

    # for passenger name
    nameEntry = StringVar()
    nameLabel = Label(window, text="Flight Name", font=("Open sans", 15), fg='black', bg='white', width=20,
                          bd=2)
    nameLabel.place(x=80, y=120)
    nameEntry = Entry(window, width=20, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
    nameEntry.place(x=350, y=120)

    # for passenger flight no
    SourceEntry = StringVar()
    Source_Label = Label(window, text="Source", font=("Open sans", 15), fg='black', bg='white', width=20, bd=2)
    Source_Label.place(x=80, y=170)
    SourceEntry = Entry(window, width=20, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
    SourceEntry.place(x=350, y=170)

    # for passenger class
    DestinationEntry = StringVar()
    DestinationLabel = Label(window, text="Destination", font=("Open sans", 15), fg='black', bg='white', width=20, bd=2)
    DestinationLabel.place(x=80, y=220)
    DestinationEntry = Entry(window, width=20, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
    DestinationEntry.place(x=350, y=220)

    # for flight name
    DtimeEntry = StringVar()
    DtimeLabel = Label(window, text="Departure time", font=("Open sans", 15), fg='black', bg='white', width=20,
                            bd=2)
    DtimeLabel.place(x=80, y=270)
    DtimeEntry = Entry(window, width=20, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
    DtimeEntry.place(x=350, y=270)

    # for source
    AtimeEntry = StringVar()
    AtimeLabel = Label(window, text="Arrival time", font=("Open sans", 15), fg='black', bg='white', width=20, bd=2)
    AtimeLabel.place(x=80, y=320)
    AtimeEntry = Entry(window, width=20, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
    AtimeEntry.place(x=350, y=320)

    # for destination
    fareEntry = StringVar()
    fareLabel = Label(window, text="Fare", font=("Open sans", 15), fg='black', bg='white', width=20,
                             bd=2)
    fareLabel.place(x=80, y=370)
    fareEntry = Entry(window, width=20, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
    fareEntry.place(x=350, y=370)

    # for departure time
    FseatsEntry = StringVar()
    FseatsLabel = Label(window, text="Filled seats ", font=("Open sans", 15), fg='black', bg='white', width=20,
                           bd=2)
    FseatsLabel.place(x=80, y=420)
    FseatsEntry = Entry(window, width=20, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
    FseatsEntry.place(x=350, y=420)

    # for arrivaltime
    EseatsEntry = StringVar()
    EseatsLabel = Label(window, text="Empty seats", font=("Open sans", 15), fg='black', bg='white', width=20, bd=2)
    EseatsLabel.place(x=80, y=470)
    EseatsEntry = Entry(window, width=20, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
    EseatsEntry.place(x=350, y=470)

    DateEntry = StringVar()
    DateLabel = Label(window, text="Date", font=("Open sans", 15), fg='black', bg='white', width=20, bd=2)
    DateLabel.place(x=80, y=520)
    DateEntry = Entry(window, width=20, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
    DateEntry.place(x=350, y=520)

    Button_2 = Button(window, text='Submit', font=('monotype 12 bold'), bg='blue', fg='white',
                      activebackground='white', activeforeground='black', command=insertadminflight)
    Button_2.place(x=220, y=560, width=270, height=40)

    window.mainloop()

#for admin database cancel flight part
def cancel_flights():
    conn = cx_Oracle.connect(user='airline', password='mmmk')
    cur = conn.cursor()
    query2 = "Select flightno,flightname from flights where flightno=:1 and flightname=:2"
    cur.execute(query2, (flightnoEntry.get(), flightnameEntry.get()))
    row = cur.fetchone()
    if flightnoEntry.get() == '' or flightnameEntry.get() == '':
        messagebox.showerror('Error', 'PLease fill all the Fields')
    else:
        if row == None:
            messagebox.showerror('Error', 'Invalid Flight No or Flight Name')
        else:
            query1 = "Delete from flights where flightno=:1"
            cur.execute(query1, (flightnoEntry.get(),))
            conn.commit()
            messagebox.showinfo('Success', 'The Flight has been cancelled')

    cur.close()
    conn.close()

#for admin cancel flight part:
def delete_flight():
    window = Toplevel()
    window.geometry("1279x600+50+100")
    window.resizable(False, False)
    window.title('Cancel Flight')
    bgImage = ImageTk.PhotoImage(file="cancel1.jpg")
    bgLabel = Label(window, image=bgImage)
    bgLabel.place(x=0, y=0)
    # openeye = PhotoImage(file='cancelled1.png')
    # eyeButton = Button(window, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2',)
    # eyeButton.place(x=700, y=150)
    global flightnoEntry
    global flightnameEntry
    Frame_login = Frame(window, bg="turquoise", highlightbackground='black', highlightthickness=5)
    Frame_login.place(x=80, y=80, height=250, width=450)

    flightno_label = Label(window, text="Flight No", font=('monotype 15 bold'), foreground='Black', background='white',
                         width=15)
    flightno_label.place(x=100, y=120)
    flightnoEntry = Entry(window, width=15, font=('Microsoft Yahei UI Light', 15, 'bold'), bd=2, fg='black')
    flightnoEntry.place(x=300, y=120)

    flightname_label = Label(window, text="Flight Name", font=('monotype 15 bold'), foreground='Black',
                           background='white',
                           width=15)
    flightname_label.place(x=100, y=190)
    flightnameEntry = Entry(window, width=15, font=('Microsoft Yahei UI Light', 15, 'bold'), bd=2, fg='black')
    flightnameEntry.place(x=300, y=190)

    CancelButton = Button(window, text='Cancel Flight', font=('Open Sans', 16, 'bold'), bd=0, fg='white', bg='blue',
                          activeforeground='white',
                          activebackground='blue', cursor='hand2', width=15, command=cancel_flights)
    CancelButton.place(x=230, y=250)

    window.mainloop()

#LOgin  database part of admin
def Login():
    def clear():
        usernameEntry.delete(0, END)
        password.delete(0, END)

    def Login_user():
        if usernameEntry.get() == '' or password.get() == '':
            messagebox.showerror('Error', 'All fields are required')
        elif usernameEntry.get() == 'Username' or password.get() == 'Password':
            messagebox.showerror('Error', 'All fields are required')
        else:
            conn = cx_Oracle.connect(user='airline', password='mmmk')
            cur = conn.cursor()
            query = "select * from admin where username=:1 and password=:2"
            cur.execute(query, (usernameEntry.get(), password.get()))

            row = cur.fetchone()
            if row == None:
                messagebox.showerror('Error', 'Invalid Username or Password')
                clear()
            else:
                messagebox.showinfo('Success', 'Login Successful')
                LoginPage.destroy()
                win1=Toplevel()
                win1.geometry("1279x600+50+100")
                win1.resizable(False, False)
                win1.title("Admin Login")
                bgImage = ImageTk.PhotoImage(file="admin4.jpg")
                bgLabel = Label(win1, image=bgImage)
                bgLabel.place(x=0, y=0)
                frame2 = Frame(win1, bg="pink", highlightthickness=4)
                frame2.place(x=650, y=0, height=900, width=600)
                Button_1 = Button(win1, text='Check all Passengers', font=('monotype 12 bold'), bg='blue', fg='white',
                                  activebackground='white', activeforeground='black',command=check_pass)
                Button_1.place(x=750, y=150, width=270, height=50)
                Button_2 = Button(win1, text='Add new flight', font=('monotype 12 bold'), bg='blue', fg='white',
                                  activebackground='white', activeforeground='black',command=insert_flight)
                Button_2.place(x=750, y=250, width=270, height=50)
                Button_2 = Button(win1, text='Delete Flight', font=('monotype 12 bold'), bg='blue', fg='white',
                                  activebackground='white', activeforeground='black',command=delete_flight)
                Button_2.place(x=750, y=350, width=270, height=50)

                win1.mainloop()


    def on_userentry(event):
        if usernameEntry.get() == 'Username':
            usernameEntry.delete(0, END)

    def on_passentry(event):
        if password.get() == 'Password':
            password.delete(0, END)

    def hide():
        openeye.config(file='m.png')
        password.config(show='*')
        eyeButton.config(command=show)

    def show():
        openeye.config(file='mm.png')
        password.config(show='')
        eyeButton.config(command=hide)


    # GUI Part
    LoginPage = Toplevel()
    LoginPage.geometry("1279x600+50+100")
    LoginPage.resizable(False, False)
    LoginPage.title("Login Page")

    # Placing Image
    bgImage = ImageTk.PhotoImage(file="Ghostlamp.jpg")
    bgLabel = Label(LoginPage, image=bgImage)
    bgLabel.place(x=0, y=0)

    # Adding Frame
    Frame_login2 = Frame(LoginPage, bg="white")
    Frame_login2.place(x=80, y=95, height=30, width=150)

    Frame_login1 = Frame(LoginPage, bg="light seagreen" ,highlightthickness=2)
    Frame_login1.place(x=580, y=0, height=700, width=1500)

    Frame_login = Frame(LoginPage, bg="white", highlightbackground='light seagreen', highlightthickness=2)
    Frame_login.place(x=700, y=90, height=400, width=350)
    # Adding Label
    heading = Label(LoginPage, text='LOGIN PAGE', font=("Impact", 30, "bold"), bg='white', fg='light seagreen')
    heading.place(x=760, y=100)

    # Entry Field for username
    usernameEntry = Entry(LoginPage, width=27, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='light seagreen')
    usernameEntry.place(x=730, y=200)
    usernameEntry.insert(0, 'Username')
    # frame for line
    usernameEntry.bind('<FocusIn>', on_userentry)
    Frame(LoginPage, width=250, height=2, bg='light seagreen').place(x=730, y=222)

    # Entry field for password
    password = Entry(LoginPage, width=27, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='light seagreen')
    password.place(x=730, y=280)
    password.insert(0, 'Password')
    password.bind('<FocusIn>', on_passentry)
    Frame(LoginPage, width=250, height=2, bg='light seagreen').place(x=730, y=305)

    # Eye Button
    openeye = PhotoImage(file='mm.png')
    eyeButton = Button(LoginPage, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2',
                       command=hide)
    eyeButton.place(x=950, y=280)

    # Forget Button
    # ForgetButton=Button(LoginPage,text='Forgot Password?',bd=0,bg='white',fg='red',font=('Microsoft Yahei UI Light',9,'bold underline'),activebackground='white',activeforeground='red',cursor='hand2')
    # ForgetButton.place(x=700,y=320)

    # Login Button
    LoginButton = Button(LoginPage, text='Login', font=('Open Sans', 16, 'bold'), bd=0, fg='white', bg='light seagreen',
                         activeforeground='white',
                         activebackground='light seagreen', cursor='hand2', width=19, command=Login_user)
    LoginButton.place(x=750, y=385)

    LoginPage.mainloop()

def exit_page():
    messagebox.showinfo("Success", 'Thank you for visiting😊')
    air.destroy()


air=Tk()
air.geometry("1279x600+50+100")
air.resizable(False,False)
air.title("Airlines")
bgImage = ImageTk.PhotoImage(file="main.jpg")

def close_win():
    messagebox.showinfo("Success", 'Thank you for visiting😊')
    air.destroy()

air.protocol("WM_DELETE_WINDOW", close_win)

bgLabel = Label(air, image=bgImage)
bgLabel.place(x=0, y=0)
heading = Label(air, text='Sparks Airline', font=("Impact", 30, "bold"), bg='white', fg='dodger blue')
heading.place(x=390, y=30,width=500,height=50)

Button_1=Button(air,text='Admin',font=('monotype 12 bold'),bg='blue',fg='white',activebackground='white',activeforeground='black',command=Login)
Button_1.place(x=500,y=150,width=270,height=50)
Button_2=Button(air,text='User',font=('monotype 12 bold'),bg='blue',fg='white',activebackground='white',activeforeground='black',command=main_page)
Button_2.place(x=500,y=250,width=270,height=50)
Button_2=Button(air,text='Exit',font=('monotype 12 bold'),bg='blue',fg='white',activebackground='white',activeforeground='black',command=exit_page)
Button_2.place(x=500,y=350,width=270,height=50)

air.mainloop()

