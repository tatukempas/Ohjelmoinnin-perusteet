SEPARATOR = ";"

def readValues(filename: str) -> str:
    with open(filename, "r", encoding="UTF-8") as f:
        lines = f.readlines()
    values = ""
    for line in lines:
        number = line.strip()
        if values == "":
            values += number
        else:
            values += SEPARATOR + number
    return values

def analyseNumbers(values_str: str) -> str:
    parts = values_str.split(SEPARATOR)
    numbers = [int(x) for x in parts]
    count = len(numbers)
    total = sum(numbers)
    greatest = max(numbers)
    average = total / count
    results = f"{count}{SEPARATOR}{total}{SEPARATOR}{greatest}{SEPARATOR}{average:.2f}"
    return results

def displayResults(filename: str, results: str):
    print("#### Number analysis - START ####")
    print(f'File "{filename}" results:')
    print("Count;Sum;Greatest;Average")
    print(results)
    print()
    print("#### Number analysis - END ####")

def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    values_str = readValues(filename)
    results = analyseNumbers(values_str)
    displayResults(filename, results)
    print("Program ending.")

if __name__ == "__main__":
    main()
