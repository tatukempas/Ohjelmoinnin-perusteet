print("Program starting.\n")

start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspect = int(input("Insert inspection point: "))

print("")

if stop <= start:
    print("Starting point value must be less than the stopping value.")

if inspect > stop or inspect < start:
    print("Inspection value must be within range of start and stop.")

else:
    print("First loop - inspection with break:")
    for i in range (start, stop):
        if i == inspect:
            break
        else:
            print(i, end=' ')

    print("\nSecond loop - inspection with continue:")
    for i in range (start, stop):
        if i == inspect:
            continue
        else:
            print(i, end=' ')

print("\n\nProgram ending.")