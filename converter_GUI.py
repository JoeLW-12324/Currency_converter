# Importing modules
from tkinter import *
from datetime import date
from btn_cmd import btn_commands
from threading import Thread

# variables
width = 900
height = 500

# function to measure the width or height of the gui to be used for size or placement of frames or buttons
def prct(prct, length):
    return (prct * length) // 100

class GUI():
    # Class variable
    date = None
    date_check = None
    from_code = None
    to_code = None
    from_amount = None
    to_amount = None

    # static method to create entries
    @staticmethod
    def create_entry(location):
        # stringvar for code Entry
        GUI.from_code = StringVar(location)
        GUI.to_code  = StringVar(location)
        GUI.from_code.trace("w", lambda name, index, mode: callback(GUI.from_code))
        GUI.to_code.trace("w", lambda name, index, mode: callback(GUI.to_code))

        # stringvar for amount Entry, the value will then convert into a float data type to be used in the api
        GUI.from_amount = StringVar(location, value="1.0")
        GUI.from_amount.trace("w", lambda name, index, mode: callback(GUI.from_amount, GUI.to_amount, 7, left_amount))
        GUI.to_amount = StringVar(location)

        # currency code Input
        left_code = Entry(location,width=8, font=("Times 30"), bd=4, textvariable=GUI.from_code)
        left_code.place(x=prct(7.2, width), y=prct(20, height))
        right_code = Entry(location,width=8, font=("Times 30"), bd=4, textvariable=GUI.to_code)
        right_code.place(x=prct(43.2, width), y=prct(20, height))

        # amount Input
        left_amount = Entry(location, width=8, font=("Times 30"), textvariable=GUI.from_amount)
        left_amount.bind("." , lambda e: "break")
        left_amount.place(x=prct(7.2, width), y=prct(40, height))
        right_amount = Entry(location, width=8, font=("Times 30"), textvariable=GUI.to_amount)
        # make the right amount read only
        right_amount.configure(state='disabled')
        right_amount.place(x=prct(43.2, width), y=prct(40, height))

        # buttons
        swap_btn = Button(location, width=5, text="<-\n->", command=lambda:btn_commands.swap(GUI))
        swap_btn.place(x=prct(32, width), y=prct(22, height))

    # static method to create conver button
    @staticmethod
    def create_convert_button(location, queue):
        convert_btn = Button(location, text="Convert", width=8, font=("Verdana bold", 16),
                             command=lambda: Thread(target=btn_commands.start_convert , daemon=True,
                                                    args=(GUI.from_code.get(), GUI.to_code.get(), GUI.from_amount,
                                                          GUI.to_amount, GUI.date_check.get() ,GUI.date.get(), queue)).start())
        convert_btn.place(x=prct(28, width), y=50)

    # static method to create date settings
    @staticmethod
    def create_date_settings(location):
        # date check intvar
        GUI.date_check = IntVar()

        # Date checkmark
        date_checkmark = Checkbutton(location, text="Date check", variable=GUI.date_check,
                                     bg="#90ee90", font=("Times 15"))
        date_checkmark.deselect()  # to turn off the button first when it first runs
        date_checkmark.place(x=prct(6, width),
                             y=prct(55, height))

        # settings date to the current date when the GUI start
        GUI.date = StringVar(location, value=date.today())
        # date text
        date_txt = Label(location, textvariable=GUI.date, font=("Verdana bold", 18))
        date_txt.place(x=prct(4, width), y=prct(68, height))

        setdate_btn = Button(location, text="Set Date", font=("Times 12"),
                             command=lambda: btn_commands.set(setdate_btn,GUI.date, date_txt))
        setdate_btn.place(x=prct(10, width), y=prct(78, height))

    # method to create history button and settings
    @staticmethod
    def create_history_btn(location, queue):
        history_btn = Button(location, text="History", width=8, font=("Times 14"),
                             command=lambda: btn_commands.history(history_btn, GUI.from_code,
                                                                  GUI.to_code, queue))
        history_btn.place(x=prct(8, width), y=prct(20, height))

# function for stringvar trace method
def callback(var, rightvar=None, length=None, entry=None ):
    # this is used for code variables
    if length is None:
        limit = var.get()[0:3].upper()
        var.set(limit)
    else: # this is used for amount variable
        rightvar.set("")
        if len(var.get()) > length:
            limit = var.get()[0:length]
            var.set(limit)
        elif var.get() == "" or var.get() == ".":
            var.set(1.0)
        else:
            limit = " ".join(var.get()).split(" ")
            new_limit = list(filter(lambda x: x.isdigit() or x == ".", limit ))
            if new_limit.count(".") != 1:
                entry.unbind(".")
            else:
                entry.bind("." , lambda e: "break")
            var.set("".join(new_limit))

# function for main GUI protocol
def main_closing(main_GUI, his_list):
    with open("history.txt", "w") as file:
        for code in his_list.queue:
            file.write(code)
            file.write("\n")
    main_GUI.destroy()

