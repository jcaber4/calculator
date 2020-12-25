from tkinter import *

class Screen(Entry):
    '''Holds Screen Contents'''
    def __init__(self, master=None, cnf={}, **kw):
        Widget.__init__(self, master, 'entry', cnf, kw)
        self.visable=''
        self.textvariable=kw['textvariable']

    def push(self, to_push):
        self.visable = self.visable + str(to_push)
        self.textvariable.set(self.visable)

    def delete(self):
        newstr = self.visable[:-1]
        self.visable = newstr
        self.textvariable.set(newstr)

    def clear(self):
        self.visable = ''
        self.textvariable.set('')

    def evaluate(self):
        try:
            result = str(eval(self.visable))
            self.textvariable.set(result)
            self.visable = ''
        except:
            self.textvariable.set(" error ")
            self.visable = ''
