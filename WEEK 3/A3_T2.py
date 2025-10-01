print("Program starting.")
print("String comparisons")
word1 = str(input("Insert first word: "))
char = str(input("Insert a character: "))
if(char in word1):
    print(f"The word '{word1}' contains '{char}'.")
else:
    print(f"The word '{word1}' doesn't contain the character '{char}'.")

word2 = str(input("Insert second word: "))
if(word1 == word2):
    print(f"The words are the same alphabetically. '{word1}'.")
elif(word1 > word2):
    print(f"The first word '{word1}' comes before the second word '{word2}' alphabetically.")
else:
    print(f"The first word '{word1}' comes after the second word '{word2}' alphabetically.")
print("Program ending.")