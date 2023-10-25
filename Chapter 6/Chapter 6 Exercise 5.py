#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 16:04:51 2023

@author: aliyya
"""

"""
Chapter 6 Exercise 5: No Pastrami
Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code

near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all

occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.
"""

sandwich_orders = ['Spicy Tuna Sandwich', 'Cheese and Ham Sandwich', 'Egg Mayonaise Sandwich','Pastrami'*3]
finished_sandwiches = []

print(sandwich_orders)
print("\nThe Deli has run out of Pastrami, we apologized for the inconvinience.")
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove('Pastrami')
    print(f"\nHere is your {sandwich_orders}")
    

print("\n")
sandwich_orders = ['Spicy Tuna Sandwiches', 'Cheese and Ham Sandwiches', 'Egg Mayonnaise Sandwich']
for i in sandwich_orders: 
    print(f"Here is your {i}")
    finished_sandwiches.append(i)
    
print("\n")
print("\nlist of the finished sandwiches:")    
for orders in finished_sandwiches:
    print(orders) 

"""
i used the for loop through the sandwich_orders. Then i use a .remove() to remove the pastrami order out of the list. like i did in the previous exercise (Exercise 5) i use the .append() to add the list of sandwiches in the finished sandwiches.
"""
