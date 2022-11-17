import pyautogui
import time
from configparser import ConfigParser

savedata = int(input("""
Type 1 If you want to create a save data
Type 2 If you want to load a save data
> 
"""))

if savedata == 1:
    rolls = int(input("How many rolls do you want to roll for (give answer in numbers only): "))
    command = input("What command do you want to type? ")
    secs = int(input("How many seconds do you want before the program runs, so you have enough time to go to discord: "))
    print(f"You Have {secs} Secs Before The Program Runs Go To Discord Immediately!")

    config_object = ConfigParser()
    config_object["USERINFO"] = {
        "rolls": rolls,
        "command": command,
        "secs": secs
    }

    with open('AutoMudaeRollerconfig.ini', 'w') as conf:
        config_object.write(conf)

        time.sleep(secs)
        i = 1

        while i <= rolls:
            line = command
            pyautogui.typewrite(line)
            pyautogui.press("enter")
            time.sleep(1)
            i = i + 1

if savedata == 2:
    config_object = ConfigParser()
    config_object.read("AutoMudaeRollerconfig.ini")
    userinfo = config_object["USERINFO"]
    rolles = int(userinfo["rolls"])
    commannd = userinfo["command"]
    seccs = int(userinfo["secs"])

    print(f"You Have {seccs} Secs Before The Program Runs Go To Discord Immediately!")

    time.sleep(seccs)
    i = 1

    while i <= rolles:
        line = commannd
        pyautogui.typewrite(line)
        pyautogui.press("enter")
        time.sleep(1)
        i = i + 1
