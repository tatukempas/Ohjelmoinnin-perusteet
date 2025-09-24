print("Program starting.\n")

word = input("Insert a closed compound word: ")
reverse = word[::-1]

input(f"\nThe word you inserted is '{word}' and in reverse it is '{reverse}'.")

lenght = (len(word))
print(f"The inserted word lenght is {lenght}")

last = word[-1]
print(f"Last character is '{last}'\n")

print("Take substring from the inserted word by inserting...")
start = int(input("1) Starting point: "))
end = int(input("2) Ending point: "))
step = int(input("3) Step size: "))

substring = word[start:end:step]

print(f"\nThe word '{word}' sliced to the defined substring is '{substring}'.")
print("Program ending.")