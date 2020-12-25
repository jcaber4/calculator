from tkinter import *

class NumberButton(Button):
    '''Hold numbers'''
    def __init__(self, gui, screen, num):
        super().__init__(gui, text=f' {num} ', fg='white', bg='grey',
                     command=lambda: screen.push(num), height=1, width=7)

class OperationButton(Button):
    '''Hold operations'''
    def __init__(self, gui, screen, operator):
        super().__init__(gui, text=f' {operator} ', fg='white', bg='grey',
                     command=lambda: screen.push(operator), height=1, width=7)

class BackspaceButton(Button):
    '''Backspace button'''
    def __init__(self, gui, screen):
        super().__init__(gui, text=f' Del ', fg='white', bg='grey',
                     command=lambda: screen.delete(), height=1, width=7)

class ClearButton(Button):
    '''Clear button'''
    def __init__(self, gui, screen):
        super().__init__(gui, text=f' Clr ', fg='white', bg='grey',
                     command=lambda: screen.clear(), height=1, width=7)

class EnterButton(Button):
    '''Eval Button'''
    def __init__(self, gui, screen):
        super().__init__(gui, text=f' = ', fg='white', bg='grey',
                     command=lambda: screen.evaluate(), height=1, width=7)