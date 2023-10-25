#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 17:10:05 2023

@author: aliyya
"""

"""
Chapter 7 Exercise 4: Large Shirts
Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a

medium shirt with the default message, and a shirt of any size with a different message.
"""

def make_shirt(size,message):
    print("Your size is:", size)
    print("Your shirt message is:", message)
    
make_shirt("Large", "I Love Python")
make_shirt("Medium", "I Love Python")
make_shirt("Extra  Large", "I Love my Programming Teacher") #calling my function three times as to what the parameter is saying.