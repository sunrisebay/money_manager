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

	def check_accounts(self, check_account):
		upper_frame = self.add_frame(check_account)
		bottom_frame = self.add_frame(check_account)
		account_name = self.add_entry(upper_frame)
		account_name_lbl = self.add_label(upper_frame, width=20, compound=LEFT, text="Account Name:")
		cancel = self.add_button(bottom_frame, width=20, compound=RIGHT, 
					text="Cancel", command=check_account.destroy)
		submit = self.add_button(bottom_frame, width=20, compound=LEFT, 
					text="Submit", command= lambda: self.get_text(account_name))

		upper_frame.pack(side=TOP)
		bottom_frame.pack(side=BOTTOM)
		account_name_lbl.pack()
		account_name.pack()
		submit.pack()
		cancel.pack()

