#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 20:40:21 2023

@author: aliyya
"""

"""
Chapter 6 Exercise 1: Pizza Toppings
Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,

print a message saying you’ll add that topping to their pizza.
"""

while True: #using while loop for my condition to be true
    toppings = input("Enter your toppings:")
    if toppings.lower()== "quit": #will break the loop once you enter quit as your toppings
        break 
    print("I will add a", toppings, "to your pizza :)")

    

    

    