#!/usr/bin/env python3

#Class : Dog Class
#11/5/2023

"""
    Dog Class
    Data Fields: name, breed
    Methods: getters, setters for each fields, maybe a __str__ method to display

"""

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    #constructor
    def __init__(self,name='Fido', breed='Mastiff'):
        self.name = name
        self.breed = breed
    
    def get_name(self):
        return self._name
    
   
    def set_name(self,value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")
    
    name = property(get_name, set_name)
    
    
    def get_breed(self):
        return self._breed

   
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed,set_breed)