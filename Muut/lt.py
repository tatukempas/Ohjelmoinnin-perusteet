print("Program starting.\n")

print("Options:")
print("1 - Admin user")
print("2 - Regular user")
print("0 - Exit")
choice = int(input("Your choice: "))

omanimi = "Tatu"
admin = omanimi

if choice == 1:
    print("Admin user selected.")
    user = str(input("Insert username: "))
    age = int(input("Insert age: "))
    if age >= 18 and user == admin:
        print("Welcome admin.")
    else:
        print("Access denied.")

elif choice == 2:
    print("Regular user selected.")
    user = str(input("Insert username: "))
    age = int(input("Insert age: "))
    if age >= 18 and user == omanimi:
        print("Welcome user.")
    elif user != omanimi:
        print("Access denied.")
    else:
        print("You are too young to enter.")

elif choice == 0:
    print("Exiting...")
