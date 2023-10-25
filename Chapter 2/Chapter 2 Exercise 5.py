#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 12:15:01 2023

@author: aliyya
"""

"""
Chapter 2 Exercise 5: USB shopper
A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.

Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.

You will to use the arithmetic operators to complete this exercise.
"""

usb = 6
budget = 50

_bought = (budget/usb) #using arithmetic operations 

_remaining = (budget % usb) #using also arithmetic operation 

print('she can buy', _bought, 'usb sticks.')
print('she will have pounds', _remaining, 'left')

"""
to print the outcome how many usd she bought and how much does she have left
"""