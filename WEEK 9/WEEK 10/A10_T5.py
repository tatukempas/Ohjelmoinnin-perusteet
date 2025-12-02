###################################
#Task A10_T5
#Developer Tatu Kempas
#3.12.2025
###################################

import sys

def recursiveFactorial(PNum: int) -> int:
    if PNum <= 1:
        return 1
    return PNum * recursiveFactorial(PNum - 1)

def buildSequence(PNum: int) -> str:
    if PNum <= 1:
        return "1"
    return buildSequence(PNum - 1) + f"*{PNum}"

def main() -> None:
    print("Program starting.")
    try:
        Feed = input("Insert factorial: ")
        Num = int(Feed)
        if Num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            Result = recursiveFactorial(Num)
            Sequence = buildSequence(Num)
            print(f"Factorial {Num}!\n{Sequence} = {Result}")
    except ValueError:
        print(f"Could not convert '{Feed}' to an integer.")
    except RecursionError:
        print("Error: Maximum recursion depth exceeded.")
    print("Program ending.")

if __name__ == "__main__":
    main()

