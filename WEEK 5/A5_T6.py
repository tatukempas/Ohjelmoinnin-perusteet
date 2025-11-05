def showoptions() -> None:
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    return None

def askchoice() -> int:
    choice = (input("Your choice: "))
    if choice.isnumeric():
        return int(choice)
    else:
        print("Unknown option!")
        return -1

def main() -> None:
    print("Program starting.")
    count = 0
    running = True
    while running:
        showoptions()
        choice = askchoice()

        if choice == 1:
            print(f"Current count - {count}")
        elif choice == 2:
            count += 1
            print("Count increased!")
        elif choice == 3:
            count = 0
            print("Cleared count!")
        elif choice == 0:
            print("Exiting program.")
            running = False
        elif choice == -1:
            pass
        else:
            print("Unknown option!")
            return -1

        print()

    print("Program ending.")            

main()