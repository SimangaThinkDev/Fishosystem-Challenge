# This code will show each concept behind the implementation of the main program
from fisho import *

"""
Try catch to move species
    -Run this file for a quick demo

"""

while True:
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
            fishosys[x-movesteps][y] = ">"
        if move == "East":
            fishosys[x][y] = " "
            fishosys[x][y+movesteps] = ">"
        if move == "South":
            fishosys[x][y] = " "
            fishosys[x+movesteps][y] = ">"
        if move == "West":
            fishosys[x][y] = " "
            fishosys[x][y-movesteps] = ">" 
        print(f"The fish will now move {move} and {movesteps} steps")


    except IndexError:
        print("The fish has hit the boundaries")

