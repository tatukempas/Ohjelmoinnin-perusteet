DELIMITER = ";"


class TIMESTAMP:
    def __init__(self):
        self.weekday = ""
        self.hour = ""
        self.consumption = 0.0
        self.price = 0.0


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


def print_timestamps(timestamps):
    print("Electricity usage:")
    for ts in timestamps:
        total = ts.price * ts.consumption
        print(" - {} {}, price {:.2f}, consumption {:.2f} kWh, total {:.2f} €"
              .format(ts.weekday, ts.hour, ts.price, ts.consumption, total))


def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    print('Reading file "{}".'.format(filename))
    timestamps = read_timestamps(filename)
    if len(timestamps) > 0:
        print_timestamps(timestamps)
    print("Program ending.")


if __name__ == "__main__":
    main()


