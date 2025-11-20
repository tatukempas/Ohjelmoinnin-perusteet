def readValues(filename: str):
    values = []
    with open(filename, "r", encoding="UTF-8") as f:
        for line in f:
            row = line.strip()
            if row != "":
                values.append(int(row))
    return values


def analyseValues(values):
    count = len(values)
    total = sum(values)
    greatest = max(values)
    average = total / count

    result = "Count;Sum;Greatest;Average\n"
    result += "{};{};{};{:.2f}\n".format(count, total, greatest, average)
    return result