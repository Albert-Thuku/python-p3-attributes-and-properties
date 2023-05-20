#!/usr/bin/env python3

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
    def __init__(self, name='Insert name', breed='Insert breed'):
        self._name = name
        self._breed = breed

    def set_name(self, name):
        if  name == '' or type(name) != str or 1 < len(name) or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = name
            print('Setting dog name')

    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
            print('Setting dog breed')
        else:
            print('Breed must be in the list of approved breeds.')

    def get_name(self):
        return self._name

    def get_breed(self):
        return self._breed

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)

