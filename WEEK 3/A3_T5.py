print("Program starting.\n")

print("Options:")

print("1 - Celcius to Fahrenheit")
print("2 - Fahrenheit to Celcius")
print("0 - Exit")

choice = int(input("Your choice: "))

if(choice == 1):
    Celcius = float(input("Insert the amount of Celcius: "))
    Fahrenheits = Celcius * 1.8 + 32
    print(f"{round(Celcius, 1)} °C equals to {round(Fahrenheits, 1)} °F\n")

elif(choice == 2):
    Fahrenheits = float(input("Insert the amount of Fahrenheit: "))
    Celcius = (Fahrenheits - 32) / 1.8
    print(f"{round(Fahrenheits, 1)} °F equals to {round(Celcius, 1)} °C\n")

elif(choice == 0):
    print("Exiting...\n")

else:
    print("Unknown option.\n")

print("Program ending.")