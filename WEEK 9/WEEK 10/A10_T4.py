###################################
#Task A10_T4
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

def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
    i = j = 0
    PMerge.clear()
    while i < len(PLeft) and j < len(PRight):
        if (PAsc and PLeft[i] <= PRight[j]) or (not PAsc and PLeft[i] >= PRight[j]):
            PMerge.append(PLeft[i])
            i += 1
        else:
            PMerge.append(PRight[j])
            j += 1
    PMerge.extend(PLeft[i:])
    PMerge.extend(PRight[j:])

def mergeSort(PValues: list[int], PAsc: bool = True) -> None:
    if len(PValues) <= 1:
        return
    mid = len(PValues) // 2
    left = PValues[:mid]
    right = PValues[mid:]
    mergeSort(left, PAsc)
    mergeSort(right, PAsc)
    merge(left, right, PValues, PAsc)

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
    mergeSort(asc_values, PAsc=True)
    displayValues(asc_values, "Ascending", Filename)

    desc_values = Values.copy()
    mergeSort(desc_values, PAsc=False)
    displayValues(desc_values, "Descending", Filename)

    Values.clear()
    print("Program ending.")

if __name__ == "__main__":
    main()
