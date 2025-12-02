###################################
#Task A9_T5
#Developer Tatu Kempas
#2.12.2025
###################################

def askIntByte(PPrompt: str) -> int:
    Feed = input(PPrompt)
    try:
        f = float(Feed)
        i = int(f)
        if f != i:
            raise Exception()
        if not (0 <= i <= 255):
            raise Exception()
        return i
    except:
        raise Exception()

def createHex(PRed: int, PGreen: int, PBlue: int) -> str:
    return "#{:02x}{:02x}{:02x}".format(PRed, PGreen, PBlue)

def main():
    print("Program starting.")
    try:
        r = askIntByte("Insert red: ")
        g = askIntByte("Insert green: ")
        b = askIntByte("Insert blue: ")
        h = createHex(r, g, b)
        print("RGB Details:")
        print("- Red {}".format(r))
        print("- Green {}".format(g))
        print("- Blue {}".format(b))
        print("- Hex {}".format(h))
        print(format(r, "08b"))
        print(format(g, "08b"))
        print(format(b, "08b"))
    except:
        print("Couldn't perform the designed task due to the invalid input values.")
    print("Program ending.")

if __name__ == "__main__":
    main()