###################################
#Task A9_T7
#Developer Tatu Kempas
#2.12.2025
###################################

import sys
import os

def showHelp() -> None:
    print("Usage: python {} <source_file> <destination_file>".format(sys.argv[0]))

def copyFile(PSrcFile: str, PDstFile: str) -> None:
    Proceed = True
    if os.path.exists(PDstFile):
        ans = input('Destination file "{}" exists. Overwrite? (y/n): '.format(PDstFile))
        if ans.lower() != "y":
            Proceed = False
            print("Copy cancelled.")
    if Proceed:
        try:
            with open(PSrcFile, "r", encoding="UTF-8") as src:
                data = src.read()
            with open(PDstFile, "w", encoding="UTF-8") as dst:
                dst.write(data)
            print('Copying file "{}" to "{}".'.format(PSrcFile, PDstFile))
        except Exception as e:
            print("Error: Could not copy file. ({})".format(e))
            sys.exit(-1)

def main() -> None:
    print("Program starting.")
    if len(sys.argv) != 3:
        print("Invalid number of arguments.")
        showHelp()
    else:
        SrcFile = sys.argv[1]
        DstFile = sys.argv[2]
        print('Source file "{}"'.format(SrcFile))
        print('Destination file "{}"'.format(DstFile))
        copyFile(SrcFile, DstFile)
    print("Program ending.")

if __name__ == "__main__":
    main()
