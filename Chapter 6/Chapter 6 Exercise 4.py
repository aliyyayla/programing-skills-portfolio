#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 21:35:03 2023

@author: aliyya
"""

"""
Chapter 6 Exercise 4: Deli
Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.

Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made,

move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.
"""

sandwich_orders = ['Spicy Tuna Sandwich', 'Cheese and Ham Sandwich', 'Egg Mayonnaise Sandwich'] #list with all of my sandwiches
finished_sandwiches = [] #the empty list called finished_sandwiches
    

for i in sandwich_orders: #using the for loop through the sandwich_orders
    print(f"\nHere is your {i}")
    finished_sandwiches.append(i) #to add my sandwich orders to finished sandwiches
    
print("\n") #for space

print("\nlist of the finished sandwiches:")    
for orders in finished_sandwiches:
    print(orders) 

"""
using a for loop for this chapter, to control over a flow statement that is repeating a statements until the condition is satisfied.
"""