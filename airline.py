from tkinter import *
import datetime as dt
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
import cx_Oracle
#Functionality

def ticket_click():
   if IDEntry.get()=='' or  passEntry.get()=='' or flightEntry.get()=='' or seatEntry.get()=='' or mobEntry.get()=='' or addressEntry.get()=='' or statusEntry.get()=='':
      messagebox.showerror('Error',"All fields are required")
   else:
      conn = cx_Oracle.connect(user='airline', password='mmmk')
      cur = conn.cursor()
      a = f"insert into passenger1 values('{IDEntry.get() }','{passEntry.get()}','{flightEntry.get()}','{seatEntry.get()}','{mobEntry.get()}','{addressEntry.get()}','{statusEntry.get()}')"
      cur.execute(a)
      conn.commit()
      messagebox.showinfo('Success', 'Your Ticket has been Booked')
      cur.close()
      conn.close()


# To check Availability of Flights
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



#For Booking Ticket
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
   bgImage = ImageTk.PhotoImage(file="tr1.jpg")
   bgLabel = Label(window, image=bgImage)
   bgLabel.place(x=0, y=0)

   heading = Label(window, text='Book your Flights ', font=("impact", 50), fg='black',bg="skyblue",borderwidth=4,relief="solid")
   heading.place(x=50, y=60)
   """openeye = PhotoImage(file='images56.png')
   eyeButton = Button(window, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2',)
   eyeButton.place(x=800, y=150)"""

   Frame_login=Frame(window, bg="Black", highlightbackground='black', highlightthickness=5)
   Frame_login.place(x=680, y=40, height=430, width=450)
   #Frame_login.attributes("-transparentcolor","black")
   label=Label(window,text="Passenger Id",font=('monotype 12 bold'),foreground='black',background='white',width=15,bd=3)
   label.place(x=700,y=60)
   IDEntry = Entry(window, width=20 ,font=('Microsoft Yahei UI Light', 11, 'bold'), bd=2, fg='black')
   IDEntry.place(x=930, y=60)

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


# get_ticket function
def display():
    conn = cx_Oracle.connect(user='airline', password='mmmk')
    cur = conn.cursor()
    query = "select pass_no from passenger1 where pass_no=:1"
    cur.execute(query, (IDEntry.get(),))
    row = cur.fetchone()
    if row == None:
          messagebox.showerror('Error', 'Invalid Passenger Id')
    else:
          #a=f"Select flightno,source,destination,departuretime,arrivaltime,flight_no,pass_name,class from flights ,passenger where flights.flightno=passenger.flight_no"
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


def cancelflight():
   conn = cx_Oracle.connect(user='airline', password='mmmk')
   cur = conn.cursor()
   query2="Select pass_no from passenger1 where pass_no=:1 and pass_name=:2"
   cur.execute(query2,(passnoEntry.get(),passnameEntry.get()))
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


def cancel_flight():
   window=Toplevel()
   window.geometry("1279x600+50+100")
   window.resizable(False, False)
   window.title('Cancel reservation')
   bgImage = ImageTk.PhotoImage(file="cancel1.jpg")
   bgLabel = Label(window, image=bgImage)
   bgLabel.place(x=0, y=0)
   #openeye = PhotoImage(file='cancelled1.png')
   #eyeButton = Button(window, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2',)
   #eyeButton.place(x=700, y=150)
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




airline=Tk()
#airline.geometry("1279x1392+0+0")
airline.geometry("1279x600+50+100")
airline.resizable(False,False)
airline.title("Airlines")

bgImage=ImageTk.PhotoImage(file="aeroplane4.jpg")
bgLabel=Label(airline,image=bgImage)
bgLabel.place(x=0,y=0)

def close_win():
   messagebox.showinfo("Success",'Thank you for visiting😊')
   airline.destroy()

airline.protocol("WM_DELETE_WINDOW", close_win)


date=dt.datetime.now()
label=Label(airline,text=f"{date:%A,%B,%d,%Y}",font="Calibri,20,bold",fg="black")
label.place(x=1000,y=550)


heading=Label(airline,text='Welcome to Spark Airlines',font=("Impact",30,"bold underline"),fg='black',bg="turquoise2")
heading.place(x=400,y=10)

#Frame_login=Frame(airline,bg="white",highlightbackground='black',highlightthickness=5)
#Frame_login.place(x=120,y=90,height=400,width=350)

#back_login=Button(airline,text='Back to Login',font=("Open Sans",10,'bold' ),fg='white',bg='black',activebackground="black",activeforeground="white",command=Back_login)
#back_login.place(x=240,y=450)

Button_1=Button(airline,text='Available flights',font=('monotype 12 bold'),bg='white',fg='black',activebackground='white',activeforeground='black',command=Avail_flight)
Button_1.place(x=150,y=150,width=270,height=50)
Button_2=Button(airline,text='Book flight',font=('monotype 12 bold'),bg='white',fg='black',activebackground='white',activeforeground='black',command=book_ticket)
Button_2.place(x=150,y=220,width=270,height=50)
Button_3=Button(airline,text='Get Ticket',font=('monotype 12 bold'),bg='white',fg='black',activebackground='white',activeforeground='black',command=get_ticket)
Button_3.place(x=150,y=290,width=270,height=50)
Button_3=Button(airline,text='Cancel flights',font=('monotype 12 bold'),bg='white',fg='black',activebackground='white',activeforeground='black',command=cancel_flight)
Button_3.place(x=150,y=360,width=270,height=50)

airline.mainloop()
