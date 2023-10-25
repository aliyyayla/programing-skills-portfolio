#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 12:38:55 2023

@author: aliyya
"""

"""
Chapter 6 Exercise 2: Movie Tickets
A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if

they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their

age, and then tell them the cost of their movie ticket
"""

age = int(input("Enter your age:"))

if(age < 3): #the age is below 3
    print("The ticket is free !")
elif(age >=3 and age <=12): #the age is between 3 and 12
    print("The ticket is $10.")
else: #age is 12 and above
    print("The ticket is $15.") 

"""
using the if-elif-else statement again to make a condition by the given statement.
"""
    
                       