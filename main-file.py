import time
import json
import signup
import login
from IPython.display import clear_output
records=dict()
choice=int((input("press\n (1) for login\n (2) sign up\n")))
while choice<3:#choice<3
    if choice==1:#login
        login.login()
        break
    elif choice==2:#sign up
        signup.create_acc()
        choice=int((input("press\n (1) for login\n (2) sign up\n")))
else:
    pass
