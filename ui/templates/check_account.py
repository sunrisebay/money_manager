import Tkinter as tk 
from Tkinter import Button as btn
from Tkinter import (LEFT,RIGHT,CENTER,TOP,BOTTOM,RAISED)
from Tkinter import Entry as entry

e = None 

def get_text():
	if e:
		print e.get()
	else:
		print e

def check_accounts(check_account):
	deposit_money = btn(check_account, width=20, compound=LEFT, text="deposit money")
	withdraw_money = btn(check_account, width=20, compound=LEFT, text="withdraw money")
	transfer_money = btn(check_account, width=20,compound=LEFT, text="transfer money")
	check_accountt = btn(check_account, width=20, compound=LEFT, 
				text="check account", command=get_text)
	global e
	e = entry(check_account)
	deposit_money.pack()
	withdraw_money.pack()
	transfer_money.pack()
	check_accountt.pack()
	e.pack()
