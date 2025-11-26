from svgwrite import Drawing
from svgwrite.shapes import Rect, Circle, Polygon

def drawSquare(PDwg: Drawing, left, top, sideLength, color, strokeColor) -> None:
    PDwg.add(Rect(insert=(left, top),
                  size=(sideLength, sideLength),
                  fill=color,
                  stroke=strokeColor))
    return None

def drawCircle(PDwg: Drawing, centerX, centerY, radius, color, stroke) -> None:
    PDwg.add(Circle(center=(centerX, centerY),
                    r=radius,
                    fill=color,
                    stroke=stroke))
    return None

def saveSvg(PDwg: Drawing, file) -> None:
    PDwg.save(file, pretty=True, indent=2)
    return None
