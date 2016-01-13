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
		account_name = self.add_entry(check_account)
		account_name_lbl = self.add_label(check_account, width=20, compound=LEFT, text="Account Name:")
		cancel = self.add_button(check_account, width=20, compound=LEFT, 
					text="Cancel", command=check_account.destroy)
		submit = self.add_button(check_account, width=20, compound=LEFT, 
					text="Submit", command= lambda: self.get_text(account_name))

		account_name_lbl.pack()
		account_name.pack()
		submit.pack()
		cancel.pack()

