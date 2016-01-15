import Tkinter as tk 
from ui.base import BaseLayout
from Tkinter import (LEFT,RIGHT,CENTER,TOP,BOTTOM,RAISED)

class CheckAccounts(BaseLayout):

	def __init__(self):
		pass
		
	def get_text(self, e):
		if e:
			print e.get()
		else:
			print e

	def check_accounts(self, base):
		upper_frame = self.add_frame(base)
		bottom_frame = self.add_frame(base)
		account_name = self.add_entry(upper_frame, width=30)
		account_name_lbl = self.add_label(upper_frame, width=20, text="Account Name:")
		cancel = self.add_button(bottom_frame, width=20, 
					text="Cancel", command=base.destroy)
		submit = self.add_button(bottom_frame, width=20, 
					text="Submit", command= lambda: self.get_text(account_name))

		upper_frame.pack(side=TOP)
		bottom_frame.pack(side=BOTTOM)
		account_name_lbl.pack(side=LEFT, pady=10)
		account_name.pack(padx=20, pady=10, side=LEFT)
		submit.pack(padx=20, pady=10, side=LEFT)
		cancel.pack(padx=20, pady=10, side=LEFT)

