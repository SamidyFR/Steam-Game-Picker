import os
import random
import time

gamechoice = input("would you like to gamble the game you want to play today?\n")

if gamechoice == "yes":
    print("your game is:")
    print(random.choice(os.listdir(r"C:\Program Files (x86)\Steam\steamapps\common")))
    print("now, open the game you.. whatever. cant say it.")
    time.sleep(5)
elif gamechoice == "no":
    print("ok then, happy playing!")
    time.sleep(1)
else:
    print("invalid input")
    time.sleep(1)
    quit()
