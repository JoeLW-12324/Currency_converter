"""This module is used for the history GUI to create the buttons"""
# import modules
from tkinter import Button

# array class to hold all of the buttons in the history GUI
class array_btns:
    def __init__(self, master, arr, left_var, right_var, btn):
        self.btns_list = list()
        for element in arr:
            button = his_btn(master, element, left_var, right_var, btn)
            self.btns_list.append(button)

# button class to hold a pair of code
class his_btn():
    def __init__(self, master, element, left_var, right_var, btn):
        self.button = Button(master, text=f"{element}", width=20,
                             command=lambda:his_btn.select(element, master, left_var, right_var, btn))
        self.button.pack()

    # static method for the button select command
    @staticmethod
    def select(element, master, left_var, right_var, btn):
        left_code, right_code = element.split("-")
        left_var.set(left_code)
        right_var.set(right_code)
        return on_closing(btn, master)

# on closing function for date set and history button protocol
def on_closing(btn, GUI):
    try:
        btn["state"] = "normal"
        GUI.destroy()
    except Exception as e: # if the main GUI is closed, this is used to allow the date gui or history gui to close too
        GUI.destroy()


