#!/usr/bin/env python3

# dog.py

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

    def sit(self):
        print("The dog is sitting.")

    def bark(self):
        print("Woof!")
