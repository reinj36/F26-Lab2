# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Reina James
# Date: 25/9/2026
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2f.py

# TO DO 1: Follow the instructions given in README.md file

import sys
num_args = len(sys.argv) -1
               
if num_args < 2 :
    print("The script requires at least 2 arguments.")
else :
    name = sys.argv[1]
    age = sys.argv[2]

    if num_args == 3 :
        print(f"Hi {name}, you are {age} years old and the script received {num_args} arguments.")
    else :
        print(f"Hi {name}, you are {age} years old and the script recieved {num_args} arguments.")
