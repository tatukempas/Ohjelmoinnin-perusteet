DELIMITER = ";"


class TIMESTAMP:
    def __init__(self):
        self.weekday = ""
        self.hour = ""
        self.consumption = 0.0
        self.price = 0.0


class DAY_USAGE:
    def __init__(self):
        self.day = ""
        self.total_consumption = 0.0
        self.total_cost = 0.0


def read_timestamps(filename):
    timestamps = []
    first = True
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if first:
                first = False
                continue

            row = line.rstrip()
            if len(row) == 0:
                continue

            columns = row.split(DELIMITER)

            ts = TIMESTAMP()
            ts.weekday = columns[0]
            ts.hour = columns[1]
            ts.consumption = float(columns[2])
            ts.price = float(columns[3])

            timestamps.append(ts)
            columns.clear()

    return timestamps


def analyse_timestamps(timestamps):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday"]
    analysis = []

    for d in days:
        du = DAY_USAGE()
        du.day = d
        analysis.append(du)

    for ts in timestamps:
        for du in analysis:
            if ts.weekday == du.day:
                du.total_consumption += ts.consumption
                du.total_cost += ts.consumption * ts.price

    return analysis


def build_results(analysis):
    results = []
    results.append("### Electricity consumption summary ###")
    for du in analysis:
        line = " - {} usage {:.2f} kWh, cost {:.2f} €".format(
            du.day, du.total_consumption, du.total_cost
        )
        results.append(line)
    results.append("### Electricity consumption summary ###")
    return results


def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    print('Reading file "{}".'.format(filename))

    timestamps = read_timestamps(filename)

    print("Analysing timestamps.")
    analysis = analyse_timestamps(timestamps)

    print("Displaying results.")
    results = build_results(analysis)

    for r in results:
        print(r)

    print("Program ending.")


if __name__ == "__main__":
    main()
