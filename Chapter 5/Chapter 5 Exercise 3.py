#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 12:28:45 2023

@author: aliyya
"""

"""
Chapter 5 Exercise 3: Glossary 2
Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()

calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms

to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.
"""

dictionary = {'if-else statement': 'if the condition is true, else if the body is false.', 
                'arithmetic operators': 'used with numeric values for mathematical operations.', 
                'Variable': 'reusable containter for storing a value;can store data of different types.', 
                'list': 'a collection of which is ordered and changable. Duplicating is OK.', 
                'Tuple': 'collection of which is ordered but unchangable. Duplicating is also OK.', 
                'Float': 'using decimal numbers.', 
                'Integer': 'Is a collection of numbers', 
                'String': 'is a collection of characters',
                'Boolean': 'it represents one of two values using the True or False'}

for i in dictionary.keys():
    print(i) #i use the .keys() to print only the keys in key-value in dictionary.
    
print("\n")   

for i in dictionary.values():
    print(i) #i use the .values() to print only the values in key-value in dictionary.
 
print("\n")  
        
for i in dictionary.items():
    print(i) #i use the .items() to print the items which is the key-value in dictionary.