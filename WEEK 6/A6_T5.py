def readValues(filename: str):
    values = []
    with open(filename, "r", encoding="UTF-8") as f:
        for line in f:
            row = line.strip()
            if row:
                values.append(int(row))
    return values


def analyseValues(values):
    count = len(values)
    total = sum(values)
    greatest = max(values)
    average = total / count
    return f"Count;Sum;Greatest;Average\n{count};{total};{greatest};{average:.2f}\n"


def main():
    filename = input("Anna tiedoston nimi: ")
    values = readValues(filename)
    result = analyseValues(values)
    print(result)


if __name__ == "__main__":
    main()
