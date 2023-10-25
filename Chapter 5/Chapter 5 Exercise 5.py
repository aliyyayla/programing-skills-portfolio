#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 18:19:22 2023

@author: aliyya
"""

"""
Chapter 5 Exercise 5: Pets
Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the

owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about

each pet
"""

dog = {'Animal': 'Golden Retriever', 'Animal Owner': 'Kai'} 
parrot = {'Animal': 'Parrot', 'Animal Owner': 'Ben'}
hedgehog = {'Animal': 'Hedgehog', 'Animal Owner': 'Steve'}
cat = {'Animal': 'Cat', 'Animal Owner': 'Terry'}
hamster = {'Animal': 'Hamster', 'Animal Owner': 'Daniel'}

pets = [{'Golden Retriever': 'Kai', 'Parrot': 'Ben', 'Hedgehog': 'Steve', 'Cat': 'Terry', 'Hamster': 'Daniel'}] #stored in a list

for pet in pets:
    for pet in pet.values(): 
        print(pet)
        
print("\nHas a pet\n") #use this print to know everything about each pet 
        
for pet in pets: 
    for pet in pet.keys():
        print(pet) 