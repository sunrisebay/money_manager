import Tkinter as tk 
from Tkinter import Button as btn
from Tkinter import Label as lbl
from Tkinter import Frame as frm
from Tkinter import (LEFT,RIGHT,CENTER,TOP,BOTTOM,RAISED)
from Tkinter import Entry as entry

class BaseLayout(object):

    ROOT = None

    def __init__(self):
        self.set_root()

    def set_root(self):
        if not self.ROOT:
            self.ROOT = tk.Tk()

    def add_frame(self, base, **kwargs):
        return frm(base, **kwargs)

    def add_button(self, base, **kwargs):
        return btn(base,**kwargs)

    def add_label(self, base, **kwargs):
        return lbl(base, **kwargs)

    def add_entry(self, base, **kwargs):
        return entry(base, **kwargs)

    def runner(self):
        self.ROOT.mainloop()

    def get_text(self, e):
        if e and e.get():
            return e.get()
        else:
            return "*"