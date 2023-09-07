from tkinter import *
import time
from tkinter import messagebox
import os
import smtplib
from email.message import EmailMessage
from random import randint

menu_selection =Tk()
menu_selection.title("Menu Options")
menu_selection.geometry("250x350")

color_white='#FFFFFF'
color0='#e1e1e1'
color1='#d1d1d1'
color2='#c1c1c1'
color3='#b1b1b1'
color4='#a1a1a1'
color5='#919191'

class NewWindow(Toplevel):
    def __init__(self, master = None, menu_type = None):
        super().__init__(master = master)
        self.title(menu_type)
        self.geometry("500x560")
        title_frame = Frame(self, width=500, height=60, bd=8, relief="raised")
        title_frame.place(x=0, y=0)
        title_frame.pack_propagate(False)
        
        menu_title = Label(title_frame, text =menu_type, font=("Comic Sans ms", 26))
        menu_title.pack()
       
        pluhmoment = StringVar()
        pluhmoment2 = StringVar()
        pluhmoment3 = StringVar()

        pizzer_frame = Frame(self, width=500, height=500, bd=8, relief="raise")
        pizzer_frame.place(x=0, y=60)
        pizzer_frame.grid_propagate(False)
       
        pizzer_label = Label(pizzer_frame,text="Cheeseburger..............$15.00", font=("Comic Sans ms", 20))
        pizzer_label.grid(row=0, column=0)

        pizzer_label_amount = Label(pizzer_frame, text="Amount: ", font=("Comic Sans ms", 20))
        pizzer_label_amount.place(x=0, y=40)

        cheeseburger_more_button = Entry(self, text="Enter amount", font=("Comic Sans ms", 12), borderwidth=2, width=4, textvariable=pluhmoment)
        cheeseburger_more_button.place(x=120, y=120)

        blank_label = Label(pizzer_frame, text  = " ")
        blank_label.grid(row=2, column=0)

        blank_label_2 = Label(pizzer_frame, text  = " ")
        blank_label_2.grid(row=3, column=0)

        cheezuborgir = Label(pizzer_frame,text="Hamburger...................$15.00", font=("Comic Sans ms", 20))
        cheezuborgir.place(x=0, y=85)

        cheezuborgir_amount = Label(self, text="Amount: ", font=("Comic Sans ms", 20))
        cheezuborgir_amount.place(x=10, y=200)

        cheezuborgir_more_button = Entry(self, text="Enter amount", font=("Comic Sans ms", 12), borderwidth=2, width=4, textvariable=pluhmoment2)
        cheezuborgir_more_button.place(x=120, y=210)

        blank_label = Label(pizzer_frame, text  = " ")
        blank_label.grid(row=5, column=0)

        blank_label_2 = Label(pizzer_frame, text  = " ")
        blank_label_2.grid(row=6, column=0)

        blank_label_3 = Label(pizzer_frame, text  = " ")
        blank_label_3.grid(row=7, column=0)

        blank_label_4 = Label(pizzer_frame, text  = " ")
        blank_label_4.grid(row=8, column=0)

        cheezuborgir = Label(pizzer_frame,text="Vegan Burger..............$15.00", font=("Comic Sans ms", 20))
        cheezuborgir.place(x=0, y=180)

        cheezuborgir_amount = Label(self, text="Amount: ", font=("Comic Sans ms", 20))
        cheezuborgir_amount.place(x=10, y=290)

        cheezuborgir_more_button = Entry(self, text="Enter amount", font=("Comic Sans ms", 12), borderwidth=2, width=4, textvariable=pluhmoment3)
        cheezuborgir_more_button.place(x=120, y=300)

        blank_label_3a = Label(pizzer_frame, text  = " ")
        blank_label_3a.grid(row=9, column=0)

        blank_label_4a = Label(pizzer_frame, text  = " ")
        blank_label_4a.grid(row=10, column=0)

        cheezuborgira = Label(pizzer_frame,text="Chicken Deluxe..............$15.00", font=("Comic Sans ms", 20))
        cheezuborgira.place(x=0, y=275)

        cheezuborgir_amounta = Label(self, text="Amount: ", font=("Comic Sans ms", 20))
        cheezuborgir_amounta.place(x=10, y=385)

        cheezuborgir_more_buttona = Entry(self, text="Enter amount", font=("Comic Sans ms", 12), borderwidth=2, width=4, textvariable=pluhmoment3)
        cheezuborgir_more_buttona.place(x=120, y=395)

        blank_label_3b = Label(pizzer_frame, text  = " ")
        blank_label_3b.grid(row=11, column=0)

        blank_label_4b = Label(pizzer_frame, text  = " ")
        blank_label_4b.grid(row=12, column=0)

        cheezuborgirab = Label(pizzer_frame,text="Fish Burger..............$15.00", font=("Comic Sans ms", 20))
        cheezuborgirab.place(x=0, y=370)

        cheezuborgir_amountab = Label(self, text="Amount: ", font=("Comic Sans ms", 20))
        cheezuborgir_amountab.place(x=10, y=480)

        cheezuborgir_more_buttonab = Entry(self, text="Enter amount", font=("Comic Sans ms", 12), borderwidth=2, width=4, textvariable=pluhmoment3)
        cheezuborgir_more_buttonab.place(x=120, y=490)

class NewWindow2(Toplevel):
    def __init__(self, master = None, menu_type = None):
        super().__init__(master = master)
        self.title(menu_type)
        self.geometry("500x560")
       
        title_frame = Frame(self, width=500, height=60, bd=8, relief="raised")
        title_frame.place(x=0, y=0)
        title_frame.pack_propagate(False)

        menu_title = Label(title_frame, text =menu_type, font=("Comic Sans ms", 26))
        menu_title.pack()
       
        pluhmoment = StringVar()
        pluhmoment2 = StringVar()
        pluhmoment3 = StringVar()
        pluhmoment4 = StringVar()
        pluhmoment5 = StringVar()

        pizzer_frame = Frame(self, width=500, height=500, bd=8, relief="raise")
        pizzer_frame.place(x=0, y=60)
        pizzer_frame.grid_propagate(False)
       
        pizzer_label = Label(pizzer_frame,text="Carbonara..............$15.00", font=("Comic Sans ms", 20))
        pizzer_label.grid(row=0, column=0)

        pizzer_label_amount = Label(pizzer_frame, text="Amount: ", font=("Comic Sans ms", 20))
        pizzer_label_amount.place(x=0, y=40)

        cheeseburger_more_button = Entry(self, text="Enter amount", font=("Comic Sans ms", 12), borderwidth=2, width=4, textvariable=pluhmoment)
        cheeseburger_more_button.place(x=120, y=120)

        blank_label = Label(pizzer_frame, text  = " ")
        blank_label.grid(row=2, column=0)

        blank_label_2 = Label(pizzer_frame, text  = " ")
        blank_label_2.grid(row=3, column=0)

        cheezuborgir = Label(pizzer_frame,text="Ravioli.....................$15.00", font=("Comic Sans ms", 20))
        cheezuborgir.place(x=0, y=85)

        cheezuborgir_amount = Label(self, text="Amount: ", font=("Comic Sans ms", 20))
        cheezuborgir_amount.place(x=10, y=200)

        cheezuborgir_more_button = Entry(self, text="Enter amount", font=("Comic Sans ms", 12), borderwidth=2, width=4, textvariable=pluhmoment2)
        cheezuborgir_more_button.place(x=120, y=210)

        blank_label = Label(pizzer_frame, text  = " ")
        blank_label.grid(row=5, column=0)

        blank_label_2 = Label(pizzer_frame, text  = " ")
        blank_label_2.grid(row=6, column=0)

        blank_label_3 = Label(pizzer_frame, text  = " ")
        blank_label_3.grid(row=7, column=0)

        blank_label_4 = Label(pizzer_frame, text  = " ")
        blank_label_4.grid(row=8, column=0)

        cheezuborgir = Label(pizzer_frame,text="Linguini...................$15.00", font=("Comic Sans ms", 20))
        cheezuborgir.place(x=0, y=180)

        cheezuborgir_amount = Label(self, text="Amount: ", font=("Comic Sans ms", 20))
        cheezuborgir_amount.place(x=10, y=290)

        cheezuborgir_more_button = Entry(self, text="Enter amount", font=("Comic Sans ms", 12), borderwidth=2, width=4, textvariable=pluhmoment3)
        cheezuborgir_more_button.place(x=120, y=300)

        blank_label_3 = Label(pizzer_frame, text  = " ")
        blank_label_3.grid(row=9, column=0)

        blank_label_4 = Label(pizzer_frame, text  = " ")
        blank_label_4.grid(row=10, column=0)

        cheezuborgir2 = Label(pizzer_frame,text="Penne.......................$15.00", font=("Comic Sans ms", 20))
        cheezuborgir2.place(x=0, y=275)

        cheezuborgir_amount2 = Label(self, text="Amount: ", font=("Comic Sans ms", 20))
        cheezuborgir_amount2.place(x=10, y=385)

        cheezuborgir_more_button2 = Entry(self, text="Enter amount", font=("Comic Sans ms", 12), borderwidth=2, width=4, textvariable=pluhmoment4)
        cheezuborgir_more_button2.place(x=120, y=395)
        blank_label_3 = Label(pizzer_frame, text  = " ")
        blank_label_3.grid(row=9, column=0)

        blank_label_4 = Label(pizzer_frame, text  = " ")
        blank_label_4.grid(row=10, column=0)

        cheezuborgir2 = Label(pizzer_frame,text="Spaghetti...............$15.00", font=("Comic Sans ms", 20))
        cheezuborgir2.place(x=0, y=370)

        cheezuborgir_amount2 = Label(self, text="Amount: ", font=("Comic Sans ms", 20))
        cheezuborgir_amount2.place(x=10, y=480)

        cheezuborgir_more_button2 = Entry(self, text="Enter amount", font=("Comic Sans ms", 12), borderwidth=2, width=4, textvariable=pluhmoment5)
        cheezuborgir_more_button2.place(x=120, y=490)

burger_button = Button(menu_selection, text="Burger >", padx=15, pady=10, background=color1)
burger_button.pack(pady=5)
TP_button = Button(menu_selection, text="Traditional Pasta >", padx=15, pady=10, background=color2)
TP_button.pack(pady=5)

burger_button.bind("<Button>", lambda e: NewWindow(menu_selection, "BURGERS"))

TP_button.bind("<Button>", lambda e: NewWindow2(menu_selection, "TRADITIONAL PASTA"))

menu_selection.mainloop()


# Chimkin Deluxe
# Fish Borgir
