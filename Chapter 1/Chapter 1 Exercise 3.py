#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 13:48:56 2023

@author: aliyya
"""
"""
Chapter 1 Exercise 3: Print date and time
Write a Python program to display the current date and time.
"""

import datetime 
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

#just like in the previous chapter, i used import to print the current date and time.