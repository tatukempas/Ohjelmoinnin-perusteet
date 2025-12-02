###################################
#Task A9_T3
#Developer Tatu Kempas
#2.12.2025
###################################

import sys
import os

print("Program starting.")

filename = input("Insert filename: ")

# Check file existence
if not os.path.isfile(filename):
    print("Couldn't read file \"{}\".".format(filename))
    sys.exit(1)

print("## {} ##".format(filename))

# Read and print file contents
try:
    with open(filename, "r") as f:
        for line in f:
            print(line.rstrip())
except:
    print("Couldn't read file \"{}\".".format(filename))
    sys.exit(1)

print("## {} ##".format(filename))
print("Program ending.")

