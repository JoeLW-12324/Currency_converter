# Importing modules
from tkinter import *
import converter_GUI
from converter_GUI import GUI
from queue_ds import history_queue

# main function to execute all of the code
def main():
    # queue data structure
    history_list = history_queue()

    #main GUI
    root = Tk()
    root.title("Currency Converter")
    root.resizable(0, 0)
    root.geometry(f"{converter_GUI.width}x{converter_GUI.height}")
    root.iconbitmap("currency.ico")
    root.protocol("WM_DELETE_WINDOW", lambda: converter_GUI.main_closing(root, history_list))

    # context manager to read the history.txt file and put them into a queue
    with open("history.txt", "r") as file:
        for line in file.readlines():
            if "\n" in line:
                history_list.queue.append(line[:-1])
            else:
                history_list.queue.append(line)
        if history_list.queue[-1] == "":
            history_list.queue.pop()

    # creating 3 frames one for date and history, one for convert button and another for setting input
    # top left frame for setting input
    top_frame = Frame(root,
                      bg="#add8e6",
                      width=converter_GUI.prct(72, converter_GUI.width),
                      height=converter_GUI.prct(70, converter_GUI.height))
    top_frame.place(x = 0, y = 0)

    # right frame for date and history
    right_frame = Frame(root,
                        bg="#90ee90",
                        width=converter_GUI.prct(28, converter_GUI.width),
                        height=converter_GUI.height)
    right_frame.place(x = converter_GUI.prct(72, converter_GUI.width) , y = 0)

    # bottom frame for convert button
    bottom_frame = Frame(root,
                         bg="#808080",
                         width=converter_GUI.prct(72, converter_GUI.width),
                         height=converter_GUI.prct(30, converter_GUI.height))
    bottom_frame.place(x=0, y=converter_GUI.prct(70, converter_GUI.height))

    # label text
    insert_code_text = Label(top_frame, text="Insert currency code", font=("Verdana bold", 20), bg="#add8e6").place(
        x=converter_GUI.prct(18, converter_GUI.width), y=0)
    amount_text = Label(top_frame, text="Amount", font=("Verdana bold", 18), bg="#add8e6").place(
        x=converter_GUI.prct(28, converter_GUI.width), y=converter_GUI.prct(42, converter_GUI.height))

    # Entry
    GUI.create_entry(top_frame)
    GUI.create_convert_button(bottom_frame, history_list)

    # history stuff
    GUI.create_history_btn(right_frame, history_list)
    GUI.create_date_settings(right_frame)

    mainloop()


if __name__ == '__main__':
    main()
