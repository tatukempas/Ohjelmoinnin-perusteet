import mathlib

def showOptions() -> None:
    print("\nOptions:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")

def askChoice() -> int:
    return int(input("Your choice: "))

def askValue(PPrompt: str) -> float:
    return float(input(PPrompt))

def main() -> None:
    print("Program starting.")

    while True:
        showOptions()
        choice = askChoice()

        if choice == 1:
            a = askValue("Insert first addend value: ")
            b = askValue("Insert second addend value: ")
            result = mathlib.add(a, b)
            print(f"{a} + {b} = {result}")
        elif choice == 2:
            a = askValue("Insert minuend value: ")
            b = askValue("Insert subtrahend value: ")
            result = mathlib.subtract(a, b)
            print(f"{a} - {b} = {result}")
        elif choice == 3:
            a = askValue("Insert multiplicant value: ")
            b = askValue("Insert multiplier value: ")
            result = mathlib.multiply(a, b)
            print(f"{a} * {b} = {result}")
        elif choice == 4:
            a = askValue("Insert dividend value: ")
            b = askValue("Insert divisor value: ")
            result = mathlib.divide(a, b)
            print(f"{a} / {b} = {result}")
        elif choice == 0:
            print("Exiting program.")
            break
        else:
            print("Unknown option!")

    print("\nProgram ending.")

if __name__ == "__main__":
    main()
