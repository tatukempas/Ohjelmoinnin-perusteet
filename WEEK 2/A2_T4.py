print("Program starting.")

print("Estimate how many minutes you spent on programming...")

task1 = int(input("A1_T1: "))
task2 = int(input("A1_T2: "))
task3 = int(input("A1_T3: "))
task4 = int(input("A1_T4: "))
task5 = int(input("A1_T5: "))
task6 = int(input("A1_T6: "))
task7 = int(input("A1_T7: "))


total = task1 + task2 + task3 + task4 + task5 + task6 + task7
Average = float(total / 7)

print(f"\nIn total you spent {total} minutes on programming.")

print(f"Average per task was {round(Average,2)} min and same rounded to the nearest integer {round(Average)} min.")

print("\nProgram ending.")