from .templates import check_accounts as ca
from .templates import deposit_moneys as dm
from .templates import withdraw_moneys as wm
from .templates import transfer_moneys as tm
import Tkinter as tk 

class MainLayoutActions(object):

    def __init__(self):
        pass

    def check_account_runner(self, base):
        ca.check_accounts(tk.Toplevel(base))

    def deposit_money_runner(self, base):
        dm.deposit_money_layout(tk.Toplevel(base))

    def withdraw_money_runner(self, base):
        wm.withdraw_money_layout(tk.Toplevel(base))

    def transfer_money_runner(self, base):
        tm.transfer_money_layout(tk.Toplevel(base))