import Tkinter as tk 
from base import BaseLayout
from Tkinter import StringVar
from Tkinter import (LEFT,RIGHT,CENTER,TOP,BOTTOM,RAISED)
from handlers import pg_handlers
from actions import MainLayoutActions

class MainLayout(BaseLayout):
    frame_left = None
    frame_right = None
    main_actions = None

    def __init__(self):
        super(MainLayout,self).__init__()
        self.main_actions = MainLayoutActions()
        self.initilize()

    def initilize(self):
        self.initialize_frames()
        self.initialize_buttons()

    def initialize_frames(self):
        self.frame_left = self.add_frame(self.ROOT)
        self.frame_left.pack(side=LEFT)
        self.frame_right = self.add_frame(self.ROOT)
        self.frame_right.pack(side=RIGHT)

    def initialize_buttons(self):
        deposit_money = self.add_button(self.frame_left, width=20, 
                        compound=LEFT, text="deposit money")
        withdraw_money = self.add_button(self.frame_left, width=20, 
                        compound=LEFT, text="withdraw money")
        transfer_money = self.add_button(self.frame_left, width=20,
                        compound=LEFT, text="transfer money")
        exit = self.add_button(self.frame_left, width=20, compound=LEFT, 
                        text="exit", command=self.ROOT.destroy)
        check_account = self.add_button(self.frame_left, width=20, 
                        compound=LEFT, text="check account", 
                        command= lambda: self.main_actions.check_account_runner(self.ROOT))
        deposit_money.pack()
        withdraw_money.pack()
        transfer_money.pack()
        check_account.pack()
        exit.pack()
        var = StringVar()
        text_area = self.add_label(self.frame_right, height=100, width=60, 
                        compound=TOP, textvariable=var, relief=RAISED)
        var.set("how are you")
        text_area.pack()

    def runner(self):
        super(MainLayout,self).runner()

# class MainLayoutActions(object):
#     def check_account_runner(self, base):
#         ca.check_accounts(tk.Toplevel(base))

