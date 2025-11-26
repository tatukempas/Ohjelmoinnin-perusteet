def showOptions() -> None:
    print("\nOptions:")
    print("1 - Read values")
    print("2 - Amount of values")
    print("3 - Calculate sum of values")
    print("4 - Calculate average of values")
    print("0 - Exit")

def askChoice() -> int:
    return int(input("Your choice: "))

def readValues(filename: str) -> list[float]:
    values = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                values.append(float(line))
    return values

def sumValues(values: list[float]) -> float:
    return round(sum(values), 1)

def averageValues(values: list[float]) -> float:
    if values:
        return round(sum(values)/len(values), 1)
    else:
        return 0.0

def main() -> None:
    print("Program starting.")
    values: list[float] = []

    while True:
        showOptions()
        choice = askChoice()

        if choice == 1:
            filename = input("Insert filename: ")
            try:
                values = readValues(filename)
            except FileNotFoundError:
                print("File not found. Try again.")
        elif choice == 2:
            print(f"Amount of values {len(values)}")
        elif choice == 3:
            print(f"Sum of values {sumValues(values)}")
        elif choice == 4:
            print(f"Average of values {averageValues(values)}")
        elif choice == 0:
            print("Exiting program.")
            break
        else:
            print("Unknown option!")

    print("\nProgram ending.")

if __name__ == "__main__":
    main()
