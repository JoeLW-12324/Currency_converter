"""This module contains staticmethod from the btn_commands class that are used as commands for the buttons in the GUI"""
# import modules
from Converter_api import api_convert
from tkinter import *
from tkinter import messagebox
from tkcalendar import *
from datetime import date
from history_buttons import array_btns, on_closing

# class method that are used as commands by the buttons in the GUI
class btn_commands:
    today_date = date.today()

    # static method for the swap button command
    @staticmethod
    def swap(cls):
        current_from_code, current_to_code = cls.from_code.get(), cls.to_code.get()
        if cls.from_amount.get() != "" and cls.to_amount.get() != "":
            current_from_amount, current_to_amount = cls.from_amount.get(), cls.to_amount.get()
            cls.from_amount.set(current_to_amount)
            cls.to_amount.set(current_from_amount)
        cls.from_code.set(current_to_code)
        cls.to_code.set(current_from_code)

    # static method for the convert button command
    @staticmethod
    def start_convert(lft_code, rgt_code, lft_amt, rgt_amt, date_check, date, queue):
        if lft_code == "" or rgt_code == "":
            messagebox.showerror(title="Error! Boxes are not fill",
                                 message="Please fill in the two top boxes with currency codes")
        elif float(lft_amt.get()) == 0:
            messagebox.showerror(title="Error! Amount input is zero",
                                 message="Please fill in the left bottom box with a value that is not 0")
        else:
            # setting date to false if date check value is 0 else it is put as its default string
            date = date if date_check else False
            converted_result = api_convert(lft_code, rgt_code, lft_amt.get(), date)
            if converted_result is None:
                messagebox.showerror(title="Error! User inputs are not currency code",
                                     message="Please fill in the two top boxes with currency codes")
            else:
                rgt_amt.set(converted_result)
            queue.modify(f"{lft_code}-{rgt_code}")

    # static method for the history button command
    @staticmethod
    def history(btn, lft_var, rgt_var, queue):
        btn["state"] = "disabled" # disabling the button so that it doesn't make the user open more than one
        history_GUI = Tk()
        history_GUI.resizable(0, 0)
        history_GUI.geometry("160x280")
        history_GUI.protocol("WM_DELETE_WINDOW", lambda: on_closing(btn, history_GUI))
        buttons_list = array_btns(history_GUI, queue.queue, lft_var, rgt_var, btn)

    # static method for the set button command for date settings
    @staticmethod
    def set(btn, set_date, label):
        btn["state"] = "disabled" # disabling the button so that it doesn't make the user open more than one
        global date_GUI
        date_GUI = Tk()
        date_GUI.title("Date settings")
        date_GUI.resizable(0, 0)
        date_GUI.geometry("250x250")
        date_GUI.protocol("WM_DELETE_WINDOW", lambda: on_closing(btn, date_GUI))

        # stringvar for calendar
        date_var = StringVar(date_GUI, value=f"{29}-{7}-{2022}")
        # calendar class from tkcalendar
        cal = Calendar(date_GUI, selectmode="day", textvariable=date_var, date_pattern="y-mm-dd")
        date_var.set(set_date.get()) # change the variable to the default isoformat that is needed for the api
        cal.place(x=0, y=0)
        date_label = Label(date_GUI, textvariable=date_var, font="Times 15").place(x=80, y=190)
        set_btn = Button(date_GUI, text="Set",
                         command=lambda: btn_commands.confirm_date(date_var.get(),set_date, on_closing(btn, date_GUI)))
        set_btn.place(x=125, y=225)


    # static method for setting date button in date GUI
    @staticmethod
    def confirm_date(new_date, current_date, function):
        if date.fromisoformat(new_date) > btn_commands.today_date:
            messagebox.showerror(title="Error! Date is a future date!",
                                 message="Please select a date that is not set in the future of the today's date")
        else:
            current_date.set(new_date)
            return function
            # close gui after setting by returning the on closing function

