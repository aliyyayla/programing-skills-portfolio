#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 18:30:56 2023

@author: aliyya
"""

"""
Chapter 5 Exercise 4: Rivers
Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

Use a loop to print the name of each river included in the dictionary.

Use a loop to print the name of each country included in the dictionary.
"""

rivers = {'Mississippi': 'Mexico', 'Jordan River': 'Jordan', 'Amazon': 'South America'}

for moon in rivers:
    print((moon), "Flows through", rivers[moon])

print("\nRivers\n")   
for moon in rivers.keys(): #only the key in key-value will print
        print(moon)

print("\nCountry\n")
for moon in rivers.values(): #only the value in key-value will print
        print(moon)
    
