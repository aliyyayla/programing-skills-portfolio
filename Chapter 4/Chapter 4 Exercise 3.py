#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 00:11:06 2023

@author: aliyya
"""

"""
Chapter 4 Exercise 3: Alien Colors#3
Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.

• If the alien is green, print a message that the player earned 5 points.

• If the alien is yellow, print a message that the player earned 10 points.

• If the alien is red, print a message that the player earned 15 points.

• Write three versions of this program, making sure each message is printed for the appropriate color alien.
"""

alien_color = "Green"

if alien_color== "Green":
    print("Hey player ! You just earned 5 points.")
elif alien_color== "Yellow":
    print("Hey player ! You just earned 10 points.")
elif alien_color== "Red":
    print("Hey player ! You just earned 15 points.")

alien_color = "Yellow"

if alien_color== "Green":
    print("Hey player ! You just earned 5 points.")
elif alien_color== "Yellow":
    print("Hey player ! You just earned 10 points.")
elif alien_color== "Red":
    print("Hey player ! You just earned 15 points.")

alien_color = "Red"

if alien_color== "Green":
    print("Hey player ! You just earned 5 points.")
elif alien_color== "Yellow":
    print("Hey player ! You just earned 10 points.")
elif alien_color== "Red":
    print("Hey player ! You just earned 15 points.") 
    
 
"""
using the if-elif condition. Elif condition is when the if condition is not true, try this elif condition. As you can see, i did elif condition in every alien color i did wherein if they input the right color the message will print according to their color and if not, then the print will not show any message.
"""