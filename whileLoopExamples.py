# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Reina James
# Date: 27/9/2026
# Purpose: Learn how to use while loops.
# Usage: ./whileLoopExamples.py


#EXAMPLE 1
#Code from example
count = 0  # iteration variable, while loop requires a relevant variable which is used in the loop expression
while count <= 5: # expression (evaluates to True or False)
    print(count)   # Loop body
    count = count + 1  # Loop body, count is incremented,  or else the loop will continue forever
print('loop has ended')  # This statement is not part of loop body. This statement will be executed once the loop condition becomes false.



# Observations

    # When I changed the value of 'count' to 1, the program only ran 4 times.

    #When I changed the expression to 'count < 5', the program ran 5 times (when count = 0).

    #When I changed the expression to 'count <= 5', the program ran 6 times.



# Off-by-one error in loops
    #Sometimes, your code can execute one time too many, one time too few, 
    #or in an array, it can access an index that's one beyond the last index for example.
    #This error usually occurs when there's a mistake in the expression (e.g. the starting
    # value, how many times it should iterate etc). 


#EXAMPLE 2 - Attempt at event-driven loop

print("\n\n")

#number to guess
num = 3

#get user input
userNum = int(input("What number am I thinking of, between 1-10? Enter: "))

#iterate until user guesses correct number
while (userNum != num) :
    print("\nIncorrect! Try again.")
    userNum = int(input("What number am I thinking of, between 1-10? Enter: "))

#run when loop terminates
print("\nCorrect!")