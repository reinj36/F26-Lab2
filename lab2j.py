# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Reina James
# Date: 28/9/2026
# Purpose: Learn how to use while loops with break and continue.
# Usage: ./lab2j.py

import math

#get user input and convert to float
num = input("Please type in a number: ")
num = float(num)
print()

#initialize variable for square root of num to 0
numSquareRooted = 0;

#iterates until user enters 0
while True :

    #get user input and convert to float
    num = float(input("Please type in a number: "))


    if num == 0 : #break out of loop if user enters 0
            print("Exiting...")
            break
    elif num < 0 : #continue to next iteration if user enters negative number
        print("Invalid number.")
        print()
        continue
    else : #calculate and print square root of num for all input above 0
         numSquareRooted = math.sqrt(num)
         print(numSquareRooted)

    print() #extra space for formatting
