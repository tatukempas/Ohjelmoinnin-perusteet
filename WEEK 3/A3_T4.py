print("Program starting.")
print("This is a program with simple menu where you can choose" \
"which operation the program performs.")
name = str(input("Before the menu please insert your name: "))

print("\nOptions:")
print("1 - Print welcome message")
print("2 - Print the name backwards")
print ("3 - Print the first character")
print("4 - Show the amount of characters in the name")
print("0 - Exit")

option = int(input("Your choice: "))
if(option == 1):
    print(f"Welcome {name}!")

if(option == 2):
    print(f"Your name backwards is {name[::-1]}")

firstchar = name[0]
if(option == 3):
    print(f"The first character of your name '{name}' is '{firstchar}'")

lenght = len(name)
if(option == 4):
    print(f"There are {lenght} characters in the name '{name}'")
if(option == 0):
    print("Exiting...")
elif(option < 0 or option > 4):
    print("Unknown option.")
print("\nProgram ending.")
