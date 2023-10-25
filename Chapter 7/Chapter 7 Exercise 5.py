#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 17:22:48 2023

@author: aliyya
"""

"""
Chapter 7 Exercise 5: Cities
Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence,

such as Reykjavik is in Iceland. Give the parameter for the country a default value.

Call your function for three different cities, at least one of which is not in the default country
"""

def describe_city(City, Country):
    print(City, "is in", Country)
    
describe_city("Frankfurt","Germany")
describe_city("Seoul","Korea")
describe_city("Bataan","Philippines") #calling my function three times according to the parameter 


    
    