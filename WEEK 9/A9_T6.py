###################################
#Task A9_T6
#Developer Tatu Kempas
#2.12.2025
###################################

def showOptions() -> None:
    print("Options:")
    print("1 - Insert line")
    print("2 - Save lines")
    print("0 - Exit")

def askChoice() -> int:
    try:
        return int(input("Your choice: "))
    except:
        return -1

def saveLines(PLines: list[str]) -> None:
    if not PLines:
        return
    try:
        filename = input("Insert filename: ")
        with open(filename, "w", encoding="UTF-8") as f:
            f.writelines(PLines)
    except:
        print("Error saving file.")

def insertLine(PLines: list[str]) -> None:
    try:
        text = input("Insert text: ")
        PLines.append(text)
    except:
        print("Error inserting line.")

def onInterrupt(PLines: list[str]) -> None:
    print("\nKeyboard interrupt and unsaved progress!")
    if PLines:
        try:
            save_choice = input("Save before quit(y/n)?: ")
            if save_choice.lower() == "y":
                saveLines(PLines)
        except:
            pass

def main() -> None:
    Lines: list[str] = []
    Choice = -1
    print("Program starting.")
    try:
        while Choice != 0:
            showOptions()
            Choice = askChoice()
            if Choice == 1:
                insertLine(Lines)
            elif Choice == 2:
                saveLines(Lines)
            elif Choice == 0:
                print("Exiting program.")
            else:
                print("Unknown option!")
            print("")
    except KeyboardInterrupt:
        onInterrupt(Lines)
    Lines.clear()
    print("Program ending.")

if __name__ == "__main__":
    main()
