import Tkinter as tk 
from ui.base import BaseLayout
from Tkinter import (LEFT,RIGHT,CENTER,TOP,BOTTOM,RAISED)

class TransferMoney(BaseLayout):

    def __init__(self):
        pass
        
    def transfer(self, from_account_name, to_account_name, amount):
        print (self.get_text(from_account_name)
            + self.get_text(to_account_name)
            + self.get_text(amount))

    def transfer_money_layout(self, base):
        from_frame = self.add_frame(base)
        to_frame = self.add_frame(base)
        amount_frame = self.add_frame(base)
        bottom_frame = self.add_frame(base)

        from_account_name = self.add_entry(from_frame, width=30)
        from_account_name_lbl = self.add_label(from_frame, width=20, 
                    text="From:")

        to_account_name = self.add_entry(to_frame, width=30)
        to_account_name_lbl = self.add_label(to_frame, width=20, 
                    text="To:")

        amount = self.add_entry(amount_frame, width=30)
        amount_lbl = self.add_label(amount_frame, width=20,
                    text="Amount: ")

        cancel = self.add_button(bottom_frame, width=20, 
                    text="Cancel", command=base.destroy)
        submit = self.add_button(bottom_frame, width=20, 
                    text="Submit", 
                    command= lambda: self.transfer(from_account_name, to_account_name, amount))

        from_frame.pack(side=TOP)
        to_frame.pack()
        amount_frame.pack()
        bottom_frame.pack(side=BOTTOM)

        from_account_name_lbl.pack(padx=20, side=LEFT, pady=10)
        from_account_name.pack(padx=20, pady=10, side=LEFT)

        to_account_name_lbl.pack(padx=20, side=LEFT, pady=10)
        to_account_name.pack(padx=20, pady=10, side=LEFT)

        amount_lbl.pack(padx=20, pady=10, side=LEFT)
        amount.pack(padx=20, pady=10, side=LEFT)

        submit.pack(padx=20, pady=10, side=LEFT)
        cancel.pack(padx=20, pady=10, side=LEFT)

