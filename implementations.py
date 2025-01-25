# This code will show each concept behind the implementation of the main program
from fisho import *

"""
Try catch to move species
    -Run this file for a quick demo

"""

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def fish_move():
    time.sleep(3)
    clear()
    try:
        y, x = fish_noticer()
        print(x, y)
        # Create a list of randomizable directions, this will act as a guide for our fishes...

        directions = ["North", "East", "South", "West"]
        spaces_to_move = [1, 2, 3]
        
        [print(row) for row in fishosys]
        move = random.choice(directions)
        movesteps = random.choice(spaces_to_move)
        if move == "North":
            fishosys[x][y] = " "
            if fishosys[x-movesteps][y] == "#":
                print("The fish fell into the hands of the shark")
            else:
                fishosys[x-movesteps][y] = ">"
        if move == "East":
            fishosys[x][y] = " "
            if fishosys[x][y+movesteps] == "#":
                print("The fish fell into the hands of the shark")
            else:
                fishosys[x][y+movesteps] = ">"
        if move == "South":
            fishosys[x][y] = " "
            if fishosys[x+movesteps][y] == "#":
                print("The fish fell into the hands of the shark")
            else:
                fishosys[x+movesteps][y] = ">"
        if move == "West":
            fishosys[x][y] = " "
            if fishosys[x][y-movesteps] == "#":
                print("The fish fell into the hands of the shark")
            else:
                fishosys[x][y-movesteps] = ">"
        print(bcolors.OKBLUE + f"The fish will now move {move} and {movesteps} steps" + bcolors.OKBLUE)


    except IndexError:
        print("The fish has hit the boundaries")

def shark_move():
    time.sleep(3)
    clear()
    try:
        y, x = shark_noticer()
        print(x, y)
        # Create a list of randomizable directions, this will act as a guide for our fishes...

        directions = ["North", "East", "South", "West"]
        spaces_to_move = [1, 2, 3]
        
        [print(row) for row in fishosys]
        move = random.choice(directions)
        movesteps = random.choice(spaces_to_move)
        if move == "North":
            fishosys[x][y] = " "
            if fishosys[x-movesteps][y] == "#":
                print("The shark is having a feast")
                fishosys[x-movesteps][y] = "#"
        if move == "East":
            fishosys[x][y] = " "
            if fishosys[x][y+movesteps] == "#":
                print("The shark is having a feast")
                fishosys[x][y+movesteps] = "#"
        if move == "South":
            fishosys[x][y] = " "
            if fishosys[x+movesteps][y] == "#":
                print("The shark is having a feast")
                fishosys[x+movesteps][y] = "#"
        if move == "West":
            fishosys[x][y] = " "
            if fishosys[x][y-movesteps] == "#":
                print("The shark is having a feast")
                fishosys[x][y-movesteps] = "#"
        print(bcolors.OKBLUE + f"The shark will now move {move} and {movesteps} steps" + bcolors.OKBLUE)


    except IndexError:
        print("The shark has hit the boundaries")



while True:
    fishes = 0
    [fishes := fishes + 1 for row in fishosys for item in row if item == ">"]
    sharks = 0
    [sharks := sharks + 1 for row in fishosys for item in row if item == "#"]
    fish_move()
    print(f"We currently have {fishes} fishes and {sharks} sharks")
    shark_move()
    print(f"We currently have {fishes} fishes and {sharks} sharks")