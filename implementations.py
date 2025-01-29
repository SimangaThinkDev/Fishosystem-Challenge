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
    # time.sleep(3)
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
                # time.sleep(1)
                print("The fish fell into the hands of the shark")
                # time.sleep(2)
                switch_for_evasion = [0,1]
                if random.choices(switch_for_evasion, [4,1])[0] == 1:
                    print("The fish has evaded the attack")
                    pass
                fishosys[x-movesteps][y] = "#"
            else:
                fishosys[x-movesteps][y] = ">"
        if move == "East":
            fishosys[x][y] = " "
            if fishosys[x][y+movesteps] == "#":
                # time.sleep(1)
                print("The fish fell into the hands of the shark")
                # time.sleep(2)
                switch_for_evasion = [0,1]
                if random.choices(switch_for_evasion, [4,1])[0] == 1:
                    print("The fish has evaded the attack")
                    pass
                fishosys[x][y+movesteps] = "#"
            else:
                fishosys[x][y+movesteps] = ">"
        if move == "South":
            fishosys[x][y] = " "
            if fishosys[x+movesteps][y] == "#":
                # time.sleep(1)
                print("The fish fell into the hands of the shark")
                # time.sleep(2)
                switch_for_evasion = [0,1]
                if random.choices(switch_for_evasion, [4,1])[0] == 1:
                    print("The fish has evaded the shark")
                    pass
                fishosys[x+movesteps][y] = "#"
            else:
                fishosys[x+movesteps][y] = ">"
        if move == "West":
            fishosys[x][y] = " "
            if fishosys[x][y-movesteps] == "#":
                # time.sleep(1)         
                print("The fish fell into the hands of the shark")
                # time.sleep(2)
                switch_for_evasion = [0,1]
                if random.choices(switch_for_evasion, [4,1])[0] == 1:
                    print("The fish has evaded the attack")
                    pass
                fishosys[x][y-movesteps] = "#"
            else:
                fishosys[x][y-movesteps] = ">"
        print(bcolors.OKBLUE + f"The fish will now move {move} and {movesteps} steps" + bcolors.OKBLUE)


    except IndexError:
        choice = random.choices([">", " "], [1,2])
        if choice[0] == " ":
            print("The fish has hit the boundaries")
        else:
            spawn(">")

def spawn(species):
    idx_1 = random.randint(0, 19)
    idx_2 = random.randint(0, 19)
    print(idx_1, idx_2)
    if species == ">":
        if fishosys[idx_1][idx_2] != "#":
            fishosys[idx_1][idx_2] = species
    else:
        fishosys[idx_1][idx_2] = species
def shark_move():
    # time.sleep(3)
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
            if fishosys[x-movesteps][y] == ">":
                # time.sleep(1)
                print("The shark is having a feast")
                switch_for_evasion = [0,1]
                if random.choices(switch_for_evasion, [4,1])[0] == 1:
                    print("The fish has evaded this attack")
                    pass
                fishosys[x-movesteps][y] = "#"
            else:
                fishosys[x-movesteps][y] = "#"
        if move == "East":
            fishosys[x][y] = " "
            if fishosys[x][y+movesteps] == ">":
                # time.sleep(1)
                print("The shark is having a feast")
                switch_for_evasion = [0,1]
                if random.choices(switch_for_evasion, [4,1])[0] == 1:
                    print("The fish has evaded this attack")
                    pass
                fishosys[x][y+movesteps] = "#"
            else:
                fishosys[x][y+movesteps] = "#"
        if move == "South":
            fishosys[x][y] = " "
            if fishosys[x+movesteps][y] == ">":
                # time.sleep(1)
                print("The shark is having a feast")
                switch_for_evasion = [0,1]
                if random.choices(switch_for_evasion, [4,1])[0] == 1:
                    print("The fish has evaded this attack")
                    pass
                fishosys[x+movesteps][y] = "#"
            else:
                fishosys[x+movesteps][y] = "#"
        if move == "West":
            fishosys[x][y] = " "
            if fishosys[x][y-movesteps] == ">":
                # time.sleep(1)
                print("The shark is having a feast")
                switch_for_evasion = [0,1]
                if random.choices(switch_for_evasion, [4,1])[0] == 1:
                    print("The fish has evaded this attack")
                    pass
                fishosys[x][y-movesteps] = "#"
            else:
                fishosys[x][y-movesteps] = "#"
        print(bcolors.OKBLUE + f"The shark will now move {move} and {movesteps} steps" + bcolors.OKBLUE)


    except IndexError:
        choice = random.choices(["#", " "], [1,2])
        if choice[0] == " ":
            print("The shark has hit the boundaries")
        else:
            spawn("#")

def  state():
    fishlen = sharklen = 0
    for row in fishosys:
        for item in row:
            if item == ">":
                fishlen += 1
            elif item == "#":
                sharklen += 1

    if fishlen == 0:
        print("All The fishes have been eaten")
        time.sleep(4)
        clear()
        return False
    elif sharklen == 0 :
        clear()
        print("All The Sharks have perished")
        time.sleep(4)
        clear()
        return False
    else:
        return True

def evade():
    pass

while state():
    fishes = 0
    [fishes := fishes + 1 for row in fishosys for item in row if item == ">"]
    sharks = 0
    [sharks := sharks + 1 for row in fishosys for item in row if item == "#"]
    # spawn(">")
    # time.sleep(2)
    fish_move()
    print(f"We currently have {fishes} fishes and {sharks} sharks")
    shark_move()
    print(f"We currently have {fishes} fishes and {sharks} sharks")
