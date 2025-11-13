def main():
    print ("Program starting.")
    firstname = input("Insert first name: ").strip()
    lastname = input("Insert last name: ").strip()
    filename = input("Insert filename: ").strip()

    with open(filename,"w") as file:
        file.write(firstname + "\n")
        file.write(lastname + "\n")

    print ("Program ending.")

if __name__ == "__main__":
    main()
