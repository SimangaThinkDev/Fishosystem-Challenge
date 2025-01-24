# Question:
## You are tasked with creating a simple ecosystem simulation in Python using the terminal. The ecosystem is represented as a 20x20 grid, where each cell can contain:

    ">": A fish
    "#": A shark
    " ": An empty space


## Tasks:

1. Enhance the simulation: Imagine that the fishes (">") and sharks ("#") interact in the ecosystem. Ideas can be any of the following.

    - Allow sharks to move towards fish.
"Eat" the fish when they collide with them.
    - Reproduce fish and sharks based on certain conditions (ie. this is entirely up to you).
    - Improve efficiency: The current simulation generates a new ecosystem randomly each time. What improvements could you make to ensure that the state of the ecosystem evolves over time, rather than resetting every second?

2. Implement a clear() function. Ensure that the terminal clears between each iteration to show the user only the current state of the game.

3. Ending the Game: In the ecosystem, there needs to be a condition to determine when the game ends. For instance:
    - Sharks win if all the fish (">") are eaten.
    - Fishes win if all the sharks ("#") are either eaten or starve, or whatever you want it to be!! (i.e., there are no sharks left).


# Due
    - Monday
