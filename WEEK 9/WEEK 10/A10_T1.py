###################################
#Task A10_T1
#Developer Tatu Kempas
#3.12.2025
###################################

def readFile(PFilename: str) -> list[str]:
    try:
        with open(PFilename, "r", encoding="UTF-8") as f:
            lines = [line.strip() for line in f if line.strip()]
        return lines
    except FileNotFoundError:
        print('File "{}" not found.'.format(PFilename))
        return []
    except Exception as e:
        print('Error reading file "{}": {}'.format(PFilename, e))
        return []

def printVertical(PData: list[str]) -> None:
    print("# --- Vertically --- #")
    for value in PData:
        print(value)
    print("# --- Vertically --- #")

def printHorizontal(PData: list[str]) -> None:
    print("# --- Horizontally --- #")
    print(", ".join(PData))
    print("# --- Horizontally --- #")

def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")
    data = readFile(filename)
    if data:
        printVertical(data)
        printHorizontal(data)
    print("Program ending.")

if __name__ == "__main__":
    main()
