WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday"]

def readFile(filename: str, rows: list[str]):
    print(f'Reading file "{filename}".')
    rows.clear()
    with open(filename, "r", encoding="UTF-8") as f:
        next(f)
        for line in f:
            if line.strip():
                rows.append(line.strip())

def analyseTimestamps(rows: list[str], results: list[str]):
    print("Analysing timestamps.")
    results.clear()
    weekday_counts = [0] * len(WEEKDAYS)
    for row in rows:
        for i, day in enumerate(WEEKDAYS):
            if row.startswith(day):
                weekday_counts[i] += 1
    results.append("### Timestamp analysis ###")
    for i, day in enumerate(WEEKDAYS):
        results.append(f" - {day} {weekday_counts[i]} stamps")
    results.append("### Timestamp analysis ###")

def displayResults(results: list[str]):
    print("Displaying results.")
    for line in results:
        print(line)

def main():
    print("Program starting.")
    rows = []
    results = []
    filename = input("Insert filename: ")
    readFile(filename, rows)
    analyseTimestamps(rows, results)
    displayResults(results)
    print("Program ending.")

if __name__ == "__main__":
    main()
