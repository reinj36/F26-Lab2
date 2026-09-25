
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Reina James
# Date: 25/9/2026
# Purpose: Practice using if, elif, and else statments.
# Usage: ./lab2c.py

# TO DO 1:
# Prmopt the user to enter a sentence, save it in the variable str1
# Prmopt the user to enter another sentence, save it in the variable str2

#get user input
str1 = input("Enter a sentence: ")
str2 = input("Enter another sentence: ")

# Use if, elif, and else statments with the len() function to check which of the 2 is longer.
# The final result should be:
# ---- is longer then ----
# If they are equal then print:
# ---- and ---- are equal.
# Get input from the user

if (len(str1) > len(str2)) :
    print ("str1 is longer than str2!")
elif (len(str2) > len(str1)) :
    print("str2 is longer than str1!")
else :
    "str1 and str2 are equal."


