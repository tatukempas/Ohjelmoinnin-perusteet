###################################
#Task A10_T6
#Developer Tatu Kempas
#3.12.2025
###################################

import copy
import time
from typing import Callable

def showOptions() -> None:
    print("Options:")
    print("1 - Read dataset values")
    print("2 - Measure speeds")
    print("3 - Save results")
    print("0 - Exit")

def askChoice() -> int:
    try:
        return int(input("Your choice: "))
    except ValueError:
        return -1

def readValues(PValues: list[int]) -> str:
    PValues.clear()
    Filename = input("Insert dataset filename: ")
    try:
        with open(Filename, "r", encoding="UTF-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    PValues.append(int(line))
        return Filename
    except Exception as e:
        print(f"Error reading file '{Filename}': {e}")
        return ""

def bubbleSort(PNums: list[int]) -> None:
    n = len(PNums)
    for i in range(n):
        for j in range(0, n-i-1):
            if PNums[j] > PNums[j+1]:
                PNums[j], PNums[j+1] = PNums[j+1], PNums[j]

def quickSort(PNums: list[int]) -> None:
    def _quickSort(arr, low, high):
        if low < high:
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i+1], arr[high] = arr[high], arr[i+1]
            pi = i+1
            _quickSort(arr, low, pi-1)
            _quickSort(arr, pi+1, high)
    _quickSort(PNums, 0, len(PNums)-1)

def measureSortingTime(PSortingAlgorithm: Callable, PArr: list[int]) -> int:
    StartTime = time.perf_counter_ns()
    PSortingAlgorithm(PArr)
    EndTime = time.perf_counter_ns()
    return EndTime - StartTime

def saveResults(PResults: list[str]) -> None:
    if not PResults:
        print("No results to save.")
        return
    Filename = input("Insert results filename: ")
    try:
        with open(Filename, "w", encoding="UTF-8") as f:
            for line in PResults:
                f.write(line + "\n")
        print(f"Results saved in '{Filename}'")
    except Exception as e:
        print(f"Error saving file '{Filename}': {e}")

def main() -> None:
    Values: list[int] = []
    Results: list[str] = []
    Filename = ""
    Choice = -1
    print("Program starting.")
    while Choice != 0:
        showOptions()
        Choice = askChoice()
        if Choice == 1:
            Filename = readValues(Values)
        elif Choice == 2:
            if not Values:
                print("Dataset not loaded. Please read dataset first.")
                continue
            Results.clear()
            print(f"Measured speeds for dataset '{Filename}':")
            BuiltinTime = measureSortingTime(sorted, copy.deepcopy(Values))
            print(f" - Built-in sorted {BuiltinTime} ns")
            Results.append(f" - Built-in sorted {BuiltinTime} ns")
            BubbleTime = measureSortingTime(bubbleSort, copy.deepcopy(Values))
            print(f" - Buble sort {BubbleTime} ns")
            Results.append(f" - Buble sort {BubbleTime} ns")
            QuickTime = measureSortingTime(quickSort, copy.deepcopy(Values))
            print(f" - Quick sort {QuickTime} ns")
            Results.append(f" - Quick sort {QuickTime} ns")
        elif Choice == 3:
            saveResults(Results)
        elif Choice == 0:
            print("Exiting program.")
        else:
            print("Unknown option!")
        print("")
    Values.clear()
    Results.clear()
    print("Program ending.")

if __name__ == "__main__":
    main()
