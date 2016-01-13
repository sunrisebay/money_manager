import Tkinter as tk 
from Tkinter import Button as btn
from Tkinter import Label as lbl
from Tkinter import Frame as frm
from Tkinter import StringVar
from Tkinter import (LEFT,RIGHT,CENTER,TOP,BOTTOM,RAISED)
from handlers import pg_handlers
from .templates import check_account as ca

ROOT = None

def set_root():
	global ROOT
	ROOT = tk.Tk()

class MainLayout(object):
	frame_left = None
	frame_right = None


	def __init__(self):
		set_root()
		self.initilize()


	def add_frame(self):
		print ROOT
		return frm(ROOT)

	def add_button(self, base, **kwargs):
		return btn(base,**kwargs)

	def initilize(self):
		self.initialize_frames()
		self.initialize_buttons()

	def initialize_frames(self):
		self.frame_left = self.add_frame()
		self.frame_left.pack(side=LEFT)
		self.frame_right = self.add_frame()
		self.frame_right.pack(side=RIGHT)

	def initialize_buttons(self):
		deposit_money = self.add_button(self.frame_left, width=20, 
						compound=LEFT, text="deposit money")
		withdraw_money = self.add_button(self.frame_left, width=20, 
						compound=LEFT, text="withdraw money")
		transfer_money = self.add_button(self.frame_left, width=20,
						compound=LEFT, text="transfer money")
		exit = self.add_button(self.frame_left, width=20, compound=LEFT, 
						text="exit", command=ROOT.destroy)
		check_account = self.add_button(self.frame_left, width=20, compound=LEFT, 
						text="check account", 
						command=self.check_account_runner)
		deposit_money.pack()
		withdraw_money.pack()
		transfer_money.pack()
		check_account.pack()
		exit.pack()
		var = StringVar()
		text_area = lbl(self.frame_right, height=100, width=60, 
						compound=TOP, textvariable=var, relief=RAISED)
		var.set("how are you")
		text_area.pack()

	def runner(self):
		ROOT.mainloop()

	def check_account_runner(self):
		ca.check_accounts(tk.Toplevel(ROOT))



#text


#start the app


