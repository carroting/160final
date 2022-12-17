import pygame
from tkinter import *

import consts

c = consts

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widget()
        self.pack()

    def create_widget(self):
        self.bttn1 = Button(self, text = c.A, font = ('Georgia',10), command = self.update1)
        self.bttn1.grid()
        if c.B != '':
            self.bttn2 = Button(self, text = c.B, font = ('Georgia',10), command = self.update2)
            self.bttn2.grid()
        if c.C != '':
            self.bttn3 = Button(self, text = c.C, font = ('Georgia',10), command = self.update3)
            self.bttn3.grid()

    def update1(self):
        c.choice = 1
        self.quit()
    def update2(self):
        c.choice = 2
        self.quit()
    def update3(self):
        c.choice = 3
        self.quit()

def options(title = '',option1 = '', option2 = '', option3 = ''):
    c.choice = 0
    win = Tk()
    win.title(title)
    win.geometry("300x300")
    c.A = option1
    c.B = option2
    c.C = option3
    if c.choice == 0:
        Application(win)
    win.mainloop()
    if c.choice != 0:
        win.destroy()
def short(name):
    options(name, 'Talk','Gift','Leave')
