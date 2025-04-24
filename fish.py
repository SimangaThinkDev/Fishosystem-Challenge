from abc import ABC, abstractmethod
from random import *
class Fish:

    @abstractmethod
    def personality():
        pass
    
    @abstractmethod
    def physical_appearance():
        pass

class Parent(Fish):

    def __init__(self):
        self.possibleGenders = ['male', 'female']
        self.gender = choice(self.possibleGenders)
    
    def personality():
        possible_personalities = ["confident", "shy", "nosy", "dual-nature"]
        fish_personality = []