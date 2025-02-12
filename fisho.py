from clear import clear
import random, time

fishosys = [[random.choices([" ", ">", "#"], [30, 2, 0.5])[0] for i in range(20)] for j in range(20)]

def fish_noticer(fishosys = fishosys):

    for y, row in enumerate(fishosys):
        for x, object in enumerate(row):
            if object == ">":
                return x, y


def shark_noticer(fishosys = fishosys):

    for y, row in enumerate(fishosys):
        for x, object in enumerate(row):
            if object == "#":
                return x, y
            
def space(fishosys = fishosys):

    for y, row in enumerate(fishosys):
        for x, object in enumerate(row):
            if object == " ":
                return x, y





if __name__ == "__main__":
    # print(fish_noticer())
    [print(row) for row in fishosys]