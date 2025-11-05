def menu():
    print("Options:")
    print("1 - Insert word")
    print("2 - Show current word")
    print("3 - Show current word in reverse")
    print("0 - Exit")
    return int(input("Your choice: "))

def main():
    print("Program starting.")
    word = ""
    choice = -1
    while choice != 0:
        choice = menu()
        if choice == 1:
            word = input("Insert word: ")
        elif choice == 2:
            print(f"Current word - \"{word}\"")
        elif choice == 3:
            print(f"Word reversed - \"{word[::-1]}\"")
        elif choice == 0:
            print("Exiting program.")
        else:
            print("Unknown option")

print("Program ending.")


main()