###################################
#Task A10_T3
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
                    PValues.append(int(line))
    except FileNotFoundError:
        print(f'File "{PFilename}" not found.')
        sys.exit(-1)
    except Exception as e:
        print(f'Error reading file "{PFilename}": {e}')
        sys.exit(-1)

def displayValues(PValues: list[int], PLabel: str, PFilename: str) -> None:
    print(f"{PLabel} '{PFilename}' -> {', '.join(str(v) for v in PValues)}")

def bubbleSort(PValues: list[int], PAsc: bool = True) -> None:
    n = len(PValues)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if (PAsc and PValues[j] > PValues[j + 1]) or (not PAsc and PValues[j] < PValues[j + 1]):
                PValues[j], PValues[j + 1] = PValues[j + 1], PValues[j]

def main() -> None:
    Values: list[int] = []
    Filename = ""
    print("Program starting.")

    if len(sys.argv) == 2:
        Filename = sys.argv[1]
    else:
        Filename = input("Insert filename: ")

    readValues(Filename, Values)
    displayValues(Values, "Raw", Filename)

    asc_values = Values.copy()
    bubbleSort(asc_values, PAsc=True)
    displayValues(asc_values, "Ascending", Filename)

    desc_values = Values.copy()
    bubbleSort(desc_values, PAsc=False)
    displayValues(desc_values, "Descending", Filename)

    Values.clear()
    print("Program ending.")

if __name__ == "__main__":
    main()
