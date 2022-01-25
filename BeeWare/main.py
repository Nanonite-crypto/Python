import os
import sys
from ButterEssentials.butter_essentials.VChange import data
import keyboard
import time


def LoginAs():
    try:
        login = input("Login.. ")

        if login != "delete" and login:
            if os.path.exists(f"{login}.json"):
                credentials = data.load_value(name=login, loadVar=login)
                if credentials != "":
                    pwd = input("Password.. ")

            if os.path.exists(f"{login}.json"):
                credentials = data.load_value(name=login, loadVar=login)
                if credentials == "":
                    # If there is no actual password assigned give them access to the Account.
                    print("Access Granted.")
                    return login
                elif pwd == credentials:
                    # If the password is correct give them access to the Account.
                    print("Access Granted.")
                    return login
                else:
                    # If the password is incorrect don't give them permission to the Account.
                    print("Access Denied.")
                    sys.exit()
            else:
                try:
                    pwd = input("Password.. ")
                    data.save_value(name=login, value=pwd, savedAs=login)
                    print("Account Made.")
                    return login
                except OSError:
                    print('You cannot use ?, ", | or /  in your name.')
        else:
            delLogin = input("Delete Login.. ")

            if os.path.exists(f"{delLogin}.json"):
                credentials = data.load_value(name=delLogin, loadVar=delLogin)
                if credentials != "":
                    pwd = input("Password.. ")

            if os.path.exists(f"{delLogin}.json"):
                credentials = data.load_value(name=delLogin, loadVar=delLogin)
                if credentials == "":
                    # If there is no actual password assigned give them access to delete the Account.
                    os.remove(f"{delLogin}.json")
                    print("Account Deleted.")
                    sys.exit()
                elif pwd == credentials:
                    # If the password is correct give them access to delete the Account.
                    os.remove(f"{delLogin}.json")
                    print("Account Deleted.")
                    sys.exit()
                else:
                    # If the password is incorrect don't give them permission to delete the Account.
                    print("Access Denied.")
                    sys.exit()
            else:
                print("Account Not Found.")
    except KeyboardInterrupt:
        pass


loginAs = LoginAs()

if not loginAs:
    pass
else:
    print("Welcome {}".format(loginAs))
    print("\n"*3)

    try:
        while True:
            cmd = input("{0} >> ".format(loginAs))

            if cmd.lower() in ["q", "quit", "exit", "end"]:
                break

            if keyboard.read_key() == 'esc':
                break
    except KeyboardInterrupt:
        pass
