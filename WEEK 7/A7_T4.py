DELIMITER = ";"


class TIMESTAMP:
    def __init__(self):
        self.weekday = ""
        self.hour = ""
        self.consumption = 0.0
        self.price = 0.0


def readTimestamps(filename, timestamps):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            first = True
            for line in file:
                if first:
                    first = False
                    continue
                row = line.rstrip()
                if not row:
                    continue
                columns = row.split(DELIMITER)
                if len(columns) < 4:
                    continue
                try:
                    ts = TIMESTAMP()
                    ts.weekday = columns[0]
                    ts.hour = columns[1]
                    ts.consumption = float(columns[2])
                    ts.price = float(columns[3])
                    timestamps.append(ts)
                except ValueError:
                    continue
    except FileNotFoundError:
        print(f'File "{filename}" not found.')


def displayTimestamps(timestamps):
    print("Electricity usage:")
    total_sum = 0.0
    for ts in timestamps:
        total = ts.price * ts.consumption
        total_sum += total
        print(
            f" - {ts.weekday} {ts.hour}, price {ts.price:.2f}, "
            f"consumption {ts.consumption:.2f} kWh, total {total:.2f} €"
        )


def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    print(f'Reading file "{filename}".')
    timestamps = []
    readTimestamps(filename, timestamps)
    displayTimestamps(timestamps)
    print("Program ending.")


if __name__ == "__main__":
    main()

