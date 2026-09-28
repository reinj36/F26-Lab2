# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Reina James
# Date: 28/9/2026
# Purpose: use for loop.
# Usage: ./lab2k.py

# TO DO 1: 
#Follow the instructions given in the README.md file.
#fruits = ["apple", "banana", "cherry", "date"]
# Use a for loop to iterate over the list
#for fruit in fruits:
#    print(fruit)
#for loop is commonly used with range functions. Here's another example using the range function to print numbers from 0  to 5.


#Lab2k :

#initialize sum to 0
sum = 0

#iterates until 100, if i is even, add to sum
for i in range(101) : 
    if i % 2 == 0 :
        sum = sum + i

#print sum
print("Sum:", sum)
