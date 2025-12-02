###################################
#Task A9_T2
#Developer Tatu Kempas
#2.12.2025
###################################

import sys

print("Program starting.")

user_input = input("Insert exit code(0-255): ")

try:
    code = int(user_input)
except ValueError:
    print("Error! '{}' is not a valid integer exit code.".format(user_input))
    sys.exit(1)

if code < 0 or code > 255:
    print("Error! Exit code must be between 0 and 255.")
    sys.exit(1)

if code == 0:
    print("Clean exit")
    sys.exit(0)
else:
    print("Error code")
    sys.exit(code)
