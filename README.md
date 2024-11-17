why did i make this this is so easy its like 20 lines of code :(
# What Am I Gonna Play On Steam Today? (WAIGPOST)
What Am I Gonna Play On Steam Today? (shortended to WAIGPOST) is a (VERY simple) Python script that looks into your steam game directory and picks a random game. 

perfect for when you're bored but dont know what to play.

it pretty much just looks in your steam game library, and chooses a random one. thats how simple it is. idek why i made this.

# FAQ's and stuff:

### Q: What if my steam games are in another directory? (aka not in the default directory)

### A: if you never tried to move your steam games, dont worry. they will stay in the default directory. if you have though, its as easy as going to this line:
### print(random.choice(os.listdir(r"C:\Program Files (x86)\Steam\steamapps\common")))
### and changing the directory to wherever your library is.

### Q: what if most of my games are from another source? (eg. gog, epic,)

### A: same as the last question. change the directory to wherever your source of games are (this script is NOT a priority of mine to add more as its simple, generic and already done a million times :P)

### Q: The script gave me a game that i uninstalled. what gives?

### A: steam leaves some files of the game still even after you deleted it, and ofc also keeps the folder. so, not my fault. 
### if your smarter then me at python (which if you know more then a beginner then likely) and for whatever reason wanna fix this, be my guest.


anyways uhh, have fun or whatever :P
and also have a good day.
