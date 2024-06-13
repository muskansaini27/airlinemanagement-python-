from tkinter import *
import datetime as dt
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
from importlib import reload
import cx_Oracle


window=Tk()
window.geometry("1279x600+50+100")
window.resizable(False, False)
window.title('Get ticket')
bgImage = ImageTk.PhotoImage(file="down.jpg")
bgLabel = Label(window, image=bgImage)
bgLabel.place(x=0, y=0)



headingLabel = Label(window, text="Spark Airlines-Ticket Window", font=("Impact", 20), bg='white',fg='black',
                        width=29, bd=2, height=2)
headingLabel.place(x=800, y=50)
getticketButton = Button(window, text='Get Ticket', font=('Open Sans', 16, 'bold'), bd=0, fg='white', bg='blue',
                         activeforeground='white',
                         activebackground='blue', cursor='hand2', width=10)
getticketButton.place(x=490,y=30)
   # for passenger id
passIDLabel = Label(window, text="Enter your passenger ID", font=("Open sans", 15), fg='black', bg='white',
                       width=20, bd=2)
passIDLabel.place(x=80, y=30)
IDEntry = Entry(window, width=6, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
IDEntry.place(x=380, y=30)

# Inside Frame

frame2 = Frame(window, bg="blue", highlightthickness=4)
frame2.place(x=50, y=100, height=440, width=580)

   # for passenger name
passnameLabel = Label(window, text="Passenger Name", font=("Open sans", 15), fg='black', bg='white', width=20,
                         bd=2)
passnameLabel.place(x=80, y=120)
nameEntry = Entry(window, width=15, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
nameEntry.place(x=350, y=120)

   # for passenger flight no
flightno_Label = Label(window, text="Flight No", font=("Open sans", 15), fg='black', bg='white', width=20, bd=2)
flightno_Label.place(x=80, y=170)
flightnoEntry = Entry(window, width=15, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
flightnoEntry.place(x=350, y=170)

# for passenger seat no

seatLabel = Label(window, text="Seat No", font=("Open sans", 15), fg='black', bg='white', width=20, bd=2)
seatLabel.place(x=80, y=220)
seatEntry = Entry(window, width=15, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
seatEntry.place(x=350, y=220)

# for flight name

flightnameLabel = Label(window, text="Flight Name", font=("Open sans", 15), fg='black', bg='white', width=20,
                           bd=2)
flightnameLabel.place(x=80, y=270)
flight_nameEntry = Entry(window, width=15, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
flight_nameEntry.place(x=350, y=270)

# for source

sourceLabel = Label(window, text="Source", font=("Open sans", 15), fg='black', bg='white', width=20, bd=2)
sourceLabel.place(x=80, y=320)
sourceEntry = Entry(window, width=15, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
sourceEntry.place(x=350, y=320)

# for destination

destinationLabel = Label(window, text="Destination", font=("Open sans", 15), fg='black', bg='white', width=20,
                            bd=2)
destinationLabel.place(x=80, y=370)
destinationEntry = Entry(window, width=15, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
destinationEntry.place(x=350, y=370)

departureLabel = Label(window, text="Departure Time ", font=("Open sans", 15), fg='black', bg='white', width=20,
                          bd=2)
departureLabel.place(x=80, y=420)
dtimeEntry = Entry(window, width=15, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
dtimeEntry.place(x=350, y=420)

# for arrivaltime

arrivaLabel = Label(window, text="Arrival Time", font=("Open sans", 15), fg='black', bg='white', width=20, bd=2)
arrivaLabel.place(x=80, y=470)
atimeEntry = Entry(window, width=15, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
atimeEntry.place(x=350, y=470)



window.mainloop()
