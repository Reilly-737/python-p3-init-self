#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed
fido = Dog("Fido")
fido.breed
        



#Define a Dog class in lib/dog.py. In the class,
#define an __init__ method that accepts an argument for the dog's name. 
#That argument should be stored within a self.name attribute.