import math
from svgwrite import Drawing
from svgwrite.shapes import Rect, Circle, Polygon

def drawSquare(PDwg: Drawing, left, top, sideLength, fill, stroke) -> None:
    PDwg.add(Rect(insert=(left, top), size=(sideLength, sideLength),
                  fill=fill, stroke=stroke))

def drawCircle(PDwg: Drawing, cx, cy, radius, fill, stroke) -> None:
    PDwg.add(Circle(center=(cx, cy), r=radius, fill=fill, stroke=stroke))

def drawHexagon(PDwg: Drawing, cx, cy, apothem, fill, stroke) -> None:
    circumradius = 2 * apothem / math.sqrt(3)
    points = []
    for i in range(6):
        angle_deg = 30 + i * 60
        angle_rad = math.radians(angle_deg)
        x = cx + circumradius * math.cos(angle_rad)
        y = cy - circumradius * math.sin(angle_rad)
        points.append((round(x), round(y)))
    PDwg.add(Polygon(points=points, fill=fill, stroke=stroke))

def saveSvg(PDwg: Drawing, filename) -> None:
    PDwg.save(pretty=True, indent=2, filename=filename)

def main() -> None:
    print("Program starting.")
    Dwg = Drawing()

    while True:
        print("Options:")
        print("1 - Draw square")
        print("2 - Draw circle")
        print("3 - Draw hexagon")
        print("4 - Save svg")
        print("0 - Exit")
        choice = int(input("Your choice: "))

        if choice == 1:
            print("Insert square")
            left = int(input("- Left edge position: "))
            top = int(input("- Top edge position: "))
            sideLength = int(input("- Side length: "))
            fill = input("- Fill color: ")
            stroke = input("- Stroke color: ")
            drawSquare(Dwg, left, top, sideLength, fill, stroke)

        elif choice == 2:
            print("Insert circle")
            cx = int(input("- Center X position: "))
            cy = int(input("- Center Y position: "))
            radius = int(input("- Radius: "))
            fill = input("- Fill color: ")
            stroke = input("- Stroke color: ")
            drawCircle(Dwg, cx, cy, radius, fill, stroke)

        elif choice == 3:
            print("Insert hexagon details:")
            cx = int(input("Middle point X: "))
            cy = int(input("Middle point Y: "))
            apothem = float(input("Apothem length: "))
            fill = input("Insert fill: ")
            stroke = input("Insert stroke: ")
            drawHexagon(Dwg, cx, cy, apothem, fill, stroke)

        elif choice == 4:
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
