print("Program starting.\n")

wordcount = 0
charcount = 0

while True:
    word = input("Insert word (empty stops): ")
    if word == "":
        break
    wordcount += 1
    charcount += len(word)

print("\nYou inserted:")
print(f"- {wordcount} words")
print(f"- {charcount} characters\n")

print("Program ending.")