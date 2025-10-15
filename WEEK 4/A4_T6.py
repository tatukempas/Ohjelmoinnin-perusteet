print("Program starting.")

n = int(input("Insert a positive integer: "))

if n > 0:
    steps = 0
    print(str(n), end="")

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print("->" + str(n), end="")
        steps += 1
        
    print("\nSequence had " + str(steps) + " total steps.\n")

print("Program ending.")