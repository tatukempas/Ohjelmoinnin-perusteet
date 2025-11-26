import timestamplib

def showOptions() -> None:
    print("\nOptions:")
    print("1 - Calculate amount of timestamps during year")
    print("2 - Calculate amount of timestamps during month")
    print("3 - Calculate amount of timestamps during weekday")
    print("0 - Exit")

def askChoice() -> int:
    choice = input("Your choice: ")
    return int(choice) if choice.isdigit() else -1

def main() -> None:
    print("Program starting.")
    timestamps = []

    filename = input("Insert filename: ")
    timestamplib.readTimestamps(filename, timestamps)

    while True:
        showOptions()
        choice = askChoice()

        if choice == 1:
            year = int(input("Insert year: "))
            amount = timestamplib.calculateYears(year, timestamps)
            print(f"Amount of timestamps during year '{year}' is {amount}")
        elif choice == 2:
            month = input("Insert month: ")
            amount = timestamplib.calculateMonths(month, timestamps)
            print(f"Amount of timestamps during month '{month}' is {amount}")
        elif choice == 3:
            weekday = input("Insert weekday: ")
            amount = timestamplib.calculateWeekdays(weekday, timestamps)
            print(f"Amount of timestamps during weekday '{weekday}' is {amount}")
        elif choice == 0:
            print("Exiting program.")
            break
        else:
            print("Unknown option!")

    print("Program ending.")

if __name__ == "__main__":
    main()
