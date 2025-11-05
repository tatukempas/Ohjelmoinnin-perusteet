def frameword(Pword):
    print("*" * (len(Pword)+4))
    print(f"* {Pword} *")
    print("*" * (len(Pword)+4))
    return None


def main():
    print("Program starting.")
    word = input("Insert word: ")
    print("")
    frameword(word)
    print("Program ending.")
main()