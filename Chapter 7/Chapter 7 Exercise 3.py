#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 16:35:22 2023

@author: aliyya
"""

"""
Chapter 7 Exercise 3: T-Shirt
Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function

should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional

arguments to make a shirt. Call the function a second time using keyword arguments.
"""

def make_shirt(size,text):
    print("Your Shirt size is:", size)
    print("Your text is:", text)

make_shirt("Medium","MOA FOREVER") #to call my function in the parameter using positional arguments
make_shirt(size = "Medium", text = "MOA FOREVER") #to call my function in the parameter using keyword arguments


    