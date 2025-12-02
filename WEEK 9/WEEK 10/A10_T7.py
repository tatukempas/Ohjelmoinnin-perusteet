###################################
#Task A10_T7
#Developer Tatu Kempas
#3.12.2025
###################################

import random

random.seed(1234)

def layMines(PMineField: list[list[int]], PMines: int) -> None:
    Rows = len(PMineField)
    Cols = len(PMineField[0]) if Rows > 0 else 0
    MinesPlaced = 0
    while MinesPlaced < PMines:
        r = random.randint(0, Rows - 1)
        c = random.randint(0, Cols - 1)
        if PMineField[r][c] != 9:
            PMineField[r][c] = 9
            MinesPlaced += 1

def calculateNearbys(PMineField: list[list[int]]) -> None:
    Rows = len(PMineField)
    Cols = len(PMineField[0]) if Rows > 0 else 0
    for r in range(Rows):
        for c in range(Cols):
            if PMineField[r][c] == 9:
                continue
            count = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < Rows and 0 <= nc < Cols:
                        if PMineField[nr][nc] == 9:
                            count += 1
            PMineField[r][c] = count

def generateMinefield(PMineField: list[list[int]], PRows: int, PCols: int, PMines: int) -> None:
    PMineField.clear()
    for _ in range(PRows):
        PMineField.append([0] * PCols)
    layMines(PMineField, PMines)
    calculateNearbys(PMineField)

def showOptions() -> None:
    print("Options:")
    print("1 - Generate minesweeper board")
    print("2 - Show generated board")
    print("3 - Save generated board")
    print("0 - Exit")

def askChoice() -> int:
    try:
        return int(input("Your choice: "))
    except ValueError:
        return -1

def showBoard(PMineField: list[list[int]]) -> None:
    if not PMineField:
        print("No board generated yet.")
        return
    for row in PMineField:
        print(row)

def saveBoard(PMineField: list[list[int]]) -> None:
    if not PMineField:
        print("No board generated yet.")
        return
    Filename = input("Insert filename: ")
    try:
        with open(Filename, "w", encoding="UTF-8") as f:
            for row in PMineField:
                f.write(",".join(str(cell) for cell in row) + "\n")
        print(f"Board saved in '{Filename}'")
    except Exception as e:
        print(f"Error saving file '{Filename}': {e}")

def main() -> None:
    MineField: list[list[int]] = []
    Choice = -1
    print("Program starting.")
    while Choice != 0:
        showOptions()
        Choice = askChoice()
        if Choice == 1:
            try:
                Rows = int(input("Insert rows: "))
                Cols = int(input("Insert columns: "))
                Mines = int(input("Insert mines: "))
                if Mines > Rows * Cols:
                    print("Too many mines! Reduce number of mines.")
                    continue
                generateMinefield(MineField, Rows, Cols, Mines)
            except ValueError:
                print("Invalid input. Enter integers only.")
        elif Choice == 2:
            showBoard(MineField)
        elif Choice == 3:
            saveBoard(MineField)
        elif Choice == 0:
            print("Exiting program.")
        else:
            print("Unknown option!")
        print("")
    print("Program ending.")

if __name__ == "__main__":
    main()
