###################################
#Task A9_T1
#Developer Tatu Kempas
#2.12.2025
###################################

print("Program starting.\n")

total = 0.0

while True:
    user_input = input("Insert a floating-point value (0 to stop): ")

    try:
        value = float(user_input)
    except ValueError:
        print("Error! '{}' couldn't be converted to float.".format(user_input))
        continue

    if value == 0:
        break

    total += value

print("\nFinal sum is {:.2f}".format(total))
print("Program ending.")
