#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 15:05:25 2023

@author: aliyya
"""

"""
Chapter 4 Exercise 5: Favorite Fruit
Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.

•Make a list of your three favorite fruits and call it favorite_fruits.

•Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block

should print a statement,such as You really like bananas!
"""

favorite_fruits = ["Cherry", "Grapes", "Mangosteen",]

if "Cherry" in favorite_fruits:
    print("Wow ! You really like Cherries.")
    
if "Grapes" in favorite_fruits:
    print("Wow ! You really like Grapes.")
    
if "Banana" in favorite_fruits:
    print("Wow ! You really like Bananas.")

    
if "Blueberry" in  favorite_fruits:
    print("Wow ! You really like Blueberries.")

if "Mangosteen" in favorite_fruits:
    print("Wow ! You really like Mangosteens.")
    
    
"""
so i printed each fruits in the list called "favorite_fruits" and use the if statements. 
if the fruits are on the list the message will print but if the fruit is not in the list, the message will not print.
"""
    