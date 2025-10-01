print("Program starting.")
print("This is a program with simple menu where you can choose" \
"which operation the program performs.")
name = str(input("Before the menu please insert your name: "))

print("\nOptions:")
print("1 - Print welcome message")
print("0 - Exit")
option = int(input("Your choice: "))
if(option == 1):
    print(f"Welcome {name}!")
elif(option == 0):
    print("Exiting...")
else:
    print("Unknown option.")
print("\nProgram ending.")

