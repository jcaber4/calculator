from tkinter import *
from screen import Screen
from buttons import *
from calc import Calc

if __name__ == "__main__":
    window = Tk()
    window.configure(background="lightblue")
    window.resizable(False, False)
    window.title("Calculator")
    window.geometry("305x125")

    screenvar = StringVar()
    screen_field = Screen(window, textvariable=screenvar)
    screen_field.grid(row=0)

    calculator = Calc(screen_field, master=window)
    calculator.grid(row=1)

    calculator.mainloop()
