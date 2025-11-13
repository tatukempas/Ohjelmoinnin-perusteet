def main():
    print("Program starting.")
    print("This program can read a file.")
    
    filename = input("Insert filename: ").strip()
    
    file = open(filename, "r")
    content = file.read()
    file.close()
    
    print(f'#### START "{filename}" ####')
    print(content)
    print(f'#### END "{filename}" ####')
    
    print("Program ending.")


if __name__ == "__main__":
    main()