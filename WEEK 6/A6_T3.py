def read_file(filename):
    print(f"Reading file '{filename}' content.")
    with open(filename, 'r') as file:
        content = file.read()
    print("File content ready in memory.")
    return content


def write_file(filename, content):
    print(f"Writing content into file '{filename}'.")
    with open(filename, 'w') as file:
        file.write(content)
    print("Copying operation complete.")


def main():
    print("Program starting.")
    print("This program can copy a file.")

    source_file = input("Insert source filename: ")
    dest_file = input("Insert destination filename: ")

    content = read_file(source_file)
    write_file(dest_file, content)

    print("Program ending.")


if __name__ == "__main__":
    main()
