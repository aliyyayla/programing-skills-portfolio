#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 20:58:20 2023

@author: aliyya
"""

"""
Chapter 3 Exercise 6: Shrinking Guest List
    You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.

•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.

•Print a message to each of the two people still on your list, letting them know they’re still invited.

•Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
"""

guestlist = ["Kristen Dodgen", "TXT Soobin", "Anne Hathaway"]
guestlist.pop() #use a pop() to remove a name in the list. 
print(guestlist)
print("Dear Anne, I apologize that we can’t invite you to dinner.")
print(guestlist[0], "You are still invited to our dinner tonight.")
print(guestlist[1], "You are still invited to our dinner tonight.")



