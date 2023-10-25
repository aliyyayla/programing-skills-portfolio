 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 19:53:11 2023

@author: aliyya
"""

"""
Chapter 4 Exercise 4: Staged of life.
Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:

•If the person is less than 2 years old, print a message that the person is a baby.

•If the person is at least 2 years old but less than 4, print a message that the person is a toddler.

•If the person is at least 4 years old but less than 13, print a message that the person is a kid.

•If the person is at least 13 years old but less than 20, print a message that the person is a teenager.

•If the person is at least 20 years old but less than 65, print a message that the person is an adult.

•If the person is age 65 or older, print a message that the person is an elder.
"""

age =int(input("enter your age:"))

if age <2:
    print("The person is a baby.") 
elif age >=2 and age <4: #the age condition is between 2 and 4 
    print("The person is a toddler.")
elif age>=4 and age <13: #the age condition is between 4 and 13
    print("The person is a kid.")
elif age>=13 and age<20: #the age condition is between 13 and 20
    print("The person is a teenager.")
elif age <=20 and age<65: #the age condition is between 20 and 65
    print("The person is an adult.")
else:
    print("The person is an elder.") #if the if-elif condition is false 

"""
if-elif-else this is the condition, where the if condition didn't work use elif for another condition but if the  else is if the if-elif condition is false.
"""
    
    
        
    