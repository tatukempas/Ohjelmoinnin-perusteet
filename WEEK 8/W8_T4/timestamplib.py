from datetime import datetime

MONTHS = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
)

WEEKDAYS = (
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
)

def readTimestamps(filename: str, timestamps: list) -> None:
    timestamps.clear()
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                # Supports format: 2000-04-11T05:01
                timestamps.append(datetime.strptime(line, "%Y-%m-%dT%H:%M"))

def calculateYears(year: int, timestamps: list) -> int:
    return sum(1 for ts in timestamps if ts.year == year)

def calculateMonths(month: str, timestamps: list) -> int:
    month_index = MONTHS.index(month) + 1
    return sum(1 for ts in timestamps if ts.month == month_index)

def calculateWeekdays(weekday: str, timestamps: list) -> int:
    weekday_index = WEEKDAYS.index(weekday)
    return sum(1 for ts in timestamps if ts.weekday() == weekday_index)
