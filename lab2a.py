# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Reina James
# Date: 25/9/2026
# Purpose: Create a variable, check its type and print the variable.
# Usage: ./lab2a.py

# TO DO 1: Follow the instructions given in README.md file

#assign user input to x
x = input("Please input a number: ")

#check type of x
type(x) 

#convert x to int
x = int(x)

if (x >= 6) :
    print("x is greater than 6!")

if (x >= 4 and x < 12) :
    print("x is greater than 4 and less than 12!")