# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Reina James
# Date: 26/9/2026
# Purpose: Learn how and practice using nested if, elif, and else statments..
# Usage: ./lab2g.py

# TO DO 1: Follow the instructions given in README.md file
# Initialize constant variables for the tax rates and rate limits.

#constant variables
TAXRATE_SINGLE_ZERO = 0.1
TAXRATE_SINGLE_8K = 0.15
TAXRATE_SINGLE_32K = 0.25

TAXRATE_MARRIED_ZERO = 0.1
TAXRATE_MARRIED_16K = 0.15
TAXRATE_MARRIED_64K = 0.25



#initialize tax to 0
tax = 0



#get user input and assign to income and status
income = int(input("Please enter your income: "))

status = input("Please enter your status: ")



#create tax calculating program for income using nested if

#calculate tax if SINGLE
if status == "single" :
    if income > 0 and income <= 8000 : #if income is between $0 and $8000, the tax is 10% of income
        tax = income * TAXRATE_SINGLE_ZERO
        print("Tax: $%.2f" %(tax))

    elif income > 8000 and income <= 32000 : #if income is between $8000 and $32000, the tax is $800 + 15% of income
        tax = 800 + (income * TAXRATE_SINGLE_8K)
        print("Tax: $%.2f" %(tax))

    elif income > 32000 : #if income is over $32000, tax is $4400 + 25% of income
        tax = 4400 + (income * TAXRATE_SINGLE_32K)
        print("Tax: $%.2f" %(tax))

    else : #if user enters 0 or a negative value
        print("Please enter a valid amount.")

#calculate tax if MARRIED
elif status == "married" : 
    if income > 0 and income <= 16000 : #if income is between $0 and $16k, tax is 10% of income
        tax = income * TAXRATE_MARRIED_ZERO
        print("Tax: $%.2f" %(tax))
    
    elif income > 16000 and income <= 64000 : #if income is between $16k and $64k, tax is $1600 + 15% of income
        tax = 1600 + (income * TAXRATE_MARRIED_16K)
        print("Tax: $%.2f" %(tax))

    elif income > 64000 : #if income is over $64k, tax is $8800 + 25% of income
        tax = 8800 + (income * TAXRATE_MARRIED_64K)
        print("Tax: $%.2f" %(tax))

    else : #if user enters 0 or a negative value
        print("Please enter a valid amount.")

    