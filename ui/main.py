import Tkinter as tk 
from Tkinter import Button as btn
from Tkinter import Label as lbl
from Tkinter import Frame as frm
from Tkinter import StringVar
from Tkinter import (LEFT,RIGHT,CENTER,TOP,BOTTOM,RAISED)
from services.connection import PostgresqlConnection as pgconn
from handlers.base import PostgresqlHandlers as pghandlers

#start the window
root = tk.Tk()

#frame
frame_left = frm(root)
frame_left.pack(side=LEFT)
frame_right = frm(root)
frame_right.pack(side=RIGHT)

#button
deposit_money = btn(frame_left, width=20, compound=LEFT, text="deposit money")
withdraw_money = btn(frame_left, width=20, compound=LEFT, text="withdraw money")
transfer_money = btn(frame_left, width=20,compound=LEFT, text="transfer money")
exit = btn(frame_left, width=20, compound=LEFT, 
			text="exit", command=root.destroy)
check_account = btn(frame_left, width=20, compound=LEFT, text="check account")
deposit_money.pack()
withdraw_money.pack()
transfer_money.pack()
check_account.pack()
exit.pack()

#text
var = StringVar()
text_area = lbl(frame_right, height=100, width=60, 
				compound=TOP, textvariable=var, relief=RAISED)
var.set("how are you")
text_area.pack()

#start the app
def runner():
	_pghandlers = pghandlers()
	_pghandlers.set_cursor()
	_pghandlers.execute_statements("""SELECT * from visa_account""")
	root.mainloop()

