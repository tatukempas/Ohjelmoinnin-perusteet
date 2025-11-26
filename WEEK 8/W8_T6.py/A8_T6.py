from svgwrite import Drawing
from drawLib import drawSquare, drawCircle, saveSvg

def main() -> None:
    print("Program starting.")
    Dwg = Drawing()

    while True:
        print("Options:")
        print("1 - Draw square")
        print("2 - Draw circle")
        print("3 - Save svg")
        print("0 - Exit")
        choice = int(input("Your choice: "))

        if choice == 1:
            print("Insert square")
            left = int(input("- Left edge position: "))
            top = int(input("- Top edge position: "))
            sideLength = int(input("- Side length: "))
            color = input("- Fill color: ")
            strokeColor = input("- Stroke color: ")
            drawSquare(Dwg, left, top, sideLength, color, strokeColor)

        elif choice == 2:
            print("Insert circle")
            centerX = int(input("- Center X position: "))
            centerY = int(input("- Center Y position: "))
            radius = int(input("- Radius: "))
            color = input("- Fill color: ")
            stroke = input("- Stroke color: ")
            drawCircle(Dwg, centerX, centerY, radius, color, stroke)

        elif choice == 3:
            filename = input("Insert filename: ")
            print(f'Saving file to "{filename}"')
            proceed = input("Proceed (y/n)?: ").lower()
            if proceed == "y":
                saveSvg(Dwg, filename)
                print("Vector saved successfully!\n")
            else:
                print("Save cancelled.\n")

        elif choice == 0:
            print("Exiting program.\n")
            break

        else:
            print("Invalid choice.\n")

    print("Program ending.")

if __name__ == "__main__":
    main()
