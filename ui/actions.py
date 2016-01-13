from .templates import check_accounts as ca
import Tkinter as tk 

class MainLayoutActions(object):
    def check_account_runner(self, base):
        ca.check_accounts(tk.Toplevel(base))