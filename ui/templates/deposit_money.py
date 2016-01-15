import Tkinter as tk 
from ui.base import BaseLayout
from Tkinter import (LEFT,RIGHT,CENTER,TOP,BOTTOM,RAISED)

class DepositMoney(BaseLayout):

    def __init__(self):
        pass
        
    def deposit(self, account_name, amount):
        print self.get_text(account_name) + self.get_text(amount)


    def get_text(self, e):
        if e and e.get():
            return e.get()
        else:
            return "*"

    def deposit_money_layout(self, base):
        upper_frame = self.add_frame(base)
        middle_frame = self.add_frame(base)
        bottom_frame = self.add_frame(base)

        account_name = self.add_entry(upper_frame, width=30)
        account_name_lbl = self.add_label(upper_frame, width=20, 
                    text="Account Name:")

        amount = self.add_entry(middle_frame, width=30)
        amount_lbl = self.add_label(middle_frame, width=20,
                    text="Amount: ")

        cancel = self.add_button(bottom_frame, width=20, 
                    text="Cancel", command=base.destroy)
        submit = self.add_button(bottom_frame, width=20, 
                    text="Submit", command= lambda: self.deposit(account_name, amount))

        upper_frame.pack(side=TOP)
        middle_frame.pack()
        bottom_frame.pack(side=BOTTOM)

        account_name_lbl.pack(padx=20, side=LEFT, pady=10)
        account_name.pack(padx=20, pady=10, side=LEFT)

        amount_lbl.pack(padx=20, pady=10, side=LEFT)
        amount.pack(padx=20, pady=10, side=LEFT)

        submit.pack(padx=20, pady=10, side=LEFT)
        cancel.pack(padx=20, pady=10, side=LEFT)

