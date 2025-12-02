###################################
#Task A10_T2
#Developer Tatu Kempas
#3.12.2025
###################################

import sys

def readValues(PFilename: str, PValues: list[int]) -> None:
    try:
        with open(PFilename, "r", encoding="UTF-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        value = int(line)
                        PValues.append(value)
                    except ValueError:
                        print('Warning: Skipping invalid integer "{}"'.format(line))
    except FileNotFoundError:
        print('File "{}" not found.'.format(PFilename))
        sys.exit(-1)
    except Exception as e:
        print('Error reading file "{}": {}'.format(PFilename, e))
        sys.exit(-1)

def sumOfValues(PValues: list[int]) -> int:
    total = 0
    for val in PValues:
        total += val
    return total

def productOfValues(PValues: list[int]) -> int:
    product = 1
    for val in PValues:
        product *= val
    return product

def main() -> None:
    Values: list[int] = []
    print("Program starting.")
    filename = input("Insert filename: ")
    readValues(filename, Values)
    
    total_sum = sumOfValues(Values)
    total_product = productOfValues(Values)
    
    print("# --- Sum of numbers --- #")
    print(total_sum)
    print("# --- Sum of numbers --- #")
    
    print("# --- Product of numbers --- #")
    print(total_product)
    print("# --- Product of numbers --- #")
    
    Values.clear()
    print("Program ending.")

if __name__ == "__main__":
    main()
